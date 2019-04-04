def maximoComunDivisor(a,b):
	resto = 0
	while(b>0):
		resto=b
		b=a%b
		a=resto
	return a
