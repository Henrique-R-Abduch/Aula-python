#26. Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo, imprimindo o resultado.
n = int(input("Digite um valor: "))
if (n >= 0):
    n = n * 2
    print(f"O número é positivo, logo o dobro é {n}")
elif (n < 0):
    n = n * 3
    print(f"o número é negativo, logo o triplo é {n}")







