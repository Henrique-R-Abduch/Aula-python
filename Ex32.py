#32. Entrar com dois valores via teclado, onde o segundo deverá ser maior que o primeiro. Caso contrário solicitar novamente apenas o segundo valor.
n1 = int(input("Digite o primeiro valor (O segundo valor deverá ser maior): "))
n2 = int(input("Digite o segundo valor (Deverá ser maior que o primeiro): "))
while (n2 < n1):
    n2 = int(input("Digitre um número maior que o primeiro: "))
print(f"O primeiro valor foi de {n1} e o segundo foi de {n2}")


