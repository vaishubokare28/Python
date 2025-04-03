# import threading

# def print_numbers():
#     for i in range(5):
#         print(f"Number: {i}")

# def print_letters():
#     for letter in "ABCDE":
#         print(f"Letter: {letter}")

# # Creating threads
# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_letters)

# # Starting threads
# thread1.start()
# thread2.start()

# # Wait for both threads to finish
# thread1.join()
# thread2.join()

# print("Threads finished execution!")
# # 🔹 start() begins execution of the thread.
# # 🔹 join() ensures the main thread waits for other threads to finish.