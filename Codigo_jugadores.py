import os
import time

##listas de los datos
nombres=[]
edades=[]
estaturas=[]

def imprimir_opciones(): #menu
    print("\n \n Jugadores de tenis")
    print("*" * 50)
    print("[C] Crear jugador")
    print("[A] Actualizar jugador")
    print("[B] Buscar jugador")
    print("[E] Eliminar jugador")
    print("[S] Salir")  
    print("\n ") 

    
def run():
    imprimir_opciones() #mostrar el menu

    comando = input()   #leer la opcion escogida
    comando = comando.upper() #hacer todas las etras mayusculas

    if comando == 'C':
        crear_jugador()
    elif comando == 'A':
        Actualizar_jugador()
    elif comando == 'B':
        Buscar_jugador()
    elif comando == 'E':
        Eliminar_jugador()
    elif comando == 'S':    
        os._exit(1) #si la eleccion es S salir
    else:
        print('Comando inválido') # mensaje de error
        time.sleep(1) #pausa para la ejecucion del codigo
        run()

def crear_jugador():#funcion de creacion de Jugadores

    print('CREACIÓN DE JUGADORES')
    print('*' * 50)
    nombre = obtener_nombre()
    nombres.append(nombre)
    
    #apellido = obtener_apellido()
    #apellidos.append(apellido)
    edad = obtener_edad()
    edades.append(edad)
    estatura = obtener_estatura()
    estaturas.append(estatura)
    run()
    
    
############# validaciones
def validar_nombre(nombre):
    if len(nombre) < 2 or len(nombre) > 10:
        raise ValueError(f'El nombre debe tener un máximo de 50 caracteres, tamaño actual:{len(nombre)}')
    if nombre==int:
        raise ValueError("El nombre debe tener solo letras")
    return True
        
#def validar_apellido(apellido):
    #if len(apellido) < 2 or len(apellido) > 10:
        #raise ValueError(f'El apellido debe tener un máximo de 50 caracteres, tamaño actual:{len(apellido)}')
    #return True
    
def validar_edad(edad):
    if edad < 0:
        raise ValueError(f'esa no es una edad valida')
    return True
    
def validar_estatura(estatura):
    if estatura < 150:
        raise ValueError(f'esa no es una altura valida')
    return True
#############################################################


def obtener_nombre():
    print("escriba el nombre: ")
    nombre= input()
    try:
        validar_nombre(nombre)
        return nombre
    except ValueError as err:
        print(err)
        obtener_nombre()
    
    
#def obtener_apellido():
    #print("escriba el apellido: ")
    #apellido= input()
    #try:
        #validar_apellido(apellido)
        #return apellido
    #except ValueError as err:
        #print(err)
        #obtener_apellido()
        
def obtener_edad():
    print("escriba la edad: ")
    edad= int(input())
    
    try:
        validar_edad(edad)
        return edad
    except ValueError as err:
        print(err)
        obtener_edad()

def obtener_estatura():
    print("escriba la estatura: ")
    estatura= int(input())
    try:
        validar_estatura(estatura)
        return estatura
    except ValueError as err:
        print(err)
        obtener_estatura()


def Actualizar_jugador():#funcion de ACTUALIZACION de jugadores
    print('ACTUALIZACION DE JUGADORES')
    print('*' * 50)
    posicion=Encontrar_jugador()
    print("nombre:",nombres[posicion])
    print("edad:",edades[posicion])
    print("estatura:",estaturas[posicion])
    print("que desea Actualizar?")
    print("[N] Nombre")
    print("[E] Edad")
    print("[A] Altura")
    print("[S] Salir")
    editar=input()
    editar=editar.upper()
    if editar == 'N':
        Editar_nombre(posicion)
    elif editar == 'E':
        Editar_edad(posicion)
    elif editar == 'A':
        Editar_estatura(posicion)
    elif editar == 'S':    
        os._exit(1) #si la eleccion es S salir
    else:
        print('Comando inválido') # mensaje de error
        time.sleep(2) #pausa para la ejecucion del codigo
        Actualizar_jugador()
    
    run()

def Encontrar_jugador():
    
    print("escriba el nombre de el jugador: ")
    nombre=input()
    posicion=nombres.index(f'{(nombre)}')

    return posicion 
    
def Editar_nombre(posicion):
    nombre = obtener_nombre()
    nombres[posicion]=nombre

def Editar_edad(posicion):
    edad = obtener_edad()
    edades[posicion]=edad
    
def Editar_estatura(posicion):
    estatura = obtener_estatura()
    estaturas[posicion]=estatura
    
def Buscar_jugador():
    
    for i in range(len(nombres)):
        print("\n")
        print("nombre:",nombres[i])
        print("edad:",edades[i])
        print("estatura:",estaturas[i])
        print("\n")
        
    posicion=Encontrar_jugador();
    print("nombre:",nombres[posicion])
    print("edad:",edades[posicion])
    print("estatura:",estaturas[posicion])
    time.sleep(3)
    run()
    
def Eliminar_jugador():
    
    print('ELIMININAR DE JUGADORES')
    print('*' * 50)
    posicion=Encontrar_jugador()
    print("nombre:",nombres[posicion])
    print("edad:",edades[posicion])
    print("estatura:",estaturas[posicion])
    time.sleep(3)
    
    print('Si desea borrar escriba si,en caso de querer cancelar escriba no')
    
    confirmacion=input()
    confirmacion=confirmacion.upper()
    
    if confirmacion == "SI":
        nombres.pop(posicion)
        edades.pop(posicion)
        estaturas.pop(posicion)
        print("eliminados con exito")
        time.sleep(2)
        run()
    elif confirmacion == "NO":
        run()
    else: 
        print("ese valor no es valido")
        time.sleep(3)
        Eliminar_jugador()
    
if __name__ == "_main_":
    run()