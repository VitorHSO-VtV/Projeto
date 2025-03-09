class Car:
    def __init__(self, name):
        self.name = name
        self._engine = None
        self._producer = None

        @property
        def engine(self):
            return self._engine

        @engine.setter
        def engine(self, engine):
            self._engine = engine

        @property
        def producer(self):
            return self._producer
        
        @producer.setter
        def producer(self, producer):
            self._producer = producer

class Producer:
    def __init__(self, name):
        self.name = name

class Engine:
    def __init__(self, name):
        self.name = name

fusca = Car('Fusca')
volkswagen = Producer('Volkswagen')
motor_1_0 = Engine('1.0')
fusca.fabricante = volkswagen
fusca.motor = motor_1_0
print(fusca.name, fusca.fabricante.name, fusca.motor.name)

gol = Car('Gol')
gol.fabricante = volkswagen
gol.motor = motor_1_0
print(gol.name, gol.fabricante.name, gol.motor.name)

fiat_uno = Car('Uno')
fiat = Producer('Fiat')
fiat_uno.fabricante = fiat
fiat_uno.motor = motor_1_0
print(fiat_uno.name, fiat_uno.fabricante.name, fiat_uno.motor.name)

focus = Car('Focus Titanium')
ford = Producer('Ford')
motor_2_0 = Engine('2.0')
focus.fabricante = ford
focus.motor = motor_2_0
print(focus.name, focus.fabricante.name, focus.motor.name)

def  teste(testando):
    pass 