import psutil

try:
    for proc in psutil.process_iter():
        processName = proc.name()
        processID = proc.pid
        if processName=="notepad.exe":
            print("El bloc de notas esta en ejecucion")
        else:
            print(processName, ' ::: ', processID)
    print("Escribe el nombre del proceso que quieras terminar: ")
    proceso= int(input())
    for proc in psutil.process_iter():
        if proc.pid==proceso:
            print("El proceso ", proc.name(), " con PID ", proc.pid, " se ha terminado")
            proc.terminate()
except:
    print("Error en los procesos")