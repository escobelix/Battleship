import numpy as np
import random
import constantes as ct

def tabla():

    tablero = np.full((10,10), ' ')
    valores_y = np.arange(10,0,-1).reshape(-1,1)

    tablero = np.hstack((valores_y, tablero))

    valores_x = np.arange(0,11)
    tablero = np.vstack((tablero,valores_x))

    return tablero



def disparar_player(tablero_maquina, tablero_player_disparo):
    try: 
        x = int(input('Tu turno de atacar\nSeleccione coordenada en X: '))
        y = int(input('Seleccione coordenada en Y: '))
        fila = -y-1
        columna = x
        if (1 <= x <= 10) and (1 <= y <= 10):
            if tablero_maquina[fila,columna] == 'O':
                tablero_player_disparo[fila,columna] = 'X'
                tablero_maquina[fila,columna] = 'X'
                print('\tTABLERO PLAYER DISPARO')
                print(tablero_player_disparo)
                
                
                disparar_player(tablero_maquina, tablero_player_disparo)
                
            elif tablero_player_disparo[fila,columna] == 'X' or tablero_player_disparo[fila,columna] == '*':
                print('Neeeerd!!')
                
            else:
                tablero_maquina[fila,columna] ='*'
                tablero_player_disparo[fila,columna] = '*'
            
                print('\tTABLERO PLAYER DISPARO')
                print(tablero_player_disparo)
        
        else:
            print('Coordenadas fuera de rango')
            disparar_player(tablero_maquina, tablero_player_disparo)
    except:
        print("El caracter es WRONG")
        disparar_player(tablero_maquina, tablero_player_disparo)
            

    
    

def disparar_maquina(tablero_player, tablero_maquina_disparo):
    fila = np.random.randint(10)
    columna = np.random.randint(1,11)
    if tablero_player[fila,columna] == 'O':
        tablero_player[fila,columna] = 'X' 
        tablero_maquina_disparo[fila,columna] = 'X'   
        disparar_maquina(tablero_player, tablero_maquina_disparo)
        
    elif tablero_maquina_disparo[fila,columna] == 'X' or tablero_maquina_disparo[fila,columna] == '*':
        print('Neeeerd!!')
        print('Tu disparo es repetido. Intentalo de nuevo\n')
        disparar_maquina(tablero_player, tablero_maquina_disparo)
        
    else:
        tablero_player[fila,columna] = '*'
        tablero_maquina_disparo[fila,columna] = '*'
        print('\tTABLERO PLAYER')
        print(tablero_player)
    print('La máquina ha atacado')
    

# FUNCION PARA CREAR UNO A UNO LOS BARCOS ALEATORIAMENTE
def crear_barco_aleatoriamente(eslora,tablero):
    while True:
    # Elijo randomly mi orientación
        orientacion = random.choice(ct.direccion)
        # print(orientacion)
        # Creamos randomly la posicion inicial de mi barco
        
        # print(posicionInicial)
        fila = np.random.randint(10)
        columna = np.random.randint(1,11)
        # Recogemos las posiciones desde la posicion inicial hasta su respectiva posicion final teniendo en cuenta la longitud
        coordenadas_N = tablero[fila:fila - eslora:-1, columna]
        coordenadas_S = tablero[fila:fila + eslora, columna]
        coordenadas_E = tablero[fila, columna:columna + eslora]
        coordenadas_W = tablero[fila, columna:columna - eslora:-1]
        # Comprobamos que sean validas
        if orientacion == 'N' and 0 <= fila - eslora < 10 and 'O' not in coordenadas_N:
            tablero[fila:fila - eslora:-1, columna] = 'O'
            break
        elif orientacion == 'S' and 0 <= fila + eslora < 10 and 'O' not in coordenadas_S:
            tablero[fila:fila + eslora, columna] = 'O'
            break
        elif orientacion == 'E' and 1 <= columna + eslora < 11 and 'O' not in coordenadas_E:
            tablero[fila, columna: columna + eslora] = 'O'
            break
        elif orientacion == 'W' and 1 <= columna - eslora < 11 and 'O' not in coordenadas_W:
            tablero[fila, columna: columna - eslora:-1] = 'O'
            break
        # No cumple con las dimensiones del tablero, o hay un barco ahi
        # Probamos con otra coordenada
        else:
            continue
    return tablero



