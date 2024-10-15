import psutil

try:
    for proc in psutil.process_iter():
        processName = proc.name()
        processID = proc.pid
        blocNotas=False
        if processName=="notepad.exe":
            blocNotas=True
        else:
            print(processName, ' ::: ', processID)
    if blocNotas == True:
        print("El Bloc de Notas esta en ejecución")
    print("Escribe el nombre del proceso que quieras terminar: ")
    proceso= int(input())
    for proc in psutil.process_iter():
        if proc.pid==proceso:
            print("El proceso ", proc.name(), " con PID ", proc.pid, " se ha terminado")
            proc.terminate()
except:
    print("Error en los procesos")