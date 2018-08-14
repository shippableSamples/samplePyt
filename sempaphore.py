import threading
import time
sem = threading.Semaphore()

def fun1():
    for num in range(1,20):
        sem.acquire()
        print(1)
        sem.release()
        time.sleep(0.25)

def fun2():
    for num in range(1,20):
        sem.acquire()
        print(3)
        sem.release()
        time.sleep(0.25)

t = threading.Thread(target = fun1)
t.start()
t2 = threading.Thread(target = fun2)
t2.start()
