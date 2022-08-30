#14. Entrar com o peso e a altura de uma determinada pessoa. Após a digitação, exibir se 
# esta pessoa está ou não com seu peso ideal. Fórmula: peso/altura².
#17. Entrar com o peso, o sexo e a altura de uma determinada pessoa. Após a digitação, exibir se esta pessoa
#está ou não com seu peso ideal. Fórmula: peso/altura².
p = float(input("Digite seu peso: "))
a = float(input("Digite sua altura: "))
sexo = str(input("Digite seu sexo [M/F]: ")).upper().strip()
imc = p / (a ** 2)
print(f"Seu imc é de {imc:.1f}")
if sexo == "M":
    if imc < 20:
        imc = "Abaixo do peso"
    elif imc >= 20 and imc < 25:
        imc = "Peso ideal"
    elif imc >= 25:
        imc = "Acime do peso"
if sexo == "F":
    if imc < 19:
        imc = "Abaixo do peso"    
    elif imc >= 19 and imc < 24:
        imc = "Peso ideal"
    elif imc >= 24:
        imc = "Acima do peso"

print(f"{imc}")


