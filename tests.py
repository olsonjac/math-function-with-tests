#Create a unittest for the all functions
from math import add
from math import subtract
from math import multiply
from math import capitalize
import unittest
class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,2), 3)
        self.assertEqual(add(5,5), 10)
        self.assertEqual(add(10,10), 20)
        self.assertEqual(add(20,20), 40)
        self.assertEqual(add(40,40), 80)
        self.assertEqual(add(80,80), 160)
        self.assertEqual(add(160,160), 320)
        
    def test_subtract(self):
        self.assertEqual(subtract(2,3), -1)
        self.assertEqual(subtract(5,5), 0)
        self.assertEqual(subtract(10,10), 0)
        self.assertEqual(subtract(20,20), 0)
        self.assertEqual(subtract(40,40), 0)
        self.assertEqual(subtract(80,80), 0)
        self.assertEqual(subtract(160,160), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2,3), 6)
        self.assertEqual(multiply(5,5), 25)
        self.assertEqual(multiply(10,1.5), 15)
        self.assertEqual(multiply(20,20), 400)
        self.assertEqual(multiply(40,40), 1600)
        self.assertEqual(multiply(80,80), 6400)
        self.assertEqual(multiply(160,160), 25600)
    
    def test_capitalize(self):
        self.assertEqual(capitalize('hello'), 'Hello')
        self.assertEqual(capitalize('world'), 'World')
        self.assertEqual(capitalize('python'), 'Python')
        self.assertEqual(capitalize('testing'), 'Testing')

if __name__ == '__main__':
    unittest.main()


    
    
