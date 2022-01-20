def calcular_calorias_en_reposo( estatura, peso, edad, valor_genero):
    
    #Calcular tasa de metabolismo basal (TMB)

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


# Leemos lo que ingresa el usuario
print("Ingrese segun el numero segun la Actividad Fisica que Realiza ")
print(" ")
print("1.- Poco o Ningún ejercicio - EQUIVALENCIA A (1.2)")
print("2.- Ejercicio ligero (1 a 3 días a la semana)- EQUIVALENCIA A (1.375)")
print("3.- Ejercicio moderado (3 a 5 días a la semana)- EQUIVALENCIA A (1.55)")
print("4.- Deportista (6 -7 días a la semana)- EQUIVALENCIA A (1.725)")
print("5.- Atleta (entrenamientos mañana y tarde)- EQUIVALENCIA A (1.9 )")
print(" ")

eligio=input("Ingrese el numero:")

# Según lo que ingresó, código diferente
if eligio=="1":
    x=1.2
    Porcentaje = calcular_calorias_en_reposo(estatura,peso,edad,valor_genero)

    print(" *********************************************")
    print("Su TMB es: ", round(Porcentaje * x,2),"cal")

elif eligio=="2":
    x = 1.375 
    Porcentaje = calcular_calorias_en_reposo(estatura,peso,edad,valor_genero)

    print(" *********************************************")
    print("Su TMB es: ", round(Porcentaje * x,2),"cal")

elif eligio=="3":
    x = 1.55
    Porcentaje = calcular_calorias_en_reposo(estatura,peso,edad,valor_genero)

    print(" *********************************************")
    print("Su TMB es: ", round(Porcentaje * x,2),"cal")

elif eligio=="4":
    x = 1.725
    Porcentaje = calcular_calorias_en_reposo(estatura,peso,edad,valor_genero)

    print(" *********************************************")
    print("Su TMB es: ", round(Porcentaje * x,2),"cal")

elif eligio=="5":
    x = 1.9
    Porcentaje = calcular_calorias_en_reposo(estatura,peso,edad,valor_genero)

    print(" *********************************************")
    print("Su TMB es: ", round(Porcentaje * x,2),"cal")
   
else:
    print("Opción no válida")

