import cProfile
from src.debitsandcredits import add_credit, delete, main



#Aqui prueba solo la función de agregar un crédito
cProfile.run('add_credit(0,[],20)')
#Aqui se prueba solo la función de borrar un valor
cProfile.run('delete(4,[20,40,50,60],2)')
#Aquí se prueba todo el código con todas sus funciones que se realicen
cProfile.run('main()')
