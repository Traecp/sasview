#!/usr/bin/env python
"""
	This software was developed by the University of Tennessee as part of the
	Distributed Data Analysis of Neutron Scattering Experiments (DANSE)
	project funded by the US National Science Foundation.

	If you use DANSE applications to do scientific research that leads to
	publication, we ask that you acknowledge the use of the software with the
	following sentence:

	"This work benefited from DANSE software developed under NSF award DMR-0520547."

	copyright 2008, University of Tennessee
"""

""" Provide functionality for a C extension model

	WARNING: THIS FILE WAS GENERATED BY WRAPPERGENERATOR.PY
 	         DO NOT MODIFY THIS FILE, MODIFY ..\c_extensions\lamellarPS_HG.h
 	         AND RE-RUN THE GENERATOR SCRIPT

"""

from sans.models.BaseComponent import BaseComponent
from sans_extension.c_models import CLamellarPSHGModel
import copy    
    
class LamellarPSHGModel(CLamellarPSHGModel, BaseComponent):
    """ Class that evaluates a LamellarPSHGModel model. 
    	This file was auto-generated from ..\c_extensions\lamellarPS_HG.h.
    	Refer to that file and the structure it contains
    	for details of the model.
    	List of default parameters:
         scale           = 1.0 
         spacing         = 40.0 [A]
         deltaT          = 10.0 [A]
         deltaH          = 2.0 [A]
         sld_tail        = 4e-007 [1/A�]
         sld_head        = 2e-006 [1/A�]
         sld_solvent     = 6e-006 [1/A�]
         n_plates        = 30.0 
         caille          = 0.001 
         background      = 0.001 [1/cm]

    """
        
    def __init__(self):
        """ Initialization """
        
        # Initialize BaseComponent first, then sphere
        BaseComponent.__init__(self)
        CLamellarPSHGModel.__init__(self)
        
        ## Name of the model
        self.name = "LamellarPSHGModel"
        ## Model description
        self.description ="""[Concentrated Lamellar (head+tail) Form Factor]: Calculates the
		intensity from a lyotropic lamellar phase.
		The intensity (form factor and structure factor)
		calculated is for lamellae of two-layer scattering
		length density that are randomly distributed in
		solution (a powder average). The scattering
		length density of the tail region, headgroup
		region, and solvent are taken to be different.
		The model can also be applied to large,
		multi-lamellar vesicles.
		No resolution smeared version is included
		in the structure factor of this model.
		*Parameters: spacing = repeat spacing,
		deltaT = tail length,
		deltaH = headgroup thickness,
		n_plates = # of Lamellar plates
		caille = Caille parameter (<0.8 or <1)
		background = incoherent bgd
		scale = scale factor ..."""
       
		## Parameter details [units, min, max]
        self.details = {}
        self.details['scale'] = ['', None, None]
        self.details['spacing'] = ['[A]', None, None]
        self.details['deltaT'] = ['[A]', None, None]
        self.details['deltaH'] = ['[A]', None, None]
        self.details['sld_tail'] = ['[1/A�]', None, None]
        self.details['sld_head'] = ['[1/A�]', None, None]
        self.details['sld_solvent'] = ['[1/A�]', None, None]
        self.details['n_plates'] = ['', None, None]
        self.details['caille'] = ['', None, None]
        self.details['background'] = ['[1/cm]', None, None]

		## fittable parameters
        self.fixed=['deltaT.width', 'deltaH.width', 'spacing.width']
        
        ## parameters with orientation
        self.orientation_params =[]
   
    def clone(self):
        """ Return a identical copy of self """
        return self._clone(LamellarPSHGModel())   
   
    def run(self, x = 0.0):
        """ Evaluate the model
            @param x: input q, or [q,phi]
            @return: scattering function P(q)
        """
        
        return CLamellarPSHGModel.run(self, x)
   
    def runXY(self, x = 0.0):
        """ Evaluate the model in cartesian coordinates
            @param x: input q, or [qx, qy]
            @return: scattering function P(q)
        """
        
        return CLamellarPSHGModel.runXY(self, x)
        
    def set_dispersion(self, parameter, dispersion):
        """
            Set the dispersion object for a model parameter
            @param parameter: name of the parameter [string]
            @dispersion: dispersion object of type DispersionModel
        """
        return CLamellarPSHGModel.set_dispersion(self, parameter, dispersion.cdisp)
        
   
# End of file
