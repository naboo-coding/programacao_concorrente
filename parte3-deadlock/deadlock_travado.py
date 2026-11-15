import threading
import time

# LOCK_A, LOCK_B = locks distintos
# Thread 1:
# adquirir(LOCK_A)
# dormir(50ms) // aumenta a chance do deadlock
# adquirir(LOCK_B)
# imprimir "T1 concluiu"
# liberar(LOCK_B)
# liberar(LOCK_A)
# Thread 2:
# adquirir(LOCK_B)
# dormir(50ms)
# adquirir(LOCK_A)
# imprimir "T2 concluiu"
# liberar(LOCK_A)
# liberar(LOCK_B)

LOCK_A = threading.Lock() 
LOCK_B = threading.Lock()

def thread1():
    LOCK_A.acquire()
    print("thread 1 pegou A")
    time.sleep(0.05)
    print("thread 1 tentando pegar B")
    LOCK_B.acquire()
    print("thread 1 pegou B")
    print("T1 concluiu")
    LOCK_B.release()
    LOCK_A.release()

def thread2():
    LOCK_B.acquire()
    print("thread 2 pegou B") 
    time.sleep(0.05)
    print ("thread 2 tentando pegar A")
    LOCK_A.acquire()
    print ("thread 2 pegou A")
    print("T2 concluiu")
    LOCK_A.release()
    LOCK_B.release()

t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

t1.start()
t2.start()

t1.join()
t2.join()

print("Programa concluiu")