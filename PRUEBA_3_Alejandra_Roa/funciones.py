#CREAR FUNCIONES PARA CADA OPCION DEL MENU 


#UNA FUNCION QUE GUARDE LOS REGISTROS DE LOS PUNTAJES DEL TORNEO Y SE PUEDA ACCEDER CON TXT#
#es para guardar tipos por avanzado 
##como 
#COMO NO ME ACUERDO COMO GUARDAR UN ARCHIVO DE TEXT EN UNA FUNCION LO DEJARE AQUI.
# def guardar_txt(filaname):
 #   with open(filaname,'w') as file_txt:
  #      file_txt.write('')


registro_total= []  #lista en forma de diccionar corchetes y luego diccionario 


#----ingresar los datos y guardalos en una lista o diccionario.


def  Registrar_puntajes_torneo():
    jugador = {}

    # Registrar ID del jugador
    id_string = input('Ingrese ID del jugador Ej: Mago: ')
    jugador['ID jugador'] = id_string

    # Registrar Nombre y apellido
    name = input('Ingrese Nombre y apellido: ')
    jugador['Nombre'] = name

    # Seleccionar tipo de juego y registrar el  puntaje
    while True:
        print('\nESCOGE (1-VALORANT, 2-FORNITE, 3-FIFA)')
        try:
            tipo_juego = int(input('Ingrese tipo de juego: '))
            if tipo_juego < 1 or tipo_juego > 3:
                print('Opción fuera de rango')
                continue
        except ValueError:
            print('Opción no válida, intente de nuevo')
            continue

        if tipo_juego == 1:
            print('Escogiste Valorant')
            ptje_obtenido = int(input('Ingresar puntaje obtenido: '))
            jugador['Valorant'] = ptje_obtenido
            break
        elif tipo_juego == 2:
            print('Escogiste FORNITE')
            ptje_obtenido = int(input('Ingresar puntaje obtenido: '))
            jugador['Fornite'] = ptje_obtenido
            break
        elif tipo_juego == 3:
            print('Escogiste FIFA')
            ptje_obtenido = int(input('Ingresar puntaje obtenido: '))
            jugador['FIFA'] = ptje_obtenido
            break

    # Seleccionar tipo de experiencia
    while True:
        print('Escoge tu nivel de experiencia 1-Principiante, 2-Avanzado, 3-Experto')
        try:
            tipo_exp = int(input('Ingrese tipo de experiencia: '))
            if tipo_exp < 1 or tipo_exp > 3:
                print('Opción fuera de rango')
                continue
        except ValueError:
            print('Opción no válida, intente de nuevo')
            continue

        if tipo_exp == 1:
            print('Escogiste Principiante')
            jugador['Tipo'] = 'Principiante'
            break
        elif tipo_exp == 2:
            print('Escogiste Avanzado')
            jugador['Tipo'] = 'Avanzado'
            break
        elif tipo_exp == 3:
            print('Escogiste Experto')
            jugador['Tipo'] = 'Experto'
            break

    # Agregar jugador al registro total
    registro_total.append(jugador)
    print('Registro exitoso.')   


    """Para registrar puntajes se requiere lo siguiente: Identificador de Jugador, Nombre y apellido del jugador, juego, puntaje obtenido. Por 
ejemplo, si el jugador compite en Fortnite y Fifa. Debe permitir seleccionar entre 1 de las 3 opciones e ingresar la cantidad de puntos 
obtenidos en esos dos juegos, también debe incluir su tipo (Principiante / Avanzado - Experto). Por lo tanto, un detalle de puntos del 
torneo podría verse registrado de la siguiente manera:
Id Jugador Nombre VALORANT FORNITE FIFA Tipo
Mago Luis Jimenez 0 125000 3500 Principiante """

#Funcion para mostrar Todos los puntajes 
def Listar_puntajes(id_string,name,tipo_juego,tipo_exp,ptje_obtenido):
    print('COdigo que muestre todos los puntajes registrados')  
    ###USAR UNA COLECCION LISTA O DICCIONARIO PARA ENCONTRAR TODOS LOS PUNTAJES
    #FOR RECORRE TODA LA LISTA
    #for i in len(jugador) :
        #AQUI SE BUSCA CON CORCHETES Y CON COMILLAS LA FILA CON EL CONTENIDO los {} SON LOS CORCHETES PLANOS
         #AQUI SE SUPONE QUE BUSCA EL ENCABEZADO O CLAVE DEL DICCIONARIO y luego los valores que estan en el diccionario.
         #print(f'Id jugador:'{'id_string'}|'Nombre:' {'id_string'}|'valorant:' {'ptje'}|'fornite' {'ptje_obtenido'}|'FIFA'{'ptje_obtenido'}|'Tipo'{'ptje_obtenido'}')
        #---Y poner :3 y eso para que se vea bonito
        #print('---AQUI SE SUPONE QUE BUSCA LA LLAVE DEL DICCIONARIO Y LOS VALORES Y LUEGO LO IMPRIME.')

         
def  Imprimir_por_Tipo():
    print('Imprimir s (Principiante Avanzado - Experto).')

###PODRIA HACERSE UNA OPCIN CON ENTER "" QUE IMPRIMA TODOS LOS TIPOS EN UN ARCHIVO TXT #
##Y OTRA OPCION QUE IMPRIMA O LISTE LOS TIPOS EN UN ARCHIVO TXT POR EJEMPLO  PRINCIPANTE.TXT , AVANZADO.TXT, EXPERTO.TXT.
    ##BUSCAR AVANZADO -PRINCIPIANTE O EXPERTO EN EL ARCHIVO E IMPRIMIR UN ARCHIVO TOTAL...
    print('Ingresa que planilla quieres descargar. 1PRINCIPIANTE 2.Avanzado 3.Experto')
    print('/n Si ingresa enter con el teclado se imprimen todos los tipos.')

    inputstring='.'


   # if inputstring=='':
       ##  filaname='Todos_los_jugares.txt'
      #   with open (filaname,'w',Indent=4) as file:
           #   for i in jugador:
               #    print('Id Jugador |Nombre |VALORANT| FORNITE| FIFA| Tipo')
                   # print('Buscar los encabezados del diccionario jugador y el valor ')
   # elif inputstring=='principiante':
    #     filaname='principiantes.txt'
      #   with open (filaname,'w',Indent=4) as file:
        #      for i in jugador:
    # print('Id Jugador |Nombre |VALORANT| FORNITE| FIFA| Tipo')
          #         # print('Buscar los encabezados del diccionario jugador  solo los que tengan principiante en el encabezado y el valor ')
         
          




