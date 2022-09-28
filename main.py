def aleatorio():
  import random
  x= random.randint(1, 65535)
  sup=0
  print("Esse código gera números aleatórios de 1 até 65535,   tente acertar qual foi o escolhido.")
  while(x!=sup):
    sup=int(input("Insira sua suposição(Insira 0 para saber o   número gerado): "))
    if(sup==x):
      print("Você acertou, parabéns.")
    elif(sup==0):
      print("O número gerado é", x)
    elif(sup<x):
        print("O número escolhido é menor que o gerado, tente novamante.")
    else:
      print("O número escolhido é maior que o gerado, tente novamente.")

def grau2(a,b,c):
  d=b**2-(4*a*c)
  x1=(-b - d**(1/2))/(2*a)
  x2=(-b + d**(1/2))/(2*a)
  print("A primeira raiz é: {:.2f} e a segunda raiz é: {:.2f}".format(x1, x2))
