import unittest
import src.receipt as receipt

class Testprueba(unittest.TestCase):

    def test_comprar(self):
        articulos=[
        ["Cereal","AR01", 25.0],
        ["Pan","AR02", 12.50],
        ["Leche","AR03", 10.25],
        ["Manzana","AR04", 4.75],
        ["Jugo de Naranja","AR05", 17.50],
        ["Cafe","AR06", 45.0],
        ["Tortillas de Harina","AR07", 20.0],
        ["Gelatina","AR08", 4.50],
        ["Galletas","AR09", 11.50],
        ["Naranja","AR10", 2.25]
        ]
        self.assertEqual(receipt.comprar_producto(articulos,[],0,0),([["Cereal","AR01", 25.0]],25.0,1))

    def test_pagar(self):
        self.assertEqual(receipt.pagar_productos([],25.0,0), ([25.0],1))
        
        

if __name__ == '__main__':
    unittest.main()