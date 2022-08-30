#13. Entrar via teclado com três valores distintos. Exibir o maior deles.
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))
mai = men = 0
mai = n1
men = n1
if n2 > mai:
    mai = n2
if n3 > mai:
    mai = n3
if n2 < men:
    men = n2
if n3 < men:
    men = n3
print(f"O maior é {mai} e o menor é {men}")



