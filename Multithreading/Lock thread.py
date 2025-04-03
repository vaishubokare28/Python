# Example 2: Multithreading with Locks (Thread Synchronization)
# When multiple threads access a shared resource, race conditions can occur.
#  We use threading.Lock() to prevent data corruption.
import threading
counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(10):
        with lock:  # Ensures only one thread modifies 'counter' at a time
            counter += 1
# Creating threads
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print(f"Final Counter Value: {counter}")
# 🔹 Using lock.acquire() and lock.release() manually is possible, but with lock: is safer.