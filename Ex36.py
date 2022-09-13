#36. Entrar via teclado com um valor (X) qualquer. Travar a digitação, no sentido de aceitar somente valores positivos. 
# Solicitar o intervalo que o programa que deverá calcular a tabuada do valor digitado, sendo que o segundo valor (B), 
# deverá ser maior que o primeiro (A), caso contrário, digitar novamente somente o segundo. Após a validação dos dados, 
# exibir a tabuada do valor digitado, no intervalo decrescente, ou seja, a tabuada de X no intervalo de B para A.
n = int(input("Insira um valor positivo para ver sua tabuada: "))
while (n <= 0):
    n = int(input("Digite um valor positivo: "))
c = int(input("Digite um valor para iniciar a tabuada: "))
t = int(input("Digite um valor para finalizar a tabuada: "))
while (t <= c):
    t = int(input("Digite um valor para finalizar a tabuadade: "))
while (t >= c):
    tabuada = n * t
    print(f"{n} X {t} = {tabuada}")
    t -= 1
