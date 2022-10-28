import unittest
from io import StringIO
from unittest.mock import patch


class Case(unittest.TestCase):
    '''
    This is a test for the complication file
    '''

    def test_main(self):
      '''
      Check if the output to stdout is correct
      '''
      expected = '''Hello world!\nHello world!\nHello world!\nHello world!\nHello world!\nHello world!\nHello world!\nHello world!\nHello world!\nHello world!\n'''

      with patch('sys.stdout', new=StringIO()) as fake_out:
        __name__ = "__main__"
        exec(open("./complication.py").read())
        self.assertEqual(fake_out.getvalue(), expected)
    def test_getHello(self):
      from complication import getHello
      self.assertEqual(getHello(), "Hello world!")
      