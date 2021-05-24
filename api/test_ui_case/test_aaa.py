'''
Created on May 12, 2021

@author: Administrator
'''
import unittest




class Test(unittest.TestCase):


    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_a(self):

        self.assertEqual(1,1,'fail')
        

    def test_b(self):

        self.assertEqual(2,2,'fail')
        
    def test_c(self):

        self.assertEqual(3,4,'fail')
        
 



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()