""" Definimos la funcion para Calcular  Porcentaje de Grasa Corporal """

from sre_constants import CALL


def calcular_IMC(estatura,peso):
    
    """Calculamos el indice de la masa corporal """

    return peso/ estatura**2

def calcular_porcentaje_grasa( Imc, edad, valor_genero):
    
    """Calculamos el  Porcentaje de Grasa Corporal """

    return (1.2*Imc)+(0.23*edad)-5.4-valor_genero



print(" *********************************************")
print("   Calcular  Porcentaje de Grasa Corporal     ")
print(" *********************************************")
peso = float(input("Escriba su peso en (Kg):  "))
print(" ")
estatura = float(input("Escriba su estatura en (m):  "))
print(" ")
edad = int(input("Escriba su edad en (años):  "))
print(" ")
valor_genero = float(input(" En caso de ser Masculino debe dijitar (10.8) y en caso de ser Femenino debe dijitar (0) : "))

"""Declaracion de los Parametros"""
Imc=calcular_IMC(estatura,peso)

Porcentaje = calcular_porcentaje_grasa(Imc,edad,valor_genero)

print("Su %GC es: ", round(Porcentaje,2),"%")

