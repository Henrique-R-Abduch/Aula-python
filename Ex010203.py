n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
mai = n1
men = n1
if n2 > mai:
    mai = n2
if n2 < men:
    men = n2
if n1 != n2:
    print(f"O maior número é o {mai} e o menor é o {men}")
else:
    print("Os dois numeros são idênticos")


