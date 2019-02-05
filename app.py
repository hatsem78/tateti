import re
from random import randint


class Matris(object):
    __posicion_vacio = '-'

    def __init__(self):
        self.__tablero = [self.posicion_vacio] * 9
        self.__poscisiones = '012345678'
        self._jugadores = ['X', 'O']
        self.__matris = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [2, 4, 6], [0, 4, 8]
        ]

    @property
    def posicion_vacio(self):
        return self.__posicion_vacio

    @property
    def tablero(self):
        return self.__tablero

    @tablero.setter
    def tablero(self, value):
        if value is None:
            raise TypeError("Tablero no puede estar vacio")
        elif not isinstance(value, (list, )):
            raise TypeError("Tablero debe ser una lista")
        self.__tablero = value

    @property
    def jugadores(self):
        return self._jugadores

    @property
    def posiciones(self):
        return self.__poscisiones

    @posiciones.setter
    def posiciones(self, value):
        if value is None:
            raise TypeError("Posición no puede estar vacio")
        self.__poscisiones = value

    @property
    def matris(self):
        return self.__matris

    def get_ganador(self):

        for row in self.matris:

            if self.tablero[row[0]] != self.posicion_vacio and self.lista_igual([self.tablero[i] for i in row], 3):
                return self.tablero[row[0]].upper()
        return False

    def lista_igual(self, lista, count):
        return not lista or lista == [lista[0]] * count

    def get_jugadores(self):
        return self.jugadores

    def hacer_movimiento(self, moviminto, jugador):

        moviminto = re.search('^[s|r]|^[0-9]{1}$', str(moviminto), flags=re.IGNORECASE)

        if moviminto:
            moviminto = moviminto.group(0)
        else:
            return 'Movimeinto no valido, posiciones validas ' + self.posiciones
        if str(moviminto) in self.posiciones and jugador.upper() in self.jugadores:
            self.tablero[int(moviminto)] = jugador
            self.posiciones = self.posiciones.replace(str(moviminto), '')
            return True


    def reanudar_juego(self):
        self.posiciones = '012345678'
        self.tablero = [self.posicion_vacio] * 9

    def get_tablero_juego(self):
        tablero = ''
        for line in [self.tablero[0:3], self.tablero[3:6], self.tablero[6:9]]:
            print(''.join(line))


class Jugadores(Matris):

    def __init__(self):
        super().__init__()
        self.__tipo_jugador = ['Jugador', 'Maquina']

    @property
    def tipo_jugador(self):
        return self.__tipo_jugador

    def jugador(self):
        definicion = self.get_ganador()

        if definicion is not False and len(self.posiciones) <= 1:
            self.definicion_juego(definicion)
        else:
            respuesta = self.ingresar_input('')

            while respuesta is False:
                if definicion is not False:
                    self.definicion_juego(definicion)

                posicion_elejida = self.ingresar_input('Movimeinto no valido, posiciones validas ' + self.posiciones)

                respuesta = self.hacer_movimiento(posicion_elejida, 'X')
                self.get_tablero_juego()
                if definicion is not False and len(self.posiciones) <= 1:
                    self.definicion_juego(definicion)

                    # si ingresa S sale del juego
            if str(respuesta).upper() == 'S':
                exit(1)
                # si ingresa R Reanuda el juego
            elif str(respuesta).upper() == 'R':
                self.reanudar_juego()
                print('Se reanuda el juego. Jugador Ingrese posición: ' + self.posiciones)
                return 'Se reanuda el juego. Jugador Ingrese posición: ' + self.posiciones
            if definicion is not False and len(self.posiciones) <= 1:
                self.get_tablero_juego()
                self.definicion_juego(definicion)

            if respuesta is True:
                self.get_tablero_juego()

    def maguina(self):

        definicion = self.get_ganador()

        if len(self.posiciones) >= 7:
            posicion = self.posiciones[randint(0, len(self.posiciones) - 1)]
            flag = self.hacer_movimiento(posicion, 'O')
            self.get_tablero_juego()
        elif definicion is not False and len(self.posiciones) <= 0:
            self.get_tablero_juego()
            self.definicion_juego(definicion)
        else:

            if definicion is False and self.posiciones != '':

                movimiento = self.get_resultado_posible()
                if len(movimiento) == 0:
                    movimiento = randint(0, len(self.posiciones) - 1)
                else:
                    movimiento = movimiento[1]

                print(movimiento)
                flag = self.hacer_movimiento(str(movimiento), self.jugadores[1])
                self.get_tablero_juego()
                definicion = self.get_ganador()
            else:
                self.get_tablero_juego()
                self.definicion_juego(definicion)

    def definicion_juego(self, definicion):

        self.reanudar_juego()
        if definicion is False:
            print('Fin del juego, Se reanuda el juego')
            self.reanudar_juego()
        else:
            if definicion == 'X':
                print('Ganador del Juego es:', self.tipo_jugador[0])
            else:
                print('Ganador del Juego es:', self.tipo_jugador[1])
            print('Fin del juego, Se reanuda el juego')

    def posible_jugada(self, lista, jugador):
        index = lista.index('-') if '-' in lista else -1
        flag = lista.count(jugador) >= 2 if index > -1 else False
        resultado = [flag, index]

        return resultado

    def get_resultado_posible(self):

        resultado = []

        # verifico si puede ganar maquina
        for row in self.matris:
            result = self.posible_jugada([self.tablero[i] for i in row], self.jugadores[1])
            if result[0]:
                resultado = [self.jugadores[1], row[result[1]]]
                return resultado

        # verifico posible jugada de Jugador
        for row in self.matris:
            result = self.posible_jugada([self.tablero[i] for i in row], self.jugadores[0])
            if result[0]:
                resultado = [self.jugadores[0], row[result[1]]]

        return resultado

    '''control de entrada solo números del 0-9 y
     letras S salida R reanudar'''
    def ingresar_input(self, msg):

        print(msg)
        valor = re.search('^[s|r]|^[0-9]{1}$', input(), flags=re.IGNORECASE)

        if valor:
            return valor.group(0)
        else:
            return False


def run_juego():
    print('Para salir Y, reanudar R')
    jugadores = Jugadores()
    primer_jugador = randint(0, 1)
    posicion_elejida = ''
    while True:
        definicion = jugadores.get_ganador()

        if definicion is not False:
            jugadores.definicion_juego(definicion)
        print((jugadores.tipo_jugador[primer_jugador]), 'Ingrese posición: ', jugadores.posiciones)

        if primer_jugador == 0:
            primer_jugador = 1
            jugadores.jugador()
        else:
            primer_jugador = 0
            jugadores.maguina()

if __name__ == '__main__':
    run_juego()
