import threading
import time
from threading import Thread

def sleep(i):
    print("thread %i will sleep"% i)
    time.sleep(5)
    print("thread is awake")

for i in range(10):
    th = Thread(target = sleep, args = (i, ))
    th.start()
    print("curr threads = %i "% threading.active_count())