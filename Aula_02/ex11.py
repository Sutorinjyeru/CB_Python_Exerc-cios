# faça um programa que leia o preço de um produto e retorne o seu preço com 5% de disconto
price = float(input("Me informe o preço original"))
disc = 0.05 * price
result = (price - disc)
print(f"O preço com disconto é de {result}")
