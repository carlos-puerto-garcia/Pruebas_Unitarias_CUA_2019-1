def primo (numero):
    valor = range(2,numero)
    contador = 0
    for n in valor:
      if numero % n == 0:
        contador +=1
        print("divisor:", n)
    if contador > 0 :
        return False
    else:
        return True
