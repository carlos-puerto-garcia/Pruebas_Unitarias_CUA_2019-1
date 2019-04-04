import Test_Carlos_PuertoG
import unittest
import testAlejandraValencia

'''
creamos los casos de prueba para las funciones
y para eso debemos crear una clase
'''

class Test_ejemplo_suma (unittest.TestCase):
    #Escribimos un metodo:
    def test_suma (self):
        result=Test_Carlos_PuertoG.suma(7,3)
        self.assertEqual(result,10)

#Despues de este mensaje ustedes deben integrar sus casos de prueba


class Test_mcd(unittest.TestCase): #Validar máximo común divisor
    def test_mcd(self):
        result=testAlejandraValencia.maximoComunDivisor(35,60)
        self.assertEqual(result,3) #Verificar si el resultado esperado es el correcto
        

#Esto va de último
if __name__ == '__main__':
    unittest.main()
    

