import psutil
continuar=True
while continuar==True:
    try:
        blocNotas = False
        #Se recorren todos los procesos, obteniendo su nombre, pid, uso de cpu y uso de memoria
        for proc in psutil.process_iter():
            processName = proc.name()
            processID = proc.pid
            cpu= proc.cpu_percent(interval=0.1)
            memoria= proc.memory_percent()
            #En cada vuelta del bucle se comprueba si el bloc de notas está en ejecucion
            if processName=="notepad.exe":
                blocNotas=True
                idBlocNotas= proc.pid
            else:
                #Se muestran todos los datos, en el caso de la RAM se redondea ya que por defecto se muestran muchos decimales
                print(processName, ' PID: ', processID, "Porcentaje de CPU: ", cpu, "%", "Porcentaje de memoria RAM:", round(memoria, 2), "%")
        if blocNotas == True:
            print("El Bloc de Notas esta en ejecución, su PID es: ", idBlocNotas)
        #Parte 2, se pide al usuario un PID, si ese proceso está activo se finaliza
        print("Escribe el nombre del proceso que quieras terminar: ")
        proceso= int(input())
        for proc in psutil.process_iter():
            if proc.pid==proceso:
                print("El proceso ", proc.name(), " con PID ", proc.pid, " se ha terminado")
                proc.terminate()
        #Se pregunta al usuario si quiere continuar en el programa
        print("¿Quieres continuar en el programa? Escribe 's' para continuar")
        respuesta= input()
        if(respuesta!='s'):
            continuar=False
            print("Has salido del programa.")
    except:
        print("Ha ocurrido un error")