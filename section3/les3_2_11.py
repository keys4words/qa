import unittest

class TestAbs(unittest.TestCase):
	"""docstring for TestAbs"unittest.TestCasef __init__(self, arg):
		super(TestAbs,unittest.TestCase.__init__()
		self.arg = arg"""
		
	def test_abs1(self):
	    self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

	def test_abs2(self):
	    self.assertEqual(abs(-42), -42, "Should be absolute value of a number")

if __name__ == "__main__":
    unittest.main()