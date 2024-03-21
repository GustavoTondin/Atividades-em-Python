#Uma pessoa foi a um restaurante que está com um prato do dia que custa R$ 35, mas no
#horário do almoço ele é vendido por R$ 25. Quantos reais uma pessoa economizaria pedindo o
#prato do dia no horário do almoço?

while True:
        preco = 35
        dia = int(input("Digite a quantidade de dias que pediu o prato do dia no horário de almoço: "))
        
        economia = dia * 10
        
        print(f"Se voce comeu o prato do dia no horario do almoço por {dia} dias, voce ira economizar {economia}R$ ")
        
        opc = int(input("Deseja fazer o calculo novamente? Digite 1 para SIM || 2 para NÂO"))
        if opc == 2:
            break
        elif opc == 1:
            print("O programa ira reiniciar")
        else:
            print("Você digitou uma opção invalida, o programa vai ser encerrado :)")
            break
            
       
            
            











