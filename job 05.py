#job 05

def calcul(nombre_1, operateur, nombre_2):
    if operateur == "+":
        return nombre_1 + nombre_2
    elif operateur == "-" and nombre_1 >= nombre_2:
        return nombre_1 - nombre_2    
    elif operateur  == "*":
        return nombre_1 * nombre_2
    elif operateur == "/":
        return nombre_1 / nombre_2
    else:return"Erreur"


print(calcul(8, "+", 6))
print(calcul(2,"-",3))
