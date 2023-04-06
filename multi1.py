#Multi-threading: Multiple threads can exist within one process where:

#Each thread contains its own register set and local variables (stored in stack).
#All threads of a process share global variables (stored in heap) and the program code


import threading
import time

def func(seconds):
    print(f"sleeping for{seconds}seconds")
    time.sleep(seconds)

time1= time.perf_counter()

# func(4)
# func(2)
# func(1)
#normal code

#same code for threading

t1= threading.Thread(target=func, args=[4])
t2= threading.Thread(target=func, args=[2])
t3= threading.Thread(target=func, args=[1])

t1.start()
t2.start()
t3.start()

time2 = time.perf_counter()
print(time2-time1)
