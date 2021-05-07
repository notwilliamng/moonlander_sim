from landerFuncs.py import*
import unittest

class TestFunctions(uniftest.TestCase):
	def test_showWelcome(self):
		self.assertEqual(showWelcome(), "Welcome to the moonlander module")
'''
		def test_getFuel(serlf):
	def test_getAltitude(self):
	def test_displayLMState(self):
	def test_displayLMLandingStaus(self):
	def test_updateAcceleration(self):
	def test_updateAltitude(self):
	def updateFuel(self):
'''

if __name__=='__main__':
	unittest.main()