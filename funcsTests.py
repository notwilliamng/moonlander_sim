import unittest
from landerFuncs import*

class TestCases(unittest.TestCase):
	def test_updateacceleration(self):
		self.assertAlmostEqual(updateAcceleration(0),-1.62)
		self.assertAlmostEqual(updateAcceleration(1),-1.296)
		self.assertAlmostEqual(updateAcceleration(9),1.296)
		self.assertAlmostEqual(updateAcceleration(1.62),-1.09512)

	def test_updateAltitdue(self):
		self.assertAlmostEqual(updateAltitude(1,2,3), 4.5)
		self.assertAlmostEqual(updateAltitude(0,0,0), 0)
		self.assertAlmostEqual(updateAltitude(1,0,0), 1)
		self.assertAlmostEqual(updateAltitude(0,2,0), 2)
		self.assertAlmostEqual(updateAltitude(0,0,2), 1)

	def test_updateFuel(self):
		self.assertAlmostEqual(updateFuel(1,1),0)
		self.assertAlmostEqual(updateFuel(3,2),1)				
		self.assertAlmostEqual(updateFuel(5,1),4)
		self.assertAlmostEqual(updateFuel(9,1),8)
		self.assertAlmostEqual(updateFuel(4,6),-2)




if __name__== "__main__":
	unittest.main()