import unittest
from unittest import TestCase
from app import Matris


class TestMatrisTestCase(TestCase):

    def setUp(self):
        self.matris = Matris()

    def test_required_properties(self):
        self.assertTrue(hasattr(self.matris, 'posicion_vacio'))
        self.assertTrue(hasattr(self.matris, 'jugadores'))
        self.assertTrue(hasattr(self.matris, 'posiciones'))
        self.assertTrue(hasattr(self.matris, 'matris'))
        self.assertTrue(hasattr(self.matris, 'salir'))

    def test_set_tablero(self):
        self.assertEqual(self.matris.tablero, ['-', '-', '-', '-', '-', '-', '-', '-', '-'])

    def test_set_tablero_vacio_raises_error(self):

        with self.assertRaises(TypeError) as exception:
            self.matris.tablero = None

        exception = exception.exception
        self.assertEqual(exception.args[0], 'Tablero no puede estar vacio')

    def test_set_tablero_isinstance_error(self):
        with self.assertRaises(TypeError) as exception:
            self.matris.tablero = {}

        exception = exception.exception
        self.assertEqual(exception.args[0], 'Tablero debe ser una lista')

    def test_posiciones(self):
        self.assertEqual(self.matris.posiciones, '012345678')

    def test_posiciones_vacio_raises_error(self):

        with self.assertRaises(TypeError) as exception:
            self.matris.posiciones = None

        exception = exception.exception
        self.assertEqual(exception.args[0], 'Posición no puede estar vacio')

    def test_get_ganador_maquina(self):
        self.matris.hacer_movimiento(0, 'x')
        self.matris.hacer_movimiento(3, 'o')
        self.matris.hacer_movimiento(2, 'x')

        self.matris.hacer_movimiento(1, 'x')
        self.matris.hacer_movimiento(4, 'o')
        self.matris.hacer_movimiento(5, 'o')
        print(self.matris.get_ganador())

        self.assertEqual('X', self.matris.get_ganador())

    def test_get_ganador_jugador(self):
        self.matris.hacer_movimiento(0, 'O')
        self.matris.hacer_movimiento(3, 'X')
        self.matris.hacer_movimiento(2, 'O')

        self.matris.hacer_movimiento(1, 'O')
        self.matris.hacer_movimiento(8, 'X')
        self.matris.hacer_movimiento(5, 'X')

        self.assertEqual('O', self.matris.get_ganador())

    def test_lista_igual_true(self):

        resultado = self.matris.lista_igual(['X', 'X', 'X'], 3)

        self.assertTrue(resultado)

    def test_lista_igual_false(self):

        resultado = self.matris.lista_igual(['X', 'X', '-'], 3)

        self.assertFalse(resultado)

    def test_hacer_movimiento_salir(self):
        resultado = self.matris.hacer_movimiento('S', '0')
        self.assertTrue(resultado)

    def test_hacer_movimiento_reanudar(self):

        self.matris.hacer_movimiento(0, 'X')
        self.matris.hacer_movimiento(3, '0')
        self.matris.hacer_movimiento(2, 'X')

        self.matris.hacer_movimiento('R', '0')

        self.assertEqual(self.matris.tablero, ['-', '-', '-', '-', '-', '-', '-', '-', '-'])
        self.assertEqual(self.matris.posiciones, '012345678')


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestMatrisTestCase('test_required_properties'))
    suite.addTest(TestMatrisTestCase('test_set_tablero_vacio_raises_error'))
    suite.addTest(TestMatrisTestCase('test_set_tablero_isinstance_error'))
    suite.addTest(TestMatrisTestCase('test_get_ganador_maquina'))
    suite.addTest(TestMatrisTestCase('test_get_ganador_jugador'))
    suite.addTest(TestMatrisTestCase('test_posiciones_vacio_raises_error'))
    suite.addTest(TestMatrisTestCase('test_lista_igual_true'))
    suite.addTest(TestMatrisTestCase('test_lista_igual_false'))
    suite.addTest(TestMatrisTestCase('test_hacer_movimiento_salir'))
    suite.addTest(TestMatrisTestCase('test_hacer_movimiento_reanudar'))


    return suite


suit = suite()

runner = unittest.TextTestRunner()
runner.run(suit)
