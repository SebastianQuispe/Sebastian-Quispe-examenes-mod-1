nombre= "Sebastian"
salario= 500
edad= "21"
compania= "Frio Global"
print(type(nombre),type(salario),type(edad),type(compania))


if int(edad) > 30 :
    print ("Usted tiene un bono de 10% en el mes de diciembre")
else :
    print ("Usted tiene un bono del 5% en el mes diciembre")

bono= salario*0.05
bono_final= pow(salario,2) + bono
print(bono_final)