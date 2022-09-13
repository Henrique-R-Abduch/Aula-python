#37. Exibir a tabuada dos valores de um a vinte, no intervalo de um a dez. Entre as tabuadas, solicitar que o usuário pressione uma tecla.
x = int(input("Digite um número para fazer sua tabuada: "))
for n in range(1, 11):
    t = x * n
    print(f"{x} x {n} = {t}")
a = str(input("Digite uma tecla para ver a tabuada até o 20: "))
if (a != ""):
    for n in range(11, 21):
        t = x * n
        print(f"{x} x {n} = {t}")

