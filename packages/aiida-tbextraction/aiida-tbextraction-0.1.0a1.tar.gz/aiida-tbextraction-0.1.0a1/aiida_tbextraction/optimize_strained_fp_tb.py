# -*- coding: utf-8 -*-

# © 2017-2019, ETH Zurich, Institut für Theoretische Physik
# Author: Dominik Gresch <greschd@gmx.ch>
"""
Defines the workflow to optimize tight-binding models from DFT inputs with different strain values.
"""

from fsc.export import export

from aiida.work.workchain import WorkChain, ToContext
from aiida.common.links import LinkType

from aiida_tools import check_workchain_step

from aiida_strain.work import ApplyStrainsWithSymmetry  # pylint: disable=import-error,useless-suppression
from aiida_strain.work.util import get_symmetries_key, get_structure_key, get_suffix  # pylint: disable=import-error,useless-suppression

from .optimize_fp_tb import OptimizeFirstPrinciplesTightBinding


@export
class OptimizeStrainedFirstPrinciplesTightBinding(WorkChain):
    """
    Workflow to optimize a DFT-based tight-binding model for different strain values.
    """

    @classmethod
    def define(cls, spec):
        super(OptimizeStrainedFirstPrinciplesTightBinding, cls).define(spec)

        spec.expose_inputs(ApplyStrainsWithSymmetry)
        spec.expose_inputs(
            OptimizeFirstPrinciplesTightBinding,
            exclude=('structure', 'symmetries')
        )

        spec.outline(cls.run_strain, cls.run_optimize_dft_tb, cls.finalize)

    @check_workchain_step
    def run_strain(self):
        """
        Apply strain to the initial structure to get the strained structures.
        """
        return ToContext(
            apply_strains=self.submit(
                ApplyStrainsWithSymmetry,
                **self.exposed_inputs(ApplyStrainsWithSymmetry)
            )
        )

    @check_workchain_step
    def run_optimize_dft_tb(self):
        """
        Run the tight-binding optimization for each strained structure.
        """
        apply_strains_outputs = self.ctx.apply_strains.get_outputs_dict()
        tocontext_kwargs = {}
        for strain in self.inputs.strain_strengths:
            key = 'tbextraction' + get_suffix(strain)
            structure_key = get_structure_key(strain)
            symmetries_key = get_symmetries_key(strain)
            tocontext_kwargs[key] = self.submit(
                OptimizeFirstPrinciplesTightBinding,
                structure=apply_strains_outputs[structure_key],
                symmetries=apply_strains_outputs[symmetries_key],
                **self.exposed_inputs(OptimizeFirstPrinciplesTightBinding)
            )
        return ToContext(**tocontext_kwargs)

    @check_workchain_step
    def finalize(self):
        """
        Retrieve and output results.
        """
        for strain in self.inputs.strain_strengths:
            suffix = get_suffix(strain)
            calc = self.ctx['tbextraction' + suffix]
            for label, node in calc.get_outputs(
                also_labels=True, link_type=LinkType.RETURN
            ):
                self.out(label + suffix, node)
