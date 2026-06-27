tareas=[]
def desplegras_menu():
    print("======MENU PRINCIPAL=====")
    print("1. Agregar tarea")
    print("2. Buscar tarea")
    print("3. Eliminar tarea")
    print("4. Actualizar Tarea")
    print("5. mostrar Tarea")
    print("6. Salir")
    print("=========================")

def seleccion_opcion():
    try:
        seleccion=int(input("Seleccione una opcion entre 1-6: "))
        if 0<seleccion<=6:
            return seleccion
        else:
            print("opcion no valida")
    except:
        print("Error: Debe ingresar un numero entre 1 a 6")

def validacion_descripcion(descripcion):
    return descripcion.strip() !=""

def validacion_prioridad(prioridad):
    try:
        dato=int(prioridad)
        return 0<dato<=10
    except ValueError:
        return False

def validacion_tiempo(tiempo):
    try:
        dato=float(tiempo)
        return 0<dato
    except ValueError:
        return False

def agregar_tarea(tareas):

    print("**** Agregar Tarea ****")

    descripcion=input("ingrese una descripcion de la tarea: ")
    if validacion_descripcion(descripcion) == False:
        print("Error: La descripcion de la tarea no puede estar en blanco")
        return
    
    prioridad=input("ingrese prioridad del 1 al 10: ")
    if validacion_prioridad(prioridad) == False:
        print("Error: La priodidad debe ser un numero entre 1 y 10 ")
        return
    
    tiempo=input("ingrese el tiempo estimado de la tarea (horas): ")
    if validacion_tiempo(tiempo) ==False:
        print("Error: El tiempo estimado debe ser mayor a 0")
        return
    
    tarea={"descripcion":descripcion,
           "prioridad":int(prioridad),
           "tiempo": float(tiempo),
           "estado":False
        }
    tareas.append(tarea)
    print("tarea agregada con exito")

def buscar_tarea(tareas,descripcion):
    for i,tarea in enumerate(tareas):
        if tarea["descripcion"].upper() == descripcion.upper():
            return i
    return -1

def actualizar_estado(tareas):
    for tarea in tareas:
        if tarea["prioridad"]>=5:
            tarea["estado"]=True
        else:
            tarea["estado"]==False

while True:
    desplegras_menu()
    seleccion=seleccion_opcion()
    if seleccion==1:
        agregar_tarea(tareas)
    
    elif seleccion==2:
        descripcion=input("ingrese la descripcion de la tarea a buscar: ").strip()
        if buscar_tarea(tareas,descripcion) !=-1:
            tarea=tareas[buscar_tarea(tareas,descripcion)]
            print(f"Tarea N°{buscar_tarea(tareas,descripcion)+1}: ")
            print(f"Descripcion: {tarea["descripcion"]}")
            print(f"Prioridad: {tarea["prioridad"]}")
            print(f"Tiempo estimado: {tarea["tiempo"]}")
            if tarea["estado"]==True:
                print("Estado: COMPLETADO")
            else:
                print("Estado: PENDIENTE")

    elif seleccion==3:
        descripcion=input("Ingrese la descripcion de la tarea a elimiar: ").strip()
        if buscar_tarea(tareas,descripcion)!=-1:
            tareas.pop(buscar_tarea(tareas,descripcion))
            print("Tarea eliminada con exito")
        else:
            print(f"La tarea {descripcion} no se encuentra registrada.")
    
    elif seleccion==4:
        actualizar_estado(tareas)
        print("se han actualizado los estados de las tareas.")
    
    elif seleccion==5:
        actualizar_estado(tareas)
        print("=== LISTAS DE TAREAS ===")
        for tarea in tareas:
            print(f"Descripcion: {tarea["descripcion"]}")
            print(f"Prioridad: {tarea["prioridad"]}")
            print(f"Tiempo estimado: {tarea["tiempo"]}")
            if tarea["estado"]==True:
                print("Estado: COMPLETADO")
            else:
                print("Estado: PENDIENTE")
            print("******************************************")
            
    elif seleccion==6:
        print("Gracias por usar el sistema. Vuelva pronto")
        break