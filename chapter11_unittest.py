import sys
import unittest

def average(seq):
    return sum(seq) / len(seq)

def get_part(L, to_where):
    return L[:to_where]

class TestAverage(unittest.TestCase):
    #is called individually before each test (not only once)
    def setUp(self): 
        self.l = None

    #is called individually after each test (not only once)
    def tearDown(self):
        pass
        
    def test_python30_zero(self):
        self.assertRaises(ZeroDivisionError, average, [])
        
    def test_python31_zero(self):
        with self.assertRaises(ZeroDivisionError):
            average([])

    def testL(self):
        self.assertRaises(TypeError, get_part, self.l, 1)

    #decorators to skip/avoid/etc tests

    #runs the test but knows it wil fail
    @unittest.expectedFailure 
    def test_expectedFailure(self):
        self.assertEqual(False, True)

    #does not run the test (ever)
    @unittest.skip('text is needed here') 
    def test_skip(self):
        self.assertEqual(False, True)

    #does not run the test if the condition is true
    @unittest.skipIf(sys.version_info.major == 3, "just a text")
    def test_skipif(self):
        self.assertEqual(False, True)
        
    #does run the test if the condition is true
    @unittest.skipUnless(sys.version_info.major == 3, "another text")
    def test_skipunless(self):
        self.assertEqual(False, True)

if __name__ == "__main__":
    unittest.main()
