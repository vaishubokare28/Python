# Using join() in Multithreading 🧵
# The join() method ensures that the main program waits for a thread to complete before moving forward. It is essential when we want to ensure that all threads finish before proceeding with the rest of the program.

# Example 1: Using join() to Wait for Threads
# python
# Copy
# Edit
# import threading
# import time

# def print_numbers():
#     for i in range(5):
#         time.sleep(1)
#         print(f"Number: {i}")

# def print_letters():
#     for letter in "ABCDE":
#         time.sleep(1)
#         print(f"Letter: {letter}")

# # Creating threads
# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_letters)

# # Start the threads
# thread1.start()
# thread2.start()

# # Wait for both threads to finish
# thread1.join()
# thread2.join()

# print("Both threads finished execution!")
# 🔹 start() begins execution of the thread.
# 🔹 join() makes the main program wait until the thread completes.

# Output (order may vary due to threading)
# makefile
# Copy
# Edit
# Number: 0
# Letter: A
# Number: 1
# Letter: B
# Number: 2
# Letter: C
# Number: 3
# Letter: D
# Number: 4
# Letter: E
# Both threads finished execution!
# =====================

# Example 2: Using join(timeout)
# You can pass a timeout to join() to avoid waiting indefinitely.

# python

import threading
import time

def long_running_task():
    print("Task started...")
    time.sleep(5)
    print("Task finished!")

thread = threading.Thread(target=long_running_task)
thread.start()
# Wait for only 2 seconds
thread.join(timeout=2)


# Example 2: Using join(timeout)
# You can pass a timeout to join() to avoid waiting indefinitely.

# python

import threading
import time

def long_running_task():
    print("Task started...")
    time.sleep(5)
    print("Task finished!")

thread = threading.Thread(target=long_running_task)

thread.start()

# Wait for only 2 seconds
thread.join(timeout=2)


import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Number: {i}")

def print_letters():
    for letter in "ABCDE":
        time.sleep(1)
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


# print("Main program continues (even if thread is still running)...")
# 🔹 If the timeout expires before the thread finishes, the main program continues execution.

# When to Use join()?
# ✅ Ensures all threads finish before proceeding.
# ✅ Prevents race conditions when multiple threads modify shared data.
# ✅ Useful in applications where sequential execution is necessary.