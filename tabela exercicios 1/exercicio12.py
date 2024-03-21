#Faça um algoritmo que calcule a distância percorrida por um veículo com base em sua velocidade e
#tempo de percurso informados pelo usuário e imprima o resultado.

tempo = float(input("Informe o tempo em horas: "))
velocidade = int(input("Infome a velocidade em Km/h: "))

distancia = velocidade * tempo

print(f"A distancia percorrida pelo veículo foi de: {distancia} Km")