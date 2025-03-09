def multiplica(quant):
    def multi(valor):
        return valor * quant
    return multi

duplicar = multiplica(2)
triplica = multiplica(3)
quadriplica = multiplica(4)

print(duplicar(2))
print(triplica(2))
print(quadriplica(2))