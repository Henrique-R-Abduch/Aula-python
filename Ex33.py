#33. Entrar via teclado com o sexo de determinado usuário, aceitar somente “F” ou “M” como respostas válidas.
sexo = str(input("Digite o sexo da pessoa [M/F]: ")).upper().strip()
while (sexo != "M" and sexo != "F"):
    sexo = str(input("Digite o sexo da pessoa [M/F]: ")).upper().strip()
print(f"A pessoa é do sexo {sexo}")


