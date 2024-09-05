amarillo = 0
rosa = 0
roja = 0
verde = 0
azul = 0
i = 0

numeCarros = int(input("ingrese la cantidad de cuantos autos entraron: "))

while i < numeCarros:
    placa = int(input("ingrese el ultimo numero de su placa: "))
    if placa == 1 or placa == 2:
        amarillo += 1
    elif placa == 3 or placa == 4:
        rosa += 1
    elif placa == 5 or placa == 6:
        roja += 1
    elif placa == 7 or placa == 8:
        verde += 1
    elif placa == 9 or placa == 0:
        azul += 1
    else:
        print(f"numero invalido.")
    
    i += 1
    print(f"cantidad de autos amarillos: {amarillo}, cantidad de autos rosa: {rosa}, cantidad de autos rojos: {roja}, cantidad de autos verdes: {verde} y cantidad de autos azules: {azul}")