def cuenta_vidas(tablero_maquina, tablero_player):
    if 'O' not in tablero_maquina or 'O' not in tablero_player:
        print('Fin del juego')
        return False

    return True


# FUNCION PARA CREAR TODOS LOS BARCOS
def crear_barcos(tablero):
    for eslora in ct.tamaños:
        
        crear_barco_aleatoriamente(eslora,tablero)
        

def crear_barcos_manualmente(tablero):
    for eslora in ct.tamaños:
        
        crear_barco_jugador(eslora,tablero)


# FUNCION PARA CREAR UNO A UNO LOS BARCOS MANUAL
def crear_barco_jugador(eslora,tablero):
    while True:
        print(tablero)
        # Creamos randomly la posicion inicial de mi barc0
        print('Creamos un barco de eslora: ', eslora)
        try:
            x = int(input("Introduce coordeanda en X entre 1 y 10: "))
            y = int(input("Introduce coordenada en Y entre 1 y 10: "))
        except:
            print('Error!!')
            continue
        fila = -y-1
        columna = x
        if (1 <= x <= 10) and (1 <= y <= 10):
        # Elijo randomly mi orientación
            orientacion = input('Introduce la orientacion querida(N,S,E,W): ').upper()
            
            if orientacion in ct.direccion:
                print(orientacion)
                # Recogemos las posiciones desde la posicion inicial hasta su respectiva posicion final teniendo en cuenta la longitud
                coordenadas_N = tablero[fila:fila - eslora:-1, columna]
                coordenadas_S = tablero[fila:fila + eslora, columna]
                coordenadas_E = tablero[fila, columna:columna + eslora]
                coordenadas_W = tablero[fila, columna:columna - eslora:-1]
                # Comprobamos que sean validas
                if orientacion == 'N' and -1 > fila - eslora >= -12 and 'O' not in coordenadas_N:
                    tablero[fila:fila - eslora:-1, columna] = 'O'
                    break
                elif orientacion == 'S' and -1 >= fila + eslora >= -11 and 'O' not in coordenadas_S:
                    tablero[fila:fila + eslora, columna] = 'O'
                    break
                elif orientacion == 'E' and 1 <= columna + eslora <= 11 and 'O' not in coordenadas_E:
                    tablero[fila, columna: columna + eslora] = 'O'
                    break
                elif orientacion == 'W' and 0 <= columna - eslora < 11 and 'O' not in coordenadas_W:
                    tablero[fila, columna: columna - eslora:-1] = 'O'
                    break
                # No cumple con las dimensiones del tablero, o hay un barco ahi
                # Probamos con otra coordenada
                else:
                    print('Ya hay un barco en esa posición o está fuera de rango, pruebe una posición u orientación distintas')
                    continue
            else:
                print('Orientación no válida')
                continue
        else:
            print('Coordenda fuera de rango')
            continue
    return tablero


def opciones(tablero_player):
    print('''Seleccione 1 para poner los barcos de forma aleatoria
Seleccione 2 para poner los barcos de forma manual''')
    
    opcion = int(input('Seleccione opcion: '))
    if opcion == 1:
        crear_barcos(tablero_player)
    elif opcion == 2:
        crear_barcos_manualmente(tablero_player)

    else:
        print('Código no válido')
        opciones(tablero_player)
    

def inicializar(tablero_player, tablero_maquina):
    # FUNCION INICIALIZAR TABLERO

    print("BIENVENIDO AL HUNDIR LA FLOTA\n\n")
    print(''' Instrucciones de juego:
    1. Juegas contra la máquina
    2. Coloca tus barcos: puedes colocarlos de forma manual o aleatoria, según el modo que elijas. 
       La máquina coloca los barcos de forma aleatoria.
       Los barcos pueden estar juntos (sin agua entre ellos)
    3. Funciona por turnos. En cada turno se dispara una vez. Si se acierta en un barco se vuelve a disparar.
       Si se falla y se impacta en agua, cambia el turno.
    4. Simbología: Los barcos están representados por 'O', el agua por espacios en blanco, barco dado por 'X' e impacto fallado por '*'
    4. Gana el primero que hunde los barcos del contrincante.
        EMPECEMOS!
    ''')
    opciones(tablero_player)
    print('\tTABLERO JUGADOR')
    print(tablero_player)
    crear_barcos(tablero_maquina)
