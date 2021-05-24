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

        self.assertEqual('a','a','fail')
        

    def test_b(self):

        self.assertEqual('b','c','fail')
        
    def test_c(self):

        self.assertEqual('c','c','fail')
        
 



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()