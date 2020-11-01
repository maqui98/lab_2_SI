import numpy as np
from colorama import init
from colorama import Fore, Back, Style
init()

import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

negro = 1
blanco = 2
'''

COLORAMA 

Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL

'''

def IMPRIME_TABLERO(matriz, lista):
    
    print("")
    #clear()
    print("")

    if(len(matriz) == 6):

        print("┌───────────────────────────────────┐")

        for i in range (0,6):
            print("|", end ="")
            for j in range (0,6):

                if (matriz[i][j] == 1):
                    print("| ",Fore.BLUE +  str(matriz[i][j]) + Fore.RESET , end = " |")
                elif(matriz[i][j] == 2):
                    print("| ", Fore.RED +  str(matriz[i][j]) + Fore.RESET, end = " |")
                else:
                    print("| ", Fore.WHITE + str(matriz[i][j]) + Fore.RESET, end = " |")

            print("")
            if(i == 5):
                print("└───────────────────────────────────┘")
            else:
                print("├───────────────────────────────────┤")
    
    else:

        print("┌───────────────────────────────────────────────┐")

        for i in range (0,8):
            print("|", end ="")
            for j in range (0,8):

                if matriz[i][j] == 1:
                    print("| ",Fore.BLUE +  str(matriz[i][j]) + Fore.RESET , end = " |")
                elif(matriz[i][j] == 2):
                    print("| ", Fore.RED +  str(matriz[i][j]) + Fore.RESET, end = " |")
                else:
                    print("| ", Fore.WHITE + str(matriz[i][j]) + Fore.RESET, end = " |")

            print("")
            if(i == 7):
                print("└───────────────────────────────────────────────┘")
            else:
                print("├───────────────────────────────────────────────┤")

    

   

def verificador(matriz, Color_ficha_propia, color_ficha_enemiga, pos_ficha_x, pos_ficha_y, direccion, flag): #verifica para una ficha, todos sus posibles movimientos permitidos

    largo_matriz = matriz.shape[0]

    dirx = 0
    diry = 0

    valor = []
    vacio = []

    if(direccion == 1):   #arriba

        #print("arriba")
        dirx = 0
        diry = -1

    elif(direccion == 2): #diagonal derecha superior

        #print("diagonal derecha superior")
        dirx = 1
        diry = -1

    elif(direccion == 3): #derecha
        #print("derecha")
        dirx = 1
        diry = 0

    elif(direccion == 4): #diagonal derecha inferior
        #print("diagonal derecha inferior")
        dirx = 1
        diry = 1

    elif(direccion == 5): #abajo
        #print("abajo")
        dirx = 0
        diry = 1

    elif(direccion == 6): #diagonal izquierda inferior
        #print("diagonal izquierda inferior")
        dirx = -1
        diry = 1

    elif(direccion == 7): #izquierda 
        #print("izquierda")
        dirx = -1
        diry = 0

    elif(direccion == 8): #diagonal izquierda superior
        #print("diagonal izquierda superior")
        dirx = -1
        diry = -1


    if(pos_ficha_x+dirx < largo_matriz and pos_ficha_y+diry < largo_matriz):   #si not sobrepasa el límite de la matriz

        if(matriz[pos_ficha_x+dirx][pos_ficha_y+diry] == color_ficha_enemiga):  #hay una ficha enemiga adelante

            flag = 1
            valor = verificador(matriz, Color_ficha_propia, color_ficha_enemiga, pos_ficha_x+dirx, pos_ficha_y+diry, direccion, flag)

        elif(matriz[pos_ficha_x+dirx][pos_ficha_y+diry] == 0 and flag == 1): # no hay ficha y pasó por lo menos 1 vez por una ficha enemiga

            matriz[pos_ficha_x+dirx][pos_ficha_y+diry] == Color_ficha_propia

            valor.append(pos_ficha_x+dirx)
            valor.append(pos_ficha_y+diry)        
            return valor
            
        else: # pasó una ficha aliada, o está vacío sin haber pasado por una ficha enemiga



            return valor

    return valor #obligatorio

def main():
    
    lista = []

    matriz_facil =np.array([
    [0,0,0,0,0,0],
    [0,0,0,1,0,0],
    [0,0,1,2,2,0],
    [0,0,2,1,2,0],
    [0,0,2,0,0,0],
    [0,0,0,0,0,0]])

    matriz_normal_dificil =np.array([
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 2, 0, 0, 0],
    [0, 0, 0, 2, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]])

    wolo_ubicacion=np.where(matriz_facil==1) #busca el numero 

    #print(wololo)

    wolo_x=wolo_ubicacion[1]
    wolo_y=wolo_ubicacion[0]
    print(wolo_x,"x",wolo_y,"y")

    print(wolo_x[0])
    print(wolo_x[1])

    lista = []

    for j in range( 0, len(wolo_x)): 

        for i in range (1,9):

            coordenada = verificador(matriz_facil, negro, blanco, wolo_x[j], wolo_y[j], i, 0) # devuelve 0 en todo 

            if(coordenada != []):
                lista.append(coordenada)

    print(lista)


#IMPRIME TABLERO

    IMPRIME_TABLERO(matriz_facil, lista)






















if __name__ == "__main__":

    main()


'''

lista = [[0]*10]*10
idea gráfica de la matriz inicializada tablero

elige una posible posicion destino
2,4  

aki
print (matriz_facil)
print(" " )
print(matriz_normal_dificil)
wololo=np.where(matriz_normal_dificil==1) #busca el numero 
print(wololo)
wolo_x=wololo[1]
wolo_y=wololo[0]
print(wolo_x,"x",wolo_y,"y")
hasta aki 






'''