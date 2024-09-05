
hombres = 0
mujeres = 0
perSalon =int(input("ingrese el total de personas en un salon: "))

for i in range (perSalon):
    genero= input("ingrese su genero (MUJER/HOMBRE): ")
    if genero == "mujer": 
        mujeres += 1
    elif genero == 'hombre':
        hombres += 1
    
print(f"la cantidad de hombres es: {hombres}, la cantidad de mujeres es: {mujeres}, la cantidad de personas en el salon es: {perSalon}")


