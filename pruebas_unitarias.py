import Test_Carlos_PuertoG
import unittest
import calculadora
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


        class Test_multiplicacion (unittest.TestCase):
    def testmultl(self):
        result=calculadora.multiplicacion (5,10,2)
        self.assertEqual(result,100)

#Esto va de último
if __name__ == '__main__':
    unittest.main()
    

