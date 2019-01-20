'''
Alji Utils
'''
import time

def millis():
	return round(time.time() * 1000)

def stringy(*args):
	return ' '.join([str(s) for s in args])

def printDict(d, level=0):
    indent = '\t'*level
    for k, v in d.items():
        if isinstance(v, dict):
            print(indent, k, ":{")
            printDict(v, level=level+1)
            print(indent, "}")
        else:
            print(indent, k, ":", v)
