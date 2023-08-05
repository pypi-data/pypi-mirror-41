# -*- coding: utf-8 -*-

# © 2017-2019, ETH Zurich, Institut für Theoretische Physik
# Author: Dominik Gresch <greschd@gmx.ch>
"""
Defines a workflow for running the tight-binding calculation and evaluation for a given energy window.
"""

try:
    from collections import ChainMap
except ImportError:
    from chainmap import ChainMap

import numpy as np
from fsc.export import export

from aiida.orm import DataFactory
from aiida.orm.data.base import List, Float
from aiida.orm.calculation.inline import make_inline
from aiida.work.workchain import WorkChain, ToContext, if_
from aiida.common.links import LinkType

from aiida_tools import check_workchain_step
from aiida_tools.workchain_inputs import WORKCHAIN_INPUT_KWARGS, load_object

from ..model_evaluation import ModelEvaluationBase
from ..calculate_tb import TightBindingCalculation


@export
class RunWindow(WorkChain):
    """
    This workchain runs the tight-binding extraction and analysis for a given energy window.
    """

    @classmethod
    def define(cls, spec):
        super(RunWindow, cls).define(spec)
        spec.expose_inputs(TightBindingCalculation)
        spec.expose_inputs(ModelEvaluationBase, exclude=['tb_model'])
        spec.input_namespace(
            'model_evaluation',
            dynamic=True,
            help=
            'Inputs that will be passed to the ``model_evaluation_workflow``.'
        )

        spec.input(
            'window',
            valid_type=List,
            help=
            'Disentaglement energy windows used by Wannier90, given as a list ``[dis_win_min, dis_froz_min, dis_froz_max, dis_win_max]``.'
        )
        spec.input(
            'wannier_bands',
            valid_type=DataFactory('array.bands'),
            help=
            'Input bandstructure for Wannier90, to be written to the ``wannier90.eig`` input file.'
        )
        spec.input(
            'model_evaluation_workflow',
            help=
            'AiiDA workflow that will be used to evaluate the tight-binding model.',
            **WORKCHAIN_INPUT_KWARGS
        )

        spec.expose_outputs(ModelEvaluationBase)
        spec.outline(
            if_(cls.window_valid
                )(cls.calculate_model, cls.evaluate_bands, cls.finalize),
            if_(cls.window_invalid)(cls.abort_invalid)
        )

    @check_workchain_step
    def window_invalid(self):
        """
        Check if a window is invalid.
        """
        return not self.window_valid(show_msg=False)

    @check_workchain_step
    def window_valid(self, show_msg=True):
        """
        Check if a window is valid.
        """
        window_list = self.inputs.window.get_attr('list')
        win_min, froz_min, froz_max, win_max = window_list
        num_wann = int(self.inputs.wannier_parameters.get_attr('num_wann'))

        window_invalid_str = 'Window [{}, ({}, {}), {}] is invalid'.format(
            *window_list
        )

        # window values must be sorted
        if sorted(window_list) != window_list:
            if show_msg:
                self.report(
                    '{}: windows values not sorted.'.
                    format(window_invalid_str)
                )
            return False

        # check number of bands in inner window <= num_wann
        if np.max(self._count_bands(limits=(froz_min, froz_max))) > num_wann:
            if show_msg:
                self.report(
                    '{}: Too many bands in inner window.'.
                    format(window_invalid_str)
                )
            return False
        # check number of bands in outer window >= num_wann
        if np.min(self._count_bands(limits=(win_min, win_max))) < num_wann:
            if show_msg:
                self.report(
                    '{}: Too few bands in outer window.'.
                    format(window_invalid_str)
                )
            return False
        return True

    def _count_bands(self, limits):
        """
        Count the number of bands within the given limits.
        """
        lower, upper = sorted(limits)
        bands = self.inputs.wannier_bands.get_bands()
        band_count = np.sum(
            np.logical_and(lower <= bands, bands <= upper), axis=-1
        )
        return band_count

    @check_workchain_step
    def calculate_model(self):
        """
        Run the tight-binding calculation workflow.
        """
        inputs = self.exposed_inputs(TightBindingCalculation)
        # set the energy window
        inputs.update(
            add_window_parameters_inline(
                wannier_parameters=inputs.pop('wannier_parameters'),
                window=self.inputs.window
            )[1]
        )
        self.report("Calculating tight-binding model.")
        return ToContext(
            tbextraction_calc=self.submit(TightBindingCalculation, **inputs)
        )

    @check_workchain_step
    def evaluate_bands(self):
        """
        Add the tight-binding model to the outputs and run the evaluation workflow.
        """
        tb_model = self.ctx.tbextraction_calc.out.tb_model
        self.report("Adding tight-binding model to output.")
        self.out('tb_model', tb_model)
        self.report("Running model evaluation.")
        return ToContext(
            model_evaluation_wf=self.submit(
                load_object(self.inputs.model_evaluation_workflow),
                tb_model=tb_model,
                **ChainMap(
                    self.inputs.model_evaluation,
                    self.exposed_inputs(ModelEvaluationBase),
                )
            )
        )

    @check_workchain_step
    def finalize(self):
        """
        Add the evaluation outputs.
        """
        for label, node in self.ctx.model_evaluation_wf.get_outputs(
            also_labels=True, link_type=LinkType.RETURN
        ):
            self.report("Adding {} to outputs.".format(label))
            self.out(label, node)

    @check_workchain_step
    def abort_invalid(self):
        """
        Abort when an invalid window is found. The 'cost_value' is set to infinity.
        """
        self.report('Window is invalid, assigning infinite cost_value.')
        self.out('cost_value', Float('inf'))


@make_inline
def add_window_parameters_inline(wannier_parameters, window):
    """
    Adds the window values to the given Wannier90 input parameters.
    """
    param_dict = wannier_parameters.get_dict()
    win_min, froz_min, froz_max, win_max = window.get_attr('list')
    param_dict.update(
        dict(
            dis_win_min=win_min,
            dis_win_max=win_max,
            dis_froz_min=froz_min,
            dis_froz_max=froz_max,
        )
    )
    return {'wannier_parameters': DataFactory('parameter')(dict=param_dict)}
