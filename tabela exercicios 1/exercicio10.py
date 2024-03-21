#Faça um algoritmo que calcule o volume de uma caixa de dimensões informadas pelo usuário e imprima o resultado.

altura = float(input("Informe a altura da caixa: "))
largura = float(input("Informe a largura da caixa: "))
comprimento = float(input("Informe o comprimento da caixa: "))

volume = altura * largura * comprimento

print(f"O volume da caixa e: {volume}")