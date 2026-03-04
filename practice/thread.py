from threading import *
def show():
    print("this is a child thread")
t = Thread(target=show)
t.start()
t.join()
print("this is a Parent thread")    