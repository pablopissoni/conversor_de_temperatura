# Funcion de conversion de temperatura con dos parametros
def conversor():
    temp = input("Ingrese la temperatura: ")
    unidad = input("Que unidad es --> Centigrados (C) o Farhreinheit (F): ").upper()

    if unidad == "F" :
        respuesta = (int(temp) - 32) * 5/9
        print("La temperatura en C° es: ", respuesta)
    elif unidad == "C":
        respuesta = ( int(temp) * 1.8 ) + 32
        print("La temperatura en F° es: ", respuesta)
    else: 
        print("Ingrese valores validos")
        reiniciar()

#Primer llamado a la funcion
conversor()

#Funcion para reiniciar la conversion que acepta un parametro (Y) o (N) para volver a ejecutar CONVERSOR o para terminar la app
def reiniciar ():
    loop = input("Realizar otra convercion (Y) o (N) ?: ").upper()
    if loop == "Y" : 
        conversor()
        reiniciar()
    elif loop == "N":
        return
    else: 
        print("Coloque la letra correcta (Y) o (N): ")
        reiniciar(input().upper())
    
#Llamado a la funcion para reiniciar la conversion o no
reiniciar()

#----------------------------------------------------------------------
# Conversor de unidad de Farhreinhheit a Celcius

# temp = input("Ingrese la temperatura: ")
# print(int(temp))
# unidad = input("Que unidad es --> Centigrados (C) o Farhreinheit (F): ").upper()


# if int(temp) != int:
#     print("Ingrese valores numericos")