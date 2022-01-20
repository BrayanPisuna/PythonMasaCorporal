
def calcular_calorias_en_reposo( estatura, peso, edad, valor_genero):
    
    """Calcular tasa de metabolismo basal (TMB) """

    return (10*peso)+(6.25*estatura)-(5*edad)+(valor_genero)



print(" *********************************************")
print("   Calcular tasa de metabolismo basal (TMB)   ")
print(" *********************************************")
peso = float(input("Escriba su peso en Kilogramos (Kg):  "))
print(" ")
estatura = float(input("Escriba su estatura en  Centimetros(cm) :  "))
print(" ")
edad = int(input("Escriba su edad en Años:  "))
print(" ")
valor_genero = int(input(" En caso de ser Masculino debe dijitar (5) y en caso de ser Femenino debe dijitar (-161) : "))

"""Declaracion de los Parametros"""

Porcentaje = calcular_calorias_en_reposo(estatura,peso,edad,valor_genero)

print(" *********************************************")
print("Su TBM es: ", round(Porcentaje,2),"cal")

