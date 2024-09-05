#leemos el numero del cual queremos la tabla de multiplicar
num = int(input("ingrese el numero para la tabla de multiplicar: "))
#imprimimos la tabla de multiplicar 
print(f"tabla de multiplicar del numero: {num}")

for i in range (1, 11):
    producto = num * i
    print(f"{num}*{i}={producto}")