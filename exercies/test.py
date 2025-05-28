class matematicas:

    def __fpotencia(base, exponente):
        return base ** exponente

    def __fraiz_cuadrada(n):
        return pow(n, 0.5)

    def __fesprimo(n):
        n = abs(n)
        if n <= 1:
            return False
        for i in range(2, round(pow(n, 0.5))+1):
            if (n % i == 0):
                return False
            return True

    potencia = staticmethod(__fpotencia)
    raiz_cuadrada = staticmethod(__fraiz_cuadrada)
    esprimo = staticmethod(__fesprimo)


m = matematicas()
print(m.potencia(2, 3))
print(m.raiz_cuadrada(25))
print(m.esprimo(13))
