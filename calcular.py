#Função que calcula o fatorial de um número
def calcular_fatorial(num):
    fatorial = 1
    for i in range(1, num + 1):
        fatorial *=i
    return fatorial