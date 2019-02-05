import unittest
from unittest import TestCase, mock
from unittest.mock import patch

from app import Matris, Jugadores


class TestJugadoresTestCase(TestCase):

    def setUp(self):
        self.jugador = Jugadores()

    def test_required_properties(self):
        self.assertTrue(hasattr(self.jugador, 'tipo_jugador'))

    def test_jugador_movimiento_reanudar(self):
        with patch('builtins.input', return_value='R'):
            resultado = self.jugador.jugador()
        self.assertEqual(resultado, 'Se reanuda el juego. Jugador Ingrese posición: 012345678')

    #busqueda jugada posible para que gane la maquina retorna falso
    def test_posible_jugada_falso_maquina(self):
       resultado = self.jugador.posible_jugada(['-', 'O', '-'], 'O')

       self.assertFalse(resultado[0])

    #busqueda posible para que bloque jugada del JUGADOR
    def test_posible_jugada_bloqueo_jugador(self):

       resultado = self.jugador.posible_jugada(['-', 'X', 'X'], 'O')
       self.assertTrue(resultado)

    # busqueda posible jugada que retorna verdadero y la posición para ganar
    def test_posible_jugada_ganador_maquina(self):
        resultado = self.jugador.posible_jugada(['-', '0', '0'], 'O')
        self.assertTrue(resultado)


    def test_ingresar_input_valor_valido(self):
        with patch('builtins.input', return_value='1'):
            resultado = self.jugador.ingresar_input('Ingresar Movimiento')
        self.assertEqual(resultado, '1')

    def test_ingresar_input_valor_invalido(self):
        with patch('builtins.input', return_value='n'):
            resultado = self.jugador.ingresar_input('Ingresar Movimiento')
        self.assertFalse(resultado)


def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestJugadoresTestCase('test_ingresar_input_valor_invalido'))
    suite.addTest(TestJugadoresTestCase('test_ingresar_input_valor_valido'))
    suite.addTest(TestJugadoresTestCase('test_jugador_movimiento_reanudar'))
    suite.addTest(TestJugadoresTestCase('test_posible_jugada_falso_maquina'))
    suite.addTest(TestJugadoresTestCase('test_posible_jugada_bloqueo_jugador'))
    suite.addTest(TestJugadoresTestCase('test_posible_jugada_ganador_maquina'))

    return suite


suit = suite()

runner = unittest.TextTestRunner()
runner.run(suit)
