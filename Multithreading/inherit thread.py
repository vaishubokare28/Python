from threading import Thread

class MyThread(Thread):
    def run(self):
        print("This is MyThread");

t1=MyThread()
t1.start()