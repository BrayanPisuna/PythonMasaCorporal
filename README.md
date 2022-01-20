# PythonMasaCorporal
Proyecto de Programación en Python  Calculadora de índices corporales
Proyecto de Programación en Python 
Calculadora de índices corporales
El objetivo general de este proyecto es crear una aplicación que permite hacer cálculos de distintos índices 
corporales como el índice de masa corporal y la tasa metabólica basal. En el desarrollo de esta aplicación pondrás en 
práctica los conceptos estudiados.
En el desarrollo de este proyecto mostrarás tu capacidad para:
1. Crear funciones.
2. Llamar funciones con parámetros.
3. Llamar funciones desde otras funciones (composición de funciones).
4. Crear y usar un módulo.
5. Probar las funciones de un módulo.
6. Construir interfaces de usuario basadas en consola.
En esta aplicación se calcula los distintos índices corporales que permite conocer algunos factores sobre el estado 
de salud. Por ejemplo, nos pueden decir si hay algún tipo de sobrepeso o si se consumiendomás calorías al día de
las que se debe. Lossiguientesson losíndices corporales que calcularemos en este proyecto:
Índice de masa corporal - IMC
El índice de masa corporal, también conocido como IMC, es un método que se utiliza para estimar si el peso de 
una persona es adecuado con respecto a su altura. El IMC se calcula como la razón entre el peso en kilogramos y 
el cuadrado de la altura en metros de la persona:
IMC=
peso(kg)
(altura(m))
!
La tabla que se muestra a continuación permite usar el IMC calculado para establecer si el peso de una persona 
se encuentra dentro de un rango normal o si por el contrario la persona padece de sobrepeso o delgadez.
Valor IMC Categoría
<16 Delgadez severa
16.00-16.99 Delgadez moderada
17.00-18.49 Delgadez aceptable
18.5-24.99 Peso normal
25.00-29.99 Sobrepeso
30.00-34.99 Obesidad tipo I
35.00-39.99 Obesidad tipo II
40.00-49.99 Obesidad tipo III o mórbida
>50 Obesidad tipo IV o extrema
Descripción de la aplicación
Objetivo general
Objetivos específicos
Porcentaje de grasa corporal - %GC
El porcentaje de grasa corporal es una medida (porcentual) que permite establecer si una persona tiene un nivel 
adecuado o excesivo de grasa en su cuerpo. Este se calcula a partir del IMC, la edad y el género de la persona:
%GC = 1.2 ∗ IMC + 0.23 ∗ edad(años) − 5.4 − valor_genero
Donde valor_genero es un valor que depende del género de la persona: en caso de ser masculino, el valor es 10.8. 
De lo contrario el valor es 0.
La siguiente tabla muestra los rangos recomendados de índice de grasa corporal según la edad y el género de las 
personas. Los porcentajes que se salen de estos rangos pueden ser causados por obesidad o por personas que se 
consideran deportistas de alto rendimiento.
Rango de edad Rango de %GC 
recomendado en 
hombres
Rango de %GC 
recomendado en 
mujeres
20 – 29 años 11% - 20% 16% - 28%
30 – 39 años 12% - 21% 17% - 29%
40 – 49 años 14% - 23% 18% - 30%
50 – 59 años 15% - 24% 19% - 31%
Tasa metabólica basal - TMB
La tasa metabólica basal es el mínimo de calorías necesarias para vivir, es decir el número de calorías que un ser 
humano quema al día estando en reposo. Estas calorías son utilizadas por el cuerpo para llevar a cabo funciones 
básicas como: bombear la sangre, hacer digestión, respirar, mantener el cerebro funcionando, etc. La TMB se 
calcula a través de la siguiente fórmula:
TMB = G10 ∗ peso (kg)H + G6.25 ∗ altura(cm)H − G5 ∗ edad(años)H + valor_genero
Donde valor_genero es un valor que depende del género de la persona: en caso de ser masculino, el valor es 5, 
mientas que es -161 en caso de ser femenino.
Tasa metabólica basal según actividad física
Dado que las personas realizamos actividad física en el día, el consumo de calorías diarias (el cual denominaremos 
TMB"#$%& %'"'_)%*%#") es mayor al TMB. Para poder calcularlo es necesario multiplicar el TMB por un valor que 
depende de la actividad física semanal que realiza cada persona:
TMB"#$%& %'"'_)%*%#" = TMB ∗ valor_actividad
Donde valor_actividad es un valor que depende de la actividad física que lleva a cabo la persona semanalmente y 
toma los siguientes valores:
• 1.2: poco o ningún ejercicio
• 1.375: ejercicio ligero (1 a 3 días a la semana)
• 1.55: ejercicio moderado (3 a 5 días a la semana)
• 1.72: deportista (6 -7 días a la semana)
• 1.9: atleta (entrenamientos mañana y tarde)
Cálculo de las calorías diarias para adelgazar
En general, si las personas desean adelgazar deben reducir las calorías que ingieren a diario y/o deben aumentar 
el gasto calórico haciendo más deporte. Si se escoge la primera opción, se recomienda que las personas ingieran 
a diario entre un 15% a 20% menos calorías de las que arroja la TMB. Lo anterior sugiere que una persona que 
desee adelgazar debe consumir entre 80% y 85% de las calorías que representa la TMB.
1. Crea una nueva carpeta para el proyecto y Usando Spyder, crea un nuevo archivo con el nombre 
“calculadora_indices.py”. En este archivo tú vas a construir un módulo en el que vas a hacer varios cálculos 
sobre los indicadores que presentamos anteriormente. En cada caso te indicaremos qué valores entran como 
parámetro las funciones y qué resultado deben arrojar.
2. Define e implementa funciones en tu nuevo archivo de acuerdo con la siguiente información:
