# Part 1 of the Python Review lab.
s=0
def hello_world():
	print("hello world!")

def greet_by_name(name):
	print("hello "+ name)

def encode(x):
	return x*3953531
	
def decode(a):
	return a/encode(3953531)
	