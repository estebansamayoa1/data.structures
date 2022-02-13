import unittest
import src.cuadrant as cuadrant

class Testprueba(unittest.TestCase):

    def test_cuadrante(self):
        x=10
        y=20
        self.assertEqual(cuadrant.cuadrante(x,y),(1.0))


          
if __name__ == '__main__':
    unittest.main()