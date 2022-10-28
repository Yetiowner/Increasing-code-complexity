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
      if hasattr(HelloWorldBuilder, '_instance'): del HelloWorldBuilder._instance
  
    @unittest.skip("can't easily be tested due to C port")
    def test_main(self):
      '''
      Check if the output to stdout is correct
      '''
      expected = '''Hello world!\nHello world!\nHello world!\nHello world!\nHello world!\nHello world!\nHello world!\nHello world!\nHello world!\nHello world!\n'''

      with patch('sys.stdout', new=StringIO()) as fake_print:
        complication.main()
        self.assertEqual(fake_out.getvalue(), expected)

    @patch("helloworld.c_helloworld")
    def test_main_function(self, mocked):
      complication.main()
      self.assertEqual(mocked.mock_calls, [call('Hello World!')] * 10)
      
    def test_getHello(self):
      from complication import getHello
      self.assertEqual(getHello(), "Hello World!")
      