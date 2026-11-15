import threading
import time

# Regra global: sempre adquirir LOCK_A antes de LOCK_B, em TODAS as threads.
# Thread 1 e Thread 2:
# adquirir(LOCK_A)
# adquirir(LOCK_B) // secao critica
# liberar(LOCK_B)
# liberar(LOCK_A)

LOCK_A = threading.Lock()
LOCK_B = threading.Lock()

def thread1():
    LOCK_A.acquire()
    print ("thread 1 pegou A")
    time.sleep(0.05)
    print ("thread 1 tentando pegar B")
    LOCK_B.acquire()
    print ("thread 1 pegou B")
    print("T1 concluiu")
    LOCK_B.release()
    LOCK_A.release()


def thread2():
    LOCK_A.acquire()
    print ("thread 2 pegou A")
    time.sleep(0.05)
    print ("thread 2 tentando pegar B")
    LOCK_B.acquire()
    print ("thread 2 pegou B")
    print("T2 concluiu")
    LOCK_B.release()
    LOCK_A.release()


t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

t1.start()
t2.start()

t1.join()
t2.join()

print("Programa concluiu")