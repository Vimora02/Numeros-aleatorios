import random
x= random.randint(1, 65535)
sup=0
print("Esse código gera números aleatórios de 1 até 65535, tente acertar qual foi o escolhido.")
while(x!=sup):
  sup=int(input("Insira sua suposição(Insira 0 para saber o número gerado): "))
  if(sup==x):
    print("Você acertou, parabéns.")
  elif(sup==0):
    print("O número gerado é", x)
  elif(sup<x):
      print("O número escolhido é menor que o gerado, tente novamante.")
  else:
      print("O número escolhido é maior que o gerado, tente novamente.")