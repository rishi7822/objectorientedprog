#thread pool executor
#Multi-threading: Multiple threads can exist within one process where:

#Each thread contains its own register set and local variables (stored in stack).
#All threads of a process share global variables (stored in heap) and the program code


import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
    print(f"sleeping for{seconds}seconds")
    time.sleep(seconds)
    return seconds

def main():

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
 
def poolingDemo():
   with ThreadPoolExecutor() as executor:
    #   future1 = executor.submit(func, 3)
    #   print(future1.result())
    #   future2 = executor.submit(func, 2)
    #   print(future2.result())
    #   future3 = executor.submit(func, 4)
    #   print(future3.result())
    l = [3,5,1,2]
    results= executor.map(func,l)
    for result in results:
      print(results)

poolingDemo()

#map function