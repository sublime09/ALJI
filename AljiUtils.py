'''
Alji Utils
'''
import time

def millis():
	return round(time.time() * 1000)

def stringy(*args):
	return ' '.join([str(s) for s in args])