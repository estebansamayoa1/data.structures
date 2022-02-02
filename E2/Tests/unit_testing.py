import unittest
import src.debitsandcredits as debitsandcredits

class Testprueba(unittest.TestCase):

    def test_agregar(self):
        credits=[]
        debits=[]
        self.assertEqual(debitsandcredits.add_credit(0,credits,20),(1,[20]))
        self.assertEqual(debitsandcredits.add_debit(0,debits,10),(1,[10]))

    def test_borrar(self):
        credits=[10,20,30,40]
        debits=[20,40,60,80]
        self.assertEqual(debitsandcredits.delete(4,debits,2), (3,[20,60,80]))
        self.assertEqual(debitsandcredits.delete(4,credits,2), (3,[10,30,40]))

          

if __name__ == '__main__':
    unittest.main()
