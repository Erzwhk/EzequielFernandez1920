#Importar la clase "Usuario" al archivo de Funciones
from Clase_User import*

#Importar libreria random para generar enteros aleatorios
import random

#Función para validar el username:
def validar_user():
        VerUsuario = True
        largo = 31
        while VerUsuario or largo > 30:
            usuario = input("Ingrese nuevo username (solo letras minusculas, sin espacios y maximo 30 caracteres): ")
            largo = len(usuario)
            usuario1 = usuario.islower()
            usuario2 = usuario.isdigit()
            if " " in usuario:
                VerUsuario = True
            elif usuario1 == True or usuario2 == True:
                if verificar_username_existe(usuario) == False:
                    VerUsuario = False
                elif verificar_username_existe(usuario) == True:
                    print("Username existente")
                    VerUsuario = True
                else:
                    VerUsuario = True
            elif usuario1 == False:
                VerUsuario = True
            else:
                VerUsuario = True  
        return usuario

#Función para validar el nombre:
def validar_nombre():
        VerNombre = True
        while VerNombre:
            nombre = input("Indique el nombre completo (sin espacios): ")
            nombre1 = nombre.isalpha()
            if nombre1 == True:
                VerNombre = False
            elif nombre1 == False:
                VerNombre = True
            else:
                VerNombre = True
        return nombre

#Función para validar la edad:
def validar_edad():
        VerEdad = True
        edad2 = 4
        while VerEdad or edad2 < 5 or edad2 > 100:
            edad = input("Indique su edad (Entre 5 y 100 años): ")
            edad1 = edad.isdigit()
            if edad1 == True:
                edad2 = int(edad)
            if edad1 == True:
                VerEdad = False
            elif edad1 == False:
                VerEdad = True
            else:
                VerEdad = True
        return edad

#Función para validar el genero:
def validar_genero():
        VerGenero = True
        while VerGenero:
            genero = input("Indique su género, 1 para M o 2 para F: ")
            genero1 = genero.isdigit()
            if genero1 == True and genero == "1":
                genero = "M"
                VerGenero = False
            elif genero1 == True and genero == "2":
                genero = "F"
                VerGenero = False
            elif genero1 == False:
                VerGenero = True
            else:
                VerGenero = True
        return genero

#Funcion para verificar la existencia de un usuario
def verificar_username_existe(usuario_verificar):
    try:
        all_users = open('BaseDeDatos.txt', 'r').readlines()# Otra forma de acceder a un archivo
        for Usuario in all_users:
            usuario = Usuario[:-1].split(',') # [:-1] para quitar el salto de linea
            if usuario[0] == usuario_verificar:
                return True
        return False
    except FileNotFoundError:
        print('Todavia no se ha registrado ningun usuario')
        return False

#Funcion para buscar usuario en base de datos
def buscar_usuario(usuario_verificar):
    with open("BaseDeDatos.txt", "r") as bd:
        datos = bd.readlines()
    for dato in datos:
        usuario = dato[:-1].split(',') # [:-1] para quitar el salto de linea
        if usuario[0] == usuario_verificar:
            bd.close() 
            return Usuario(usuario[0], usuario[1], usuario[2], usuario[3])

#Registrar usuario en la base de datos:
def agregarUsuario(Usuario):
    archivo = open("BaseDeDatos.txt", "a")
    archivo.write(Usuario.string() + '\n')
    archivo.close() 
    return True

#Funcion para leer base de datos:
def leerBaseDeDatos():
    ListaDeUsuarios = []
    archivo = open("BaseDeDatos.txt", "r")
    for linea in archivo.readlines():
        listaDeValores = linea.split(",")
        ListaDeUsuarios.append(Usuario(listaDeValores[0],listaDeValores[1],listaDeValores[2],listaDeValores[3]))
        archivo.close()
    return ListaDeUsuarios
    
