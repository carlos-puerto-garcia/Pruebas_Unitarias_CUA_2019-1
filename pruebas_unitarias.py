import unittest
import Calculadora_Melu
import Test_Carlos_PuertoG
import Test2_Carlos_PuertoG
import testAlejandraValencia
import Prueba_Unitaria_AC
import multiplicacionAlejandroVilla
import numeroPrimoAlejandroVilla
import Daniel_Cardona
import formulas
import raiz

'''
creamos los casos de prueba para las funciones
y para eso debemos crear una clase
'''

class Test_raiz(unittest.TestCase):
    def test_raiz(self):
        result=raiz.raiz(100)
        self.assertEqual(result,5)

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
       
class Test_areacilindro (unittest.TestCase):
    def test_area(self):
        result=Prueba_Unitaria_AC.areacilindro(3.14, 3, 3)
        self.assertEqual(result,113.03999999999999)#result=area total del cilindro
        
class TestMultiplicacion (unittest.TestCase):
    def testMultiplicacion(self):
        resultado = multiplicacionAlejandroVilla.multiplicacion (5, 6)
        self.assertEqual(resultado, 30) #Multiplicar dos numeros
        
class TestNumeroPrimo (unittest.TestCase):
    def testNumeroPrimo(self):
        resultado = numeroPrimoAlejandroVilla.primo(5)
        self.assertEqual(resultado, True) #Validar Numero Primo

class Test_potencia(unittest.TestCase): 
    def test_potencia(self):
        result=Daniel_Cardona.potencia(8,2)
        self.assertEqual(result,3) #Validar potencia

class Test_suma(unittest.TestCase):
    def test_suma(self):
        result=formulas.suma(15,23)
        self.assertEqual (result,60)

class Test_resta(unittest.TestCase):
    def test_resta(self):
        result=formulas.resta(28,12)
        self.assertEqual (result,19)        

class Test_multiplicacion(unittest.TestCase):
    def test_multiplicacion(self):
        result=formulas.multiplicacion(7,5)
        self.assertEqual (result,40)

class Test_division(unittest.TestCase):
    def test_division(self):
        result=formulas.division(80,4)
        self.assertEqual (result,13)        

class Test_maximocomundivisor(unittest.TestCase): 
    def test_maximocomundivisor(self):
        result=formulas.maximocomundivisor(30,90)
        self.assertEqual(result,4)

class Test_max(unittest.TestCase): 
    def test_max(self):
        result=formulas.max(30,90,15)
        self.assertEqual(result,max)

#Esto va de último
if __name__ == '__main__':
    unittest.main()
    

