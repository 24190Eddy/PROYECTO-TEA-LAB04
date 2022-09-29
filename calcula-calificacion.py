# Tendencias e Innovacion en Tecnologia Agricola

def calcularGrade(score):
    if(float(score)> 0.9 and float(score) < 1):
        print("Sobresaliente")
    elif(float(score)> 0.8 and float(score) < 0.9):
        print("Notable")
    elif(float(score)> 0.7 and float(score) < 0.8):
        print("Bien")
    elif(float(score)> 0.6 and float(score) < 0.7):
        print("Suficiente")
    elif(float(score)> 0.5 and float(score) < 0.6):
        print("Insuficiente")

while True:
    score = input("Ingrese puntuación: ")
    if(score == "done"):
        break
    calcularGrade(score)