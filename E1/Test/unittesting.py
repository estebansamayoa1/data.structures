import unittest
import sys
sys.path.append('/Users/estebansamayoa/Desktop/UFM/Quinto Semestre/Estructura de Datos/E1/src')
import ejercicio1

class Testprueba(unittest.TestCase):

    def test_C(self):
        n=43
        self.assertEqual(ejercicio1.nota(n),"C")

    def test_D(self):
        n=37
        self.assertEqual(ejercicio1.nota(n), "D")

    def test_0(self):
        n=88
        self.assertEqual(ejercicio1.nota(n), "O")        

if __name__ == '__main__':
    unittest.main()