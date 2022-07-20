import Utiles #as U

Utiles.Menu()


while True:
    Opcion = (input("Seleccione una opción: "))

    if Opcion == "1":
       Utiles.Grabar()
    elif Opcion == "2":
        Utiles.Listar()
    elif Opcion == "3":
        break
    else:
        Utiles.Error()    
    Utiles.Menu()
    
