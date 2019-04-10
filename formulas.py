def suma (x,y):
    return x + y

def resta (x,y):
    return x - y

def multiplicacion (x,y):
    return x * y

def division (x,y):
    return x / y

def maximocomundivisor(x,y):
	resto = 0
	while(y>0):
		resto=y
		y=x%y
		x=resto
	return x

def max(x,y,z):
	if x>y and x>z:
		return x
	elif y>z:
		return y
	return z