#Funcion para editar Usuario en la base de datos
def editarUsuarios(buscar_usuario, usuario_verificar):
    Objetos_User = []
    buscar = True
    while buscar:
        print("Estos sos sus datos actuales".center(50,"="))
        buscar_usuario.datos()
        print("".center(50,"="))
        info = input('''Indique una de las siguientes opciones:
1) Editar username
2) Editar nombre
3) Editar edad
4) Editar genero
5) Regresar al menu de inicio
''')
        if info == "1":
            for Usuario in leerBaseDeDatos():
                if Usuario.username == usuario_verificar:
                    Usuario.username = validar_user()
                    usuario_verificar = Usuario.username
                    Objetos_User.append(Usuario)
                else:
                    Objetos_User.append(Usuario)
            archivo = open("BaseDeDatos.txt", "w")
            for Usuario in Objetos_User:
                archivo.write(Usuario.string())
            archivo.close()
            Objetos_User.clear()
            buscar = True
        elif info == "2":
            for Usuario in leerBaseDeDatos():
                if Usuario.username == usuario_verificar:
                    Usuario.nombre = validar_nombre()
                    Objetos_User.append(Usuario)
                else:
                    Objetos_User.append(Usuario)
            archivo = open("BaseDeDatos.txt", "w")
            for Usuario in Objetos_User:
                archivo.write(Usuario.string())
            archivo.close()
            Objetos_User.clear()
            buscar = True
        elif info == "3":
            for Usuario in leerBaseDeDatos():
                if Usuario.username == usuario_verificar:
                    Usuario.edad = validar_edad()
                    Objetos_User.append(Usuario)
                else:
                    Objetos_User.append(Usuario)
            archivo = open("BaseDeDatos.txt", "w")
            for Usuario in Objetos_User:
                archivo.write(Usuario.string())
            archivo.close()
            Objetos_User.clear()
            buscar = True
        elif info == "4":
            for Usuario in leerBaseDeDatos():
                if Usuario.username == usuario_verificar:
                    Usuario.genero = validar_genero()
                    Objetos_User.append(Usuario)
                else:
                    Objetos_User.append(Usuario)
            archivo = open("BaseDeDatos.txt", "w")
            for Usuario in Objetos_User:
                archivo.write(Usuario.string())
            archivo.close()
            Objetos_User.clear()
            buscar = True
        elif info == "5":
            buscar = False
        else:
            print("Opción inválida")
            buscar = True
    return usuario_verificar

#Recorrer matriz:
def mostrar_tablero(tablero):
    for f in range(10):
        for c in range(10):
            print (tablero[f][c],end=' ')
        print()

#Funcion para validar posiciones contiguas de barcos:
def validar_botes(matriz, x, y):

    if matriz[x][y] != "O":
        return False

    if x > 0:
        if matriz[x-1][y] != "O":
            return False

    if x < 9:
        if matriz[x+1][y] != "O":
            return False

    if y > 0:
        if matriz[x][y-1] != "O":
            return False
            
    if y < 9:
        if matriz[x][y+1] != "O":
            return False

    return True

