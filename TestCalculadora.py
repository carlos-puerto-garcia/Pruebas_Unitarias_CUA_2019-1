import unittest
import Calculadora_Melu

class TestCalculadora (unittest.TestCase):
    def testMultiplicacion(self):
        resultado=Calculadora_Melu.multiplicacion (2, 4)
        self.assertEqual(resultado, 8)
        
if __name__ == "__main__":
    unittest.main()
