import unittest
from unittest import TestCase, mock
from unittest.mock import patch

from app import Matris, Jugadores


class TestJugadoresTestCase(TestCase):

    def setUp(self):
        self.jugador = Jugadores()

    def test_required_properties(self):
        self.assertTrue(hasattr(self.jugador, 'tipo_jugador'))

    def test_jugador_movimiento_correcto(self):

        resultado = self.jugador.jugador(1)
        self.assertEqual(resultado, None)

    def test_jugador_movimiento_incorrecto(self):
        #primiero se envia un valor incorrecto y luego un valor correcto
        with patch('builtins.input', return_value='1'):
            self.jugador.jugador('v')
        print('Success: test_jugador_movimiento_incorrecto')

    def test_jugador_movimiento_salir(self):

        with self.assertRaises(SystemExit) as cm:
            self.jugador.jugador('S')

        self.assertEqual(cm.exception.code, 1)

    def test_jugador_movimiento_reanudar(self):
        with patch('builtins.input', return_value='1'):
            self.jugador.jugador('R')
        self.assertEqual(self.jugador.salir, 'R')

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




def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestJugadoresTestCase('test_required_properties'))
    suite.addTest(TestJugadoresTestCase('test_jugador_movimiento_correcto'))
    suite.addTest(TestJugadoresTestCase('test_jugador_movimiento_incorrecto'))
    suite.addTest(TestJugadoresTestCase('test_jugador_movimiento_salir'))
    suite.addTest(TestJugadoresTestCase('test_jugador_movimiento_salir'))
    suite.addTest(TestJugadoresTestCase('test_jugador_movimiento_reanudar'))
    suite.addTest(TestJugadoresTestCase('test_posible_jugada_falso_maquina'))
    suite.addTest(TestJugadoresTestCase('test_posible_jugada_bloqueo_jugador'))
    suite.addTest(TestJugadoresTestCase('test_posible_jugada_ganador_maquina'))

    return suite


suit = suite()

runner = unittest.TextTestRunner()
runner.run(suit)
