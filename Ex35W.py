v = int(input("Digite um valor positivo: "))
multiplicador = 1

while (v < 0):
    print("O valor precisa ser positivo.")
    v = int(input("Digite um valor positivo: "))

while (multiplicador > 0) and (multiplicador < 11):
    r = v * multiplicador
    print(f"{v} * {multiplicador} = {r}")
    multiplicador = multiplicador + 1