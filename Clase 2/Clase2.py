from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, placa, combustible):
        self.__placa = placa             # Encapsulamiento
        self.__combustible = combustible # Encapsulamiento

    @property
    def placa(self):
        return self.__placa

    @property
    def combustible(self):
        return self.__combustible

    def agregar_combustible(self, cantidad):
        if cantidad > 0:
            self.__combustible += cantidad
            print(f"[{self.placa}] Se agregó {cantidad} L de combustible. Total: {self.__combustible}")
        else:
            print("Cantidad inválida.")

    def _consumir(self, cantidad):
        if cantidad <= self.__combustible:
            self.__combustible -= cantidad
        else:
            print(f"[{self.placa}] No hay suficiente combustible. Requiere {cantidad} L.")

    @abstractmethod
    def mover(self, distancia):
        pass

    @abstractmethod
    def calcular_pago(self, minutos):
        pass


class Carro(Vehiculo):
    def mover(self, distancia):
        consumo = distancia * 0.1
        print(f"[Carro {self.placa}] Moviendo {distancia} km.")
        self._consumir(consumo)
        print(f"Combustible restante: {self.combustible:.2f} L")

    def calcular_pago(self, minutos):
        tarifa = 0.05
        total = minutos * tarifa
        return total


class Moto(Vehiculo):
    def mover(self, distancia):
        consumo = distancia * 0.05
        print(f"[Moto {self.placa}] Moviendo {distancia} km.")
        self._consumir(consumo)
        print(f"Combustible restante: {self.combustible:.2f} L")

    def calcular_pago(self, minutos):
        tarifa = 0.03
        return minutos * tarifa


class Camion(Vehiculo):
    def mover(self, distancia):
        consumo = distancia * 0.3
        print(f"[Camión {self.placa}] Moviendo {distancia} km.")
        self._consumir(consumo)
        print(f"Combustible restante: {self.combustible:.2f} L")

    def calcular_pago(self, minutos):
        tarifa = 0.10
        extra = 0
        if minutos > 180:  # Más de 3 horas paga extra
            extra = 5.00
        return minutos * tarifa + extra


# Programa principal
def main():
    vehiculos = [
        Carro("P123ABC", 15),
        Moto("M555XYZ", 6),
        Camion("C999TTT", 40)
    ]

    print("\n---- Simulación de estacionamiento ----")
    for v in vehiculos:
        v.mover(20)  # Polimorfismo
        pago = v.calcular_pago(200)
        print(f"Pago total por {v.placa}: Q{pago:.2f}")
        print("-" * 35)

    print("\n---- Agregar combustible si es necesario ----")
    for v in vehiculos:
        if v.combustible < 5: #
            v.agregar_combustible(10)
        else:
            print(f"[{v.placa}] Tiene suficiente combustible: {v.combustible:.2f} L")


if __name__ == "__main__":
    main()
