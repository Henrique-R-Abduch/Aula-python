#24. Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. Caso sexo seja “F” e 
# estado civil seja “CASADA”, solicitar o tempo de casada (anos).
nome = str(input("Digite seu nome: "))
sexo = str(input("Digite seu sexo [M/F]: ")).upper().strip()
while sexo not in "M" and sexo not in "F":
    sexo = str(input("Digite o seu sexo [M/F]: ")).upper().strip()
estado_civil = str(input("Digite o seu estado civil [S/C/D/V]: ")).upper().strip()
while estado_civil not in "S" and estado_civil not in "C" and estado_civil not in "D" and estado_civil not in "V":
    estado_civil = str(input("Digite o seu estado civil [S/C/D/V]: ")).upper().strip()
if sexo == "F" and estado_civil == "C":
    tempo_casamento = int(input("Digite (em anos) o seu tempo de casada: "))
    print(f"Nome: {nome}\n Sexo: {sexo}\n Estado civil: {estado_civil}\n Tempo de casada: {tempo_casamento} anos")
else: 
    print(f"Nome: {nome}\n Sexo: {sexo}\n Estado civil: {estado_civil}")