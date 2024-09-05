pesoNiños = 0
pesoJovenes = 0
pesoAdultos = 0
pesoAncianos = 0

niños = 0
jovenes = 0
adultos = 0
ancianos = 0

for i in range(1, 3):
    edades = int(input("ingrese su edad: "))  
    pesos = int(input("ingrese su peso: "))

    if 0 <= edades <= 12:  
        niños += 1         
        pesoNiños += pesos  
    elif 13 <= edades <= 29:
        jovenes += 1
        pesoJovenes += pesos

    elif 30 <= edades <= 59:
        adultos += 1
        pesoAdultos += pesos
    elif edades >= 60:
        ancianos += 1
        pesoAncianos += pesos
        
promedioNiño = pesoNiños / niños
promedioJovenes = pesoJovenes / jovenes
promedioAdultos = pesoAdultos / adultos
promedioAncianos = pesoAncianos / ancianos

print(f"El promedio de los niños: {promedioNiño}, el promedio de los Jovenes: {promedioJovenes}, el promedio de los adultos: {promedioAdultos} y el promedio de los ancianos: {promedioAncianos}")

