import threading
import time


def task():
    print("Thread going to sleep")
    time.sleep(3)                           #Thread is now in waiting time.
    print("Thread woke up")

object = threading.Thread(target=task)
object.start()