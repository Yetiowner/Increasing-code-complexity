import unittest
from io import StringIO
from unittest.mock import patch


class Case(unittest.TestCase):
    '''
    This is a test for the complication file
    '''

    def test_hello_world(self):
        '''
        Check if the output to stdout is correct
        '''
        expected = '''Hello world!\nHello world!\nHello world!\nHello world!\nHello world!\nHello world!\nHello world!\nHello world!\nHello world!\nHello world!\n'''

        with patch('sys.stdout', new=StringIO()) as fake_out:
            exec(open("./complication.py").read())
            self.assertEqual(fake_out.getvalue(), expected)
