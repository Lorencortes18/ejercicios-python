negativos = 0
for i in range(0, 20):
    num = int(input("ingrese numeros negativos: "))
    if num < 0:
        negativos += num * -1

print(f"la suma de los numeros negativos convertidos a positivos son:{negativos}")