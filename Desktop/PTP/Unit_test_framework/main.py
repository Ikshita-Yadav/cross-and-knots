from logging import FATAL
import unittest
from unittest.result import failfast
from selenium import webdriver
import page 

class PythinOrgSearch(unittest.TestCase):

    def setUp(self):#constructor~ for every unit test the constructor will run first then the test and then the destructor
        self.driver =  webdriver.Chrome("C:/Users/ikshi/bin/chromedriver_win32/chromedriver.exe")
        self.driver.get("http://www.python.org")

    def test_exmaple(self):
        print("this is an example of a test that will automatically be tested.")
        assert True# tells us if the test case passes or fails

    def test_example_2(self):
        print("this test will fail")
        assert False

    def not_a_test(self):
        print("only the tests which have the string test in their name in the starting are automatically tested so this will not be tested.")
        assert True

    def tearDown(self):#destructor
        self.driver.close()

if __name__ == "__main__":
    unittest.main()