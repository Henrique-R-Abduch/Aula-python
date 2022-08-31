#18. A partir dos valores da aceleração (a em m/s2), da velocidade inicial (v0 em m/s) e do tempo de percurso (t em s).
valor_aceleracao = float(input("Digite a aceleração: "))
velocidade_inicial = float(input("Digite a velocidade inicial: "))
tempo_de_percurso = float(input("Digite o tempo de percurso: "))

velocidade_final = (velocidade_inicial + (valor_aceleracao * tempo_de_percurso)) * 3.6

if velocidade_final <= 40:
    print("Veículo muito lento")
elif velocidade_final > 40 and velocidade_final <= 60:
    print("Veículo permitido")
elif velocidade_final > 60 and velocidade_final <= 80:
    print("Velocidade de cruzeiro")
elif velocidade_final > 80 and velocidade_final <= 120:
    print("Veículo rápido")
elif velocidade_final > 120:
    print("Veículo muito rápido")

