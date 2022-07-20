import os, re
def Menu():
    print("Bienvenidos a nuestra agenda telefonica")
    print("Seleccione un opcion:")
    print("\t 1- agregar un registro a la agenda \n")
    print("\t 2- Listar contenido de la agenda \n")
    print("\t 3- exit \n")



def validar_mail(email):
    # funcion para validar el mail recibe como parametro el mail a controlar

    # se necesita una expresion regular para la comparacion de caracteres
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
 
    # con la libreria re y el metodo fullmatch() se realiza la comparacion
    # retornando un boolean de acuerdo con el resultado
    if(re.fullmatch(regex, email)):
        return True
 
    else:
        return False


def id_nuevo(ruta):
    
    # funcion creada para generar un autoincremental del ID
    with open(ruta, "rb") as file:

        # va al final del archivo con el metodo seek() y retrocedemos 2 posiciones
        file.seek(-2, os.SEEK_END)
        while file.read(1) != b'\n':
            # mientras no sea un salto de linea traemos el ultimo registro
            file.seek(-2, os.SEEK_CUR) 
        ultima = file.readline()
        #print(ultima)
        # separa el Id del resto con la funcion findall() de re y sumamos 1 para retornar le nuevo id
        numbers = [int(s) for s in re.findall(r'-?\d+\.?\d*', str(ultima))]
        return numbers[0] + 1

def Grabar():

    # establecemos la ruta del archivo csv
    ruta = (os.path.dirname(os.path.abspath(__file__))) + "\MyAgenda.csv"
    # comprobamos la existencia del archivo
    if os.path.isfile(ruta):
        
        print("************Ingresar Nuevo registro*********** \n")
        
        # se crea lista para solicitar los campos
        lista = ("Nombre", "Apellido", "E-mail")

        # se solicita el id nuevo a la funcion
        # se le asigna a la lista datos
        datos = [str(id_nuevo(ruta))]
        print("Nuevo Id: ", datos[0])
        
        # se inicia el bucle while para la lista
        # (Aclaracion: no se usa for para poder retroceder a voluntad en el bucle)
        i = 0
        while i < len(lista):
            # se añaden elementos a la lista
            datos.append(";")
            datos.append(input(lista[i] + ": "))
            # manejo de errores, si los datos no corresponden
            try:
                if lista[i] == "Nombre" or lista[i] == "Apellido":
                    
                    # verifica si el dato es una letra
                    if datos[-1].isalpha():
                        datos[-1] = datos[-1].capitalize() # primer letra en mayuscula
                        
                    else:
                        print(f"ingrese un {lista[i]} valido")
    
                        raise Exception # salta al manejo del error

                if lista[i] == 'E-mail':
                    # valida el email
                    if validar_mail(datos[-1]):

                        datos.append("\n") # agrega el salto de linea para completar el array
                        
                        # abre el archivo para grabar, con la variable de entorno with
                        with open(ruta, "a") as f:
                            # ciclo de grabado
                            for dato in datos:
                                f.write(dato)
                        print("Registro agregado con éxito, presione enter para continuar...\n")
                        input() # crea una pausa de aviso, antes de lanzar el menu
                    else:
                        
                        print("ingrese un mail valido")
                        
                        
                        raise Exception
            except Exception:
                datos.pop() # elimina el dato incorrecto
                datos.pop() # elimina el ";"
                i -= 1
            i += 1
        
        print (Listar())
        
    else:
        print('Error: el archivo no existe....\n')
        




def Listar():
    ruta = (os.path.dirname(os.path.abspath(__file__))) + "\MyAgenda.csv"
    if os.path.isfile(ruta):
        with open(ruta) as f: #abre archivo
            titulos = ["ID", "Nombre", "Apellido", "Email"] # crea una lista para el titulo
            
            for i in f.readlines(): # comienza el ciclo para leer lineas del reg.
                linea = i # introduce la linea a una variable para poder manipularla
                linea = linea.split(";") # separa los elementos del registro creando una lista
                
                if linea[0] == 'ï»¿Id': # pregunta por el inicio del archivo
                    print("\n") 
                    print("="*50) # ========
                    print(f'{titulos[0]:3} |{titulos[1]:8} |{titulos[2]:8} |{titulos[3]:20}') # crea el titulo con espacios
                    print("-"*50) # delimitador del titulo
                    
                else:
                    # carga los registros con el mismo formato del titulo, elimina el ultimo caractere de salto de linea
                    print(f'{linea[0]:3} |{linea[1]:8} |{linea[2]:8} |{linea[3][:-1]:20}') 
                    
            print("\n\n")
Listar()
