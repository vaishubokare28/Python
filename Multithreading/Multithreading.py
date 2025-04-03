'''Multithreading tithreading in Python refers to the concept of executing multiple threads 
(smaller units of a process) concurrently within a single program. Each thread runs a part of the code, 
which can help improve the performance of a program, especially when dealing with I/O-bound tasks (like file operations, 
network requests, etc.).

Thread: A thread is a sequence of instructions that can be executed independently. Python provides the threading module, which allows you to work with threads.'''
# Why Use Multithreading in Python?
# I/O-bound tasks: For tasks that spend a lot of time waiting (like reading files, network requests, or database queries), multithreading can help maximize efficiency since while one thread is waiting for data, another thread can do some work.

# Simulating concurrency: Even if threads aren't truly running in parallel, multithreading can help simulate concurrent behavior and can lead to a better user experience for tasks like handling multiple user inputs or processing multiple files at once.

# summary:
# Multithreading
# life cycle of Multithreading
# synchronization
# sleep and join

# interview questions
# 1)what is multithreading
# 2)why we use multithreading?
# 3)Explain life cycle methods of multithreading with example?
# 4)what is join() and sleep() ?
# 5)what is synchronization?
# 6)why we use join () method?

from threading import Thread

class Job:
    def run(self):
        print("All is well")
        
obj = Job()
t1 = Thread(target=obj.run)
t1.start()

t2 = Thread(target=obj.run)
t2.start()

