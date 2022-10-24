import threading
import time
import random

semaforo = threading.Semaphore(3)

def atenderCliente(id_client):

    semaforo.acquire()

    print("Cliente {}".format(id_client) + " está sendo atendido.")
    time.sleep(random.randint(3, 10))
    print("Finalizado: Cliente {}".format(id_client))

    semaforo.release()

if __name__=="__main__":

    threads =  []
    for i in range(1, 31):
        t = threading.Thread(target=atenderCliente, args=(i, ))
        threads.append(t)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()