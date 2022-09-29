#53. Armazenar vinte valores em um vetor. Após a digitação, entrar com uma constante multiplicativa que deverá multiplicar cada um dos valores do vetor e armazenar o resultado no próprio vetor, na respectiva posição.
r = 1
lista = []
provisorio = []
for n in range(0,20):
    lista.append(int(input(f"Digite o {n} valor: ")))

mult = float(input("Digite a constante multiplicativa: "))
for a in lista:
    r = a * mult
    provisorio.append(r)

x = sum(provisorio)
lista.append(x)

for i in lista:
    print(f"{i} ", end="")