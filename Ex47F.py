#Calcular o fatorial de um valor que será digitado. Este valor não poderá ser negativo. Enviar mensagem de erro e solicitar o valor novamente, se necessário. Perguntar se o usuário deseja ou não fazer um novo cálculo, consistir a resposta em “S” ou “N”. N! = N x N-1 x N-2 x N-3 x ....... x (N - (N-1)). Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

print("Digite um valor positivo")
n = int(input("Digite um valor: "))
while n < 0:
    print("Valor inválido!")
    n = int(input("Digite um valor: "))
fatorial = 1
for i in range(1, n + 1):
    fatorial = fatorial * i
print("O fatorial de", n, "é", fatorial)

print("Deseja uma nova execução? (S/N))")
resposta = input()
if resposta == "S":
    print("Digite um valor positivo")
    n = int(input("Digite um valor: "))
    while n < 0:
        print("Valor inválido!")
        n = int(input("Digite um valor: "))
    fatorial = 1
    for i in range(1, n + 1):
        fatorial = fatorial * i
    print("O fatorial de", n, "é", fatorial)
else:
    print("Fim do programa")