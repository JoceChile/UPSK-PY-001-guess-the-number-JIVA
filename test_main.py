import unittest
from unittest.mock import patch
import io
import sys
import random

def adivina_el_numero(numero_secreto, intentos):
    # Redirigir la entrada y salida estándar para usarla en el test
    sys.stdin = io.StringIO('\n'.join(map(str, intentos)))
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Ejecutar la función principal con el número secreto proporcionado
    with patch('random.randint', return_value=numero_secreto):
        import main
    
    # Restaurar la entrada y salida estándar
    sys.stdin = sys.__stdin__
    sys.stdout = sys.__stdout__
    
    # Obtener la salida capturada
    output = captured_output.getvalue().strip()
    
    return output

class TestAdivinaElNumero(unittest.TestCase):
    def test_adivina_numero_correcto(self):
        numero_secreto = 42
        intentos = [42]
        output = adivina_el_numero(numero_secreto, intentos)
        self.assertIn("¡Felicidades! ¡Has adivinado el número!", output)
    
    def test_adivina_numero_menor(self):
        numero_secreto = 75
        intentos = [50, 60, 70, 74, 73, 72, 71, 70, 75]
        output = adivina_el_numero(numero_secreto, intentos)
        self.assertIn("El número secreto es menor.", output)
    
    def test_adivina_numero_mayor(self):
        numero_secreto = 15
        intentos = [20, 18, 16, 15]
        output = adivina_el_numero(numero_secreto, intentos)
        self.assertIn("El número secreto es mayor.", output)
        
if __name__ == '__main__':
    unittest.main()
