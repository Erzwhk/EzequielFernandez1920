import Funciones
from Clase_User import *
import random

resp = True
validar = True
a = -1
Usuarios = []
Nombres = []
Edades = []
Generos = []
Barcos = []
Objetos_User = []

#Top 10
print("".center(50,"="))
print('''TOP 10'''.center(50,"="))
print("".center(50,"="))
Partidas = Funciones.leerHistorial()
Partidas.sort(reverse = True, key = lambda partida: partida[1])
archivo = open("Top10.txt", "w")
if len(Partidas) >= 9:
    for x in range(0,9):
        archivo.write(("{},{},{}".format(Partidas[x][0], Partidas[x][1], Partidas[x][2])))
    archivo.close()

elif len(Partidas) < 9:
    for x in range(len(Partidas)):
        archivo.write(("{},{},{}".format(Partidas[x][0], Partidas[x][1], Partidas[x][2])))
    archivo.close()

elif len(Partidas) == 0:
    print("No se ha jugado ninguna partida")
        
Top10 = Funciones.buscarTop10()
for x in range(len(Top10)):
    print("{}/{}/{}".format(Top10[x][0], Top10[x][1], Top10[x][2]))
print("".center(50,"="))

#Comienzo del módulo de usuario:
resp = True
while resp:
    menu = input('''Indique una de las siguientes opciones:
1) Registrar nuevo usuario
2) Iniciar sesión
3) Estadísticas
''')
    if menu == "1":
        user = Funciones.validar_user()
        Funciones.agregarUsuario(Usuario(user, Funciones.validar_nombre(), Funciones.validar_edad(), Funciones.validar_genero()))
        print("".center(50,"="))
        Funciones.buscar_usuario(user).datos()
        print("".center(50,"="))

    if menu == "2":
        inicio = True
        while inicio:
            usuario_verificar = input("Ingrese 1 para introducir su username o 2 para regresar: ")
            if usuario_verificar == '1':
                usuario_verificar = input('Ingrese su username: ')
                if Funciones.verificar_username_existe(usuario_verificar) == True:
                    print("".center(50,"="))
                    print('''Inicio de sesión exitoso'''.center(50,"="))
                    print("".center(50,"="))
                    inicio = True
                    while inicio:
                        menu2 = input('''Indique una de las siguientes opciones:
1) Editar datos
2) Nuevo juego
3) Ver datos
4) Cerrar sesion
''')      
                        if menu2 == "1":
                            usuario_verificar = Funciones.editarUsuarios(Funciones.buscar_usuario(usuario_verificar), usuario_verificar)                            
                            inicio = True 

                        elif menu2 == "2":#Comienzo modulo2

                            Barcos = []
                            Barco3 = Buque3(3)
                            Barco2 = Buque2(2)
                            Barco1 = Submarino(1)
                            Barcos.append(Barco3)
                            Barcos.append(Barco3)
                            Barcos.append(Barco3)
                            Barcos.append(Barco2)
                            Barcos.append(Barco2)
                            Barcos.append(Barco1)
                            Barcos.append(Barco1)
                            Barcos.append(Barco1)
                            Barcos.append(Barco1)

                            tablero = [["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],
                            ["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"],["O","O","O","O","O","O","O","O","O","O"]]
                            
                            print("".center(50,"="))
                            print('''PARTIDA INICIADA'''.center(50,"="))
                            print("".center(50,"="))
                            Funciones.crear_tablero(tablero)
                            disparos_realizados = []
                            puntos = 0
                            puntosM = 0
                            puntosF = 0
                            disparos = 0
                            disparos_repetidos = 0

                            juego = True
                            while juego:
                                print("-------------------")
                                Funciones.mostrar_tablero(tablero)
                                x = input("Indique la fila entre 0 y 9: ")
                                y = input("Indique la columna entre 0 y 9: ")
                                
                                if x.isdigit() and y.isdigit() == True:
                                    xi = int(x)
                                    yi = int(y)

                                    if xi >= 0 and xi <= 9 and yi >= 0 and yi <= 9:

                                        if [x,y] in disparos_realizados:
                                            print("Disparo ya realizado")
                                            disparos_repetidos = disparos_repetidos + 1
                                            juego = True

                                        elif tablero[xi][yi] == "O":
                                            tablero[xi][yi] = "X"
                                            print("Disparo errado")
                                            disparos = disparos + 1
                                            disparos_realizados.append([x,y])
                                            if puntos > 1:
                                                puntos = puntos - 2
                                                juego = True
                                            elif puntos == 1:
                                                puntos = puntos - 1
                                                juego = True
                                            elif puntos == 0:
                                                juego = True

                                        elif tablero[xi][yi] != "O":
                                            if tablero[xi][yi].largo == 3:
                                                if len(Barcos) != 1:
                                                    print("Disparo acertado")
                                                    Barco3.catalogar()
                                                    tablero[xi][yi] = "F"
                                                    puntos = puntos + 10
                                                    disparos = disparos + 1
                                                    disparos_realizados.append([x,y])
                                                    Barcos.remove(Barco3)
                                                    juego = True
                                                elif len(Barcos) == 1:
                                                    print("Disparo acertado")
                                                    Barco1.catalogar()
                                                    tablero[xi][yi] = "F"
                                                    puntos = puntos + 10
                                                    disparos = disparos + 1
                                                    disparos_realizados.append([x,y])
                                                    juego = False

                                            elif tablero[xi][yi].largo == 2:
                                                if len(Barcos) != 1:
                                                    print("Disparo acertado")
                                                    Barco2.catalogar()
                                                    tablero[xi][yi] = "F"
                                                    puntos = puntos + 10
                                                    disparos = disparos + 1
                                                    disparos_realizados.append([x,y])
                                                    Barcos.remove(Barco2)
                                                    juego = True
                                                elif len(Barcos) == 1:
                                                    print("Disparo acertado")
                                                    Barco1.catalogar()
                                                    tablero[xi][yi] = "F"
                                                    puntos = puntos + 10
                                                    disparos = disparos + 1
                                                    disparos_realizados.append([x,y])
                                                    juego = False

                                            elif tablero[xi][yi].largo == 1:
                                                if len(Barcos) != 1:
                                                    print("Disparo acertado")
                                                    Barco1.catalogar()
                                                    tablero[xi][yi] = "F"
                                                    puntos = puntos + 10
                                                    disparos = disparos + 1
                                                    disparos_realizados.append([x,y])
                                                    Barcos.remove(Barco1)
                                                    juego = True
                                                elif len(Barcos) == 1:
                                                    print("Disparo acertado")
                                                    Barco1.catalogar()
                                                    tablero[xi][yi] = "F"
                                                    puntos = puntos + 10
                                                    disparos = disparos + 1
                                                    disparos_realizados.append([x,y])
                                                    juego = False
                                    
                                    else:
                                        print("Disparo fuera de rango")
                                        juego = True

                                else:
                                    print("Disparo invalido")

                            #Culmino la partida
                            if disparos == 9:
                                print("".center(50,"="))
                                print('''¿Eres un Robot? lo que acabas de hacer es poco probable ....'''.center(50,"="))
                                print("".center(50,"="))
                            
                            elif disparos < 45:
                                print("".center(50,"="))
                                print('''Excelente Estrategia'''.center(50,"="))
                                print("".center(50,"="))

                            elif disparos >= 45 and disparos <= 70:
                                print("".center(50,"="))
                                print('''Buena Estrategia; pero hay que mejorar'''.center(50,"="))
                                print("".center(50,"="))
                            
                            elif disparos > 70:
                                print("".center(50,"="))
                                print('''Considérese Perdedor, tiene que mejorar notablemente'''.center(50,"="))
                                print("".center(50,"="))

                            #Historial de juegos:
                            archivo = open("Historial.txt", "a")
                            archivo.write(("{},{},{}".format(usuario_verificar, puntos, disparos)) + '\n')
                            archivo.close()
                            
                            #Recolectar puntos por genero
                            puntosV = Funciones.leerPuntosPorGenero(usuario_verificar)
                            Funciones.escribirPuntosPorGenero(usuario_verificar, puntosV, puntos)

                            #Datos finales
                            print("Username: ",usuario_verificar)
                            print("Cantidad de disparos: ",disparos)
                            print("Puntaje total: ",puntos)
                            print("Disparos repetidos: ",disparos_repetidos)
                            Funciones.mostrar_tablero(tablero)

                        elif menu2 == "3":
                            print("".center(50,"="))
                            Funciones.buscar_usuario(usuario_verificar).datos()
                            print("".center(50,"="))

                        elif menu2 == "4":
                            inicio = False

                if Funciones.verificar_username_existe(usuario_verificar) == False:
                    print("Username no está registardo")
                    inicio = True

            elif usuario_verificar == "2":
                inicio = False
            else:
                inicio = True

    elif menu == "3":#Comienzo modulo
        #Mostrar rango de edades
        edades1 = 0
        edades2 = 0
        edades3 = 0
        edades4 = 0
        print("".center(50,"="))
        print('''RANGO DE EDADES'''.center(50,"="))
        print("".center(50,"="))
        for Usuario in Funciones.leerBaseDeDatos():
            if Usuario.edad <= "18":
                edades1 = edades1 + 1
            elif Usuario.edad >= "19" and Usuario.edad <= "45":
                edades2 = edades2 + 1
            elif Usuario.edad >= "46" and Usuario.edad <= "60":
                edades3 = edades3 + 1
            elif Usuario.edad >= "61" and Usuario.edad <= "100":
                edades4 = edades4 + 1
        print("Jugadores entre [5-18] años: {}".format(edades1))
        print("Jugadores entre [19-45] años: {}".format(edades2))
        print("Jugadores entre [46-60] años: {}".format(edades3))
        print("Jugadores entre [61-100] años: {}".format(edades4))

        #Mostrar puntos por genero
        print("".center(50,"="))
        print('''PUNTOS POR GENERO'''.center(50,"="))
        print("".center(50,"="))
        ar = open("puntosM.txt", "r")
        for linea in ar.readlines():
            listaDeValores = linea.split(",")
            puntosV = listaDeValores[0]
        puntosV = int(puntosV)
        ar.close()
        print("Puntos totales de hombres: {}".format(puntosV))
        ar = open("puntosF.txt", "r")
        for linea in ar.readlines():
            listaDeValores = linea.split(",")
            puntosV = listaDeValores[0]
        puntosV = int(puntosV)
        ar.close()
        print("Puntos totales de mujeres: {}".format(puntosV))

        #Mostrar promedios de disparos para ganar
        print("".center(50,"="))
        print('''PROMEDIO DE DISPAROS PARA GANAR'''.center(50,"="))
        print("".center(50,"="))
        cantidad_disparos = []
        disparosPromedio = 0
        historial = Funciones.leerHistorial()
        if len(historial) != 0:
            for x in range(len(historial)):
                cantidad_disparos.append(historial[x][2])
            for x in range(len(cantidad_disparos)):
                disparosPromedio = disparosPromedio + int(cantidad_disparos[x])
            disparosPromedio = round(disparosPromedio / len(cantidad_disparos))
            print(disparosPromedio)
        elif len(historial) == 0:
            print("No se ha jugado ninguna partida")

    else:
        resp = True
       
    while a != "1" or a != "0":
        i = input("Ingrese 1 para regresar al menu principal o 0 para salir: ")
        if i == "1":
            resp = True
            break                                                           
        elif i == "0":
            resp = False
            break
        else:
            print("Opción no válida")