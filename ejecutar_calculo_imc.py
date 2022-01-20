
""" Definimos la funcion para calcular IMC """

def calcular_IMC(estatura,peso):
    
    """Calculamos el indice de la masa corporal """

    return peso /estatura **2

print(" ")
print("Calcular el índice de masa corporal de una persona")
print(" ")
peso = float(input("Escriba su peso en (Kg):  "))
print(" ")
estatura = float(input("Escriba su estatura en (m):  "))

"""Declaracion de los Parametros"""
Indice =calcular_IMC(estatura,peso)

""" Aqui nos va imprimir el Imc que lo hemos declarado como Indice"""
""" Tambien usamos round  para redondear a cuantos decimales"""
print("Su IMC es: ", round(Indice,2))
if Indice < 16:
    print ("Su estado es : Delgadez severa")
elif 16.00 <= Indice and Indice < 17:
    print ("Su estado es : Delgadez moderada")
elif 17.00 <= Indice and Indice < 18.50:
    print (" Su estado es : Delgadez aceptable")
elif 18.50 <= Indice and Indice < 25:
    print ("Su estado es : Peso Normal ")   
elif 25 <= Indice and Indice < 30:
    print ("Su estado es : Sobrepeso ")  
elif 30 <= Indice and Indice < 35:
    print ("Su estado es : Obesidad Tipo I ")  
elif 35 <= Indice and Indice < 40:
    print ("Su estado es : Obesidad Tipo II ")  
elif 40 <= Indice and Indice < 50:
    print ("Su estado es : Obesidad Tipo III o Morbida ")  
else: 
    print ("Su estado es : Obesidad Tipo IV o Extrema ")  

