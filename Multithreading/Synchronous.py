import threading
import time
counter1=0
counter2=0
lock=threading.Lock()

def print_numbers():
    global counter1
    for i in range(5):
        with lock:
          print(f"Number: {i}")

def print_letters():
    global counter2
    for letter in "ABCDE":
        with lock:
           print(f"Letter: {letter}")

# Creating threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

# print("Both threads finished execution!")
# 🔹 start() begins execution of the thread.
# 🔹 join() makes the main program wait until the thread completes.

