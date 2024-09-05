positivo = 0
negativo = 0
neutro = 0 
 #leemos los 20 numeros 

for i in range (0, 20):
    num = int(input("ingrese un numero: "))
    if num > 1 :
        positivo +=1
    elif num < 0 :
        negativo += 1
    elif num == 0 or num == 1: 
        neutro += 1

 #verificamos si el numero es positivo, negativo o neutro
    
print(f"los numeros positivos son: {positivo}, los numeros negativos son: {negativo}, y los numeros neutros son: {neutro}")
   
