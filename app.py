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
        self.__salir = ''

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

    @property
    def salir(self):
        return self.__salir

    @salir.setter
    def salir(self, value):
        if value is None:
            raise ValueError
        self.__salir = value

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

        #si ingresa S sale del juego
        if str(moviminto).upper() == 'S':
            self.salir = 'S'
            return True
        #si ingresa R Reanuda el juego
        elif str(moviminto).upper() == 'R':
            self.reanudar_juego()
        elif str(moviminto) in self.posiciones and jugador.upper() in self.jugadores:
            self.tablero[int(moviminto)] = jugador
            self.posiciones = self.posiciones.replace(str(moviminto), '')
            return True
        else:
            return 'Movimeinto no valido, posiciones validas ' + self.posiciones

    def reanudar_juego(self):
        self.posiciones = '012345678'
        self.tablero = [self.posicion_vacio] * 9

    def get_tablero_juego(self):
        for line in [self.tablero[0:3], self.tablero[3:6], self.tablero[6:9]]:
            print('-'.join(line))


class Jugadores(Matris):

    def __init__(self):
        super().__init__()
        self.tipo_jugador = ['Jugador', 'Maquina']

    def jugador(self, posicion):
        definicion = self.get_ganador()

        if definicion is not False and len(self.posiciones) <= 1:
            self.definicion_juego(definicion)
        else:
            flag = self.hacer_movimiento(posicion, 'X')
            if definicion is not False and len(self.posiciones) <= 1:
                self.get_tablero_juego()
                self.definicion_juego(definicion)
            while flag is not True:
                if definicion is not False:
                    self.definicion_juego(definicion)
                print(flag)
                print('Jugador Ingrese posición: ', self.posiciones)
                posicion_elejida = input()
                flag = self.hacer_movimiento(posicion_elejida, 'X')
                self.get_tablero_juego()
                if definicion is not False and len(self.posiciones) <= 1:
                    self.definicion_juego(definicion)
            if flag is True:
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

        flag = []

        # verifico si puede ganar maquina
        for row in self.matris:
            result = self.posible_jugada([self.tablero[i] for i in row], self.jugadores[1])
            if result[0]:
                flag = [self.jugadores[1], row[result[1]]]
                return flag

        # verifico posible jugada de Jugador
        for row in self.matris:
            result = self.posible_jugada([self.tablero[i] for i in row], self.jugadores[0])
            if result[0]:
                flag = [self.jugadores[0], row[result[1]]]

        return flag


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
            posicion_elejida = input()
            jugadores.jugador(posicion_elejida)

        elif jugadores.salir == 'R':
            jugadores.reanudar_juego()
        elif jugadores.salir == 'S':
            return True
        else:
            primer_jugador = 0
            jugadores.maguina()

if __name__ == '__main__':
    run_juego()
