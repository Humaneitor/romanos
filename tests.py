import unittest
from romanos import *

class RomanosTest(unittest.TestCase):

    def test_single_simbol(self):
        sel.assertEqual(romano_a_entero('M'), 1000)
        sel.assertEqual(romano_a_entero('D'), 500)
        sel.assertEqual(romano_a_entero('C'), 100)
        sel.assertEqual(romano_a_entero('L'), 50)
        sel.assertEqual(romano_a_entero('X'), 10)
        sel.assertEqual(romano_a_entero('V'), 5)
        sel.assertEqual(romano_a_entero('I'), 1)

        self.assertRaises(ValueError, romano_a_entero,  'Z')
        self.assertRaises(ValueError, romano_a_entero,  23)