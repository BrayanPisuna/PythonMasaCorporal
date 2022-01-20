# Leemos lo que ingresa el usuario
print("Ingrese segun el numero segun la Actividad Fisica que Realiza ")
print(" ")
print("1.- Poco o Ningún ejercicio ")
print("2.- Ejercicio ligero (1 a 3 días a la semana)")
print("3.- Ejercicio moderado (3 a 5 días a la semana)")
print("4.- Deportista (6 -7 días a la semana)")
print("5.- Atleta (entrenamientos mañana y tarde)")
print(" ")

eligio=input("Ingrese el numero:")

# Según lo que ingresó, código diferente
if eligio=="1":
    x=1.2
    print("Listamos otras herramientas")
elif eligio=="2":
    x = 1.375 
    print(" ")
elif eligio=="3":
    x = 1.55
    print("Creo que hace frío")
elif eligio=="4":
    x = 1.72
    print("otra opción")
elif eligio=="5":
    x = 1.9
    print("otra opción")
else:
    print("Opción no válida")
