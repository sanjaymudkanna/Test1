
def decor(func):
	def inner(name):
		if name=='Sunny':
			print("Hello Sunny Bad Morning")

		else:
			func(name)
	return inner

@decor
def wish(name):
	print("Hello",name,"Good Morning")

wish('John')

wish('Ravi')

wish('Sunny')

wish('sanju')
