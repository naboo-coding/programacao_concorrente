import threading
import time

#variaveis
T = 8
M = 200_000
count = 0
sem = threading.Semaphore(1)


def somar(valor):
    return valor +1 

def counting(): 
    global count 
    for i in range(M):
        sem.acquire()
        try:
            tmp = count
            tmp = somar(tmp)
            count = tmp
        finally:
            sem.release()


if __name__ == "__main__":
    threads = [threading.Thread(target=counting) for _ in range(T)]
    inicio = time.time()
    
    for t in threads:
            t.start()

    for t in threads:
            t.join()
            tempo = time.time()  - inicio

print(f"valor esperado: {T * M} | valor obtido: {count} | tempo: {tempo:.3f} segundos")