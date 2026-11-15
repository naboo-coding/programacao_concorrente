import threading
import time

#variveis
T = 8
M = 200000
threads = []
count = 0

def counting():
    global count
    for i in range(M):
        count += 1

inicio_thread = time.time()

for i in range(T):
    thread = threading.Thread(target=counting)
    threads.append(thread)
    thread.start()


fim_thread = time.time()

print(f"Contador: {count}")
print(f"Tempo em que executou: {inicio_thread - fim_thread}")