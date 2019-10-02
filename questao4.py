def nob (numero1, numero2):
    unidade1 = numero1 % 10
    dezena1 = numero1 // 10
    unidade2 = numero2 % 10
    dezena2 = numero2 // 10
    resultado = unidade1 + dezena1 + unidade2 + dezena2
    return resultado

def main():
    print(nob(21,36))

main()