def crear_tablero(tablero):
    #Insertando Buque3:
    Barco3 = Buque3(3)#Buque3
    x = random.randint(0,7)
    y = random.randint(0,7)
    v = random.randint(0,1)#Horizontal o vertical
    tablero[x][y] = Barco3
    if x == 0:
        if v == 0:
            tablero[x][y+1] = Barco3
            tablero[x][y+2] = Barco3
        else:
            tablero[x+1][y] = Barco3
            tablero[x+2][y] = Barco3
    elif y == 0:
        if v == 0:
            tablero[x+1][y] = Barco3
            tablero[x+2][y] = Barco3
        else:
            tablero[x][y+1] = Barco3
            tablero[x][y+2] = Barco3
    else:
        if v == 0:
            tablero[x][y+1] = Barco3
            tablero[x][y+2] = Barco3
        else:
            tablero[x+1][y] = Barco3
            tablero[x+2][y] = Barco3

    #Insertando buque2
    Barco2 = Buque2(2)
    blue = True
    while blue:
        x = random.randint(0,7)
        y = random.randint(0,7)
        v = random.randint(0,1)#Horizontal o vertical
        if validar_botes(tablero, x, y) == True:
            if x == 0:
                if v == 0:
                    if validar_botes(tablero, x, y+1) == True:
                        tablero[x][y] = Barco2
                        tablero[x][y+1] = Barco2
                        blue = False
                    else:
                        blue = True
                elif v == 1:
                    if validar_botes(tablero, x+1, y) == True:
                        tablero[x][y] = Barco2
                        tablero[x+1][y] = Barco2
                        blue = False
                    else:
                        blue = True
            elif y == 0:
                if v == 0:
                    if validar_botes(tablero, x+1, y) == True:
                        tablero[x][y] = Barco2
                        tablero[x+1][y] = Barco2
                        blue = False
                    else:
                        blue = True
                elif v == 1:
                    if validar_botes(tablero, x, y+1) == True:
                        tablero[x][y] = Barco2
                        tablero[x][y+1] = Barco2
                        blue = False
                    else:
                        blue = True
            else:
                if v == 0:
                    if validar_botes(tablero, x, y+1) == True:
                        tablero[x][y] = Barco2
                        tablero[x][y+1] = Barco2
                        blue = False
                    else:
                        blue = True
                elif v == 1:
                    if validar_botes(tablero, x+1, y) == True:
                        tablero[x][y] = Barco2
                        tablero[x+1][y] = Barco2
                        blue = False
                    else:
                        blue = True
        elif validar_botes(tablero, x, y) == False:
            blue = True

    #Insertando submarinos:
    for i in range(0,4):
        Barco1 = Submarino(1)
        blue = True
        while blue:
            x = random.randint(0,7)
            y = random.randint(0,7)
            if validar_botes(tablero, x, y) == True:
                tablero[x][y] = Barco1
                blue = False
            elif validar_botes(tablero, x, y) == False:
                blue = True

    return tablero

#buscar puntos por genero en base de datos
def leerPuntosPorGenero(usuario_verificar):
    if buscar_usuario(usuario_verificar).genero == "M":                                 
        ar = open("puntosM.txt", "r")
        for linea in ar.readlines():
            listaDeValores = linea.split(",")
            puntosV = listaDeValores[0]
            puntosV = int(puntosV)
            ar.close()
            return puntosV

    elif buscar_usuario(usuario_verificar).genero == "F":   
        ar = open("puntosF.txt", "r")
        for linea in ar.readlines():
            listaDeValores = linea.split(",")
            puntosV = listaDeValores[0]
        puntosV = int(puntosV)
        ar.close()
        return puntosV

#actualizar puntos por genero en base de datos     
def escribirPuntosPorGenero(usuario_verificar, puntosV, puntos):
    if buscar_usuario(usuario_verificar).genero == "M": 
        archivo = open("puntosM.txt", "w")
        archivo.write(str(puntosV + puntos))
        archivo.close()
        return True

    elif buscar_usuario(usuario_verificar).genero == "F": 
        archivo = open("puntosF.txt", "w")
        archivo.write(str(puntosV + puntos))
        archivo.close()
        archivo.close()
        return True
    
#Leer historial de partidas en base de datos
def leerHistorial():
    listaDePartidas = []
    archivo = open("Historial.txt", "r")
    for linea in archivo.readlines():
        listaDeValores = linea.split(",")
        listaDePartidas.append(listaDeValores)
        archivo.close()
    return listaDePartidas

#Buscar TOP 10
def buscarTop10():
    listaDePartidas = []
    archivo = open("Top10.txt", "r")
    for linea in archivo.readlines():
        listaDeValores = linea.split(",")
        listaDePartidas.append(listaDeValores)
        archivo.close()
    return listaDePartidas
