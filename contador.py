# Tendencias e Innovacion en Tecnologia Agricola

contador = 0 
suma = 0
while True:
    try:
        numero = input("Ingrese un número: ")
        if (numero == "salir"):
            break
        else:
            suma = suma + int(numero)
            contador = contador + 1
            promedio = suma / contador
    except:
        print("Error, debe ingresar un valor numérico")
        contador = contador - 1
        continue
print("Sumatoria:", suma)
print("Contador:", contador)
print("Promedio:", promedio)