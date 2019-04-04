import unittest
import Calculadora_Melu
import Test_Carlos_PuertoG
import Test2_Carlos_PuertoG
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

class TestCalculadora (unittest.TestCase):
    def testMultiplicacion(self):
        resultado=Calculadora_Melu.multiplicacion (2, 4)
        self.assertEqual(resultado, 8)

class Test_multiplicacion(unittest.TestCase):
    def test_multl(self):
        result=Test2_Carlos_PuertoG.multiplicacion(5,3)
        self.assertEqual(result,18)

class Test_mcd(unittest.TestCase): 
    def test_mcd(self):
        result=testAlejandraValencia.maximoComunDivisor(35,60)
        self.assertEqual(result,3) #Validar máximo común divisor
        

#Esto va de último
if __name__ == '__main__':
    unittest.main()
    

