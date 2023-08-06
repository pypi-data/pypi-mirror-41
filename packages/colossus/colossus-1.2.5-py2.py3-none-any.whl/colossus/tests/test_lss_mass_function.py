###################################################################################################
#
# test_lss_mass_function.py (c) Benedikt Diemer
#     				    	    benedikt.diemer@cfa.harvard.edu
#
###################################################################################################

import unittest
import numpy as np

from colossus.tests import test_colossus
from colossus.cosmology import cosmology
from colossus.lss import mass_function
from colossus.lss import peaks

###################################################################################################
# TEST CASES
###################################################################################################

class TCMassFunction(test_colossus.ColosssusTestCase):

	def setUp(self):
		cosmology.setCosmology('planck15')
		pass
		
	def test_hmfInput(self):
		
		M = 1E12
		z = 1.0
		nu = peaks.peakHeight(M, z)
		delta_c = peaks.collapseOverdensity()
		sigma = delta_c / nu
		
		correct = 4.431994181910e-01
		
		mf = mass_function.massFunction(M, z, q_in = 'M', mdef = 'fof', model = 'press74')
		self.assertAlmostEqual(mf, correct, msg = 'Quantity M.')			

		mf = mass_function.massFunction(sigma, z, q_in = 'sigma', mdef = 'fof', model = 'press74')
		self.assertAlmostEqual(mf, correct, msg = 'Quantity sigma.')			

		mf = mass_function.massFunction(nu, z, q_in = 'nu', mdef = 'fof', model = 'press74')
		self.assertAlmostEqual(mf, correct, msg = 'Quantity nu.')			

	def test_hmfConvert(self):
		
		M = 1E13
		z = 0.2
		
		correct = 4.496414343625e-01
		mf = mass_function.massFunction(M, z, q_in = 'M', mdef = 'fof', model = 'press74', q_out = 'f')
		self.assertAlmostEqual(mf, correct, msg = 'Quantity f.')			

		correct = 6.780705345630e-04
		mf = mass_function.massFunction(M, z, q_in = 'M', mdef = 'fof', model = 'press74', q_out = 'dndlnM')
		self.assertAlmostEqual(mf, correct, msg = 'Quantity dndlnM.')			

		correct = 7.910751930078e-02
		mf = mass_function.massFunction(M, z, q_in = 'M', mdef = 'fof', model = 'press74', q_out = 'M2dndM')
		self.assertAlmostEqual(mf, correct, msg = 'Quantity M2dndM.')			
				
	def test_hmfModelsFOF(self):
		models = mass_function.models
		for k in models.keys():
			msg = 'Failure in model = %s.' % (k)
			
			if not 'fof' in models[k].mdefs:
				continue
			
			if k == 'press74':
				correct = [2.236848309312e-01, 1.791604300031e-02]
			elif k == 'sheth99':
				correct = [2.037025979090e-01, 3.217299134400e-02]
			elif k == 'jenkins01':
				correct = [6.026570865773e-02, 3.438245438370e-02]
			elif k == 'reed03':
				correct = [2.037025979090e-01, 2.875270538256e-02]
			elif k == 'warren06':
				correct = [2.176072717238e-01, 3.380303422386e-02]
			elif k == 'reed07':
				correct = [1.912790683881e-01, 3.723943155151e-02]
			elif k == 'crocce10':
				correct = [2.196768758003e-01, 4.195009468463e-02]
			elif k == 'bhattacharya11':
				correct = [2.241129561811e-01, 4.065577992624e-02]
			elif k == 'courtin11':
				correct = [1.519178456652e-01, 4.489022975923e-02]
			elif k == 'angulo12':
				correct = [2.283410678096e-01, 3.769899907588e-02]
			elif k == 'watson13':
				correct = [2.847701359546e-01, 3.803906522670e-02]
			else:
				msg = 'Unknown model, %s.' % k
				raise Exception(msg)
			
			self.assertAlmostEqualArray(mass_function.massFunction(np.array([1E8, 1E15]), 0.0, 
								q_in = 'M', mdef = 'fof', model = k), correct, msg = msg)

	def test_hmfModelsSO_200m(self):
		models = mass_function.models
		for k in models.keys():
			msg = 'Failure in model = %s.' % (k)
			
			mdef = '200m'
			z = 1.0
			
			if not (('*' in models[k].mdefs) or (mdef in models[k].mdefs)):
				continue
			
			if k == 'tinker08':
				correct = [2.510110624301e-01, 4.611808159773e-05]
			elif k == 'watson13':
				correct = [1.621415008597e-01, 4.427873341813e-05]
			elif k == 'bocquet16':
				correct = [2.836178412101e-01, 3.832756307994e-05]
			elif k == 'despali16':
				correct = [2.566878298120e-01, 6.642693089794e-05]
			else:
				msg = 'Unknown model, %s.' % k
				raise Exception(msg)
			
			self.assertAlmostEqualArray(mass_function.massFunction(np.array([1E8, 1E15]), z, 
								q_in = 'M', mdef = mdef, model = k), correct, msg = msg)

	def test_hmfModelsSO_vir(self):
		models = mass_function.models
		for k in models.keys():
			msg = 'Failure in model = %s.' % (k)
			
			mdef = 'vir'
			z = 1.0
			
			if not (('*' in models[k].mdefs) or (mdef in models[k].mdefs)):
				continue
			
			if k == 'tinker08':
				correct = [2.509254068511e-01, 4.540789859771e-05]
			elif k == 'watson13':
				correct = [1.613528810685e-01, 4.366870740478e-05]
			elif k == 'despali16':
				correct = [2.566102311495e-01, 6.539189884732e-05]
			elif k == 'comparat17':
				correct = [2.449553401913e-01, 2.342956829892e-05]
			else:
				msg = 'Unknown model, %s.' % k
				raise Exception(msg)
			
			self.assertAlmostEqualArray(mass_function.massFunction(np.array([1E8, 1E15]), z, 
								q_in = 'M', mdef = mdef, model = k), correct, msg = msg)

###################################################################################################
# TRIGGER
###################################################################################################

if __name__ == '__main__':
	unittest.main()
