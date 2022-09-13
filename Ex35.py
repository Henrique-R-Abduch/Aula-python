#35. Entrar via teclado com um valor qualquer. Travar a digitação, no sentido de aceitar somente valores positivos. 
# Após a digitação, exibir a tabuada do valor solicitado, no intervalo de um a dez.
n = int(input("Digite um número positivo para ver sua tabuada: "))
while (n <= 0):
    n = (int(input("Digite um número positivo para ver sua tabuada: ")))
for d in range(1, 11):
    t = n * d
    print(f"{n} x {d} = {t}")


