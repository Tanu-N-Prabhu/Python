from threading import *
import threading


def new():
    """
    This is a test method to call threading 
    """
    for x in range(6):
    	print("child executing..", current_thread().getName())


t1 = Thread(target=new)
t1.start()
t1.join()
print("done", current_thread().getName())


# class for threading
class A(threading.Thread):
	def run(self):
		for x in range(6):
			print("child executing..", current_thread().getName())


objA = A()
objA.start()
objA.join()
print("control returned to main ", current_thread().getName())


class ex():
	def B(self):
		lst = [5,2,7,'good', 9, 'bad']
		for x in lst:
			print("child printing ", x)


objEx = ex()
t1 = Thread(target=objEx.B)
t1.start()
t1.join()
print("done")


