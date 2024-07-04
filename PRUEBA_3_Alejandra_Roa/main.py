from funciones import *



#FUNCION MENU 
def menu():
    menupal=True
    #MOSTRAR MENU PRINCIPAL CON UN CICLO WHILE

    while menupal:
        print('eShirlitos')
        print('1-Registrar puntajes torneo')
        print('2-Listar los todos puntajes')
        print('3-Imprimir por Tipo')
        print('4-Salir del programa')
        op=0
        try:
            op=int(input('Ingrese opcion valida---> '))
            if op<1 or op>5:
                print('Opcion fuera de rango')
        except:
            print('Opcion no valida intente de nuevo')       
            
    #OPCIONES DEL MENU
        if op==1:
            print('Registrar puntajes torneo') 
            #HAY QUE INGRESAR LOS DATOS ACA 
            Registrar_puntajes_torneo()
        elif op==2:
            print('Listar todos los puntajes') 
            listar=Listar_puntajes()
        elif op==3:  
            print('Imprimir por Tipo')
            imprimir=Imprimir_por_Tipo()
        elif op==4: #Salir 
            print('Saliendo del programa....')
            menupal=False


    #.1 Registrar puntajes torneo
    #2. Listar los todos puntajes
    #3. Imprimir por Tipo
    #4. Salir del programa






#PARA HACER ESTE ARCHIVO EL PRINCIPAL Y QUE LA FUNCION MENU SEA EL PROGRAMA PRINCIPAL
    
if __name__== "__main__":
    menu()



