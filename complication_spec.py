import unittest
from io import StringIO
from unittest.mock import Mock, patch, call
from sys import modules
import helloworld as hw
import complication
from helloworld_builder import HelloWorldBuilder

class Case(unittest.TestCase):
    '''
    This is a test for the complication file
    '''

    def setUp(self):
      if hasattr(HelloWorldBuilder, '_instance'):
        # Testing caused Hello world! to be printed double
        # due to HelloWorldBuilder being a singleton
        del HelloWorldBuilder._instance

    @patch("helloworld.c_helloworld")
    def test_main_function(self, mocked):
      complication.main()
      self.assertEqual(mocked.mock_calls, [call('Hello World!')] * 10)
      
    def test_getHello(self):
      from complication import getHello
      self.assertEqual(getHello(), "Hello World!")
      