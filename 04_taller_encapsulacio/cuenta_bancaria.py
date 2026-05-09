class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self._titular = titular
        self._saldo = saldo

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, nuevo_saldo):
        if nuevo_saldo < 0:
            raise ValueError("El saldo no puede ser negativo")
        self._saldo = nuevo_saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            return True
        return False

    def retirar(self, cantidad):
        if cantidad <= self._saldo:
            self._saldo -= cantidad
            return True
        return False


def main():
    cuenta = CuentaBancaria("Kevin Zapata", 1000)

    print("Titular:", cuenta.titular)
    print("Saldo inicial:", cuenta.saldo)

    cuenta.depositar(500)
    print("Saldo después del depósito:", cuenta.saldo)

    cuenta.retirar(300)
    print("Saldo después del retiro:", cuenta.saldo)


if __name__ == "__main__":
    main()