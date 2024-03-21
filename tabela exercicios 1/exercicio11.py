#Faça um algoritmo que calcule o desconto de um produto com base em sua porcentagem de desconto e imprima o preço final.

preco = float(input("Digite o valor da mercadoria: "))
desconto = float(input("Digite a porcentagem de desconto: "))

valor_desconto = preco * desconto / 100
pagar = preco - valor_desconto

print(f"Um produto que custa {preco} e possui {desconto}% de desconto custara um preço final de: {pagar} ")
