# Leia o peso de 5 pessoas e mostre o maior e menor peso digitado
great = 0
low = 0

for i in range(1,6):
    weight = int(input("Peso "))
    if i == 1:
        great = weight
        low = weight
    if weight > great:
        great = weight
    elif weight < low:
        low = weight
print(f"O maior foi {great} e o menor foi {low}. ")