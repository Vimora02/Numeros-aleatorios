def grau2(a,b,c):
  d=b**2-(4*a*c)
  x1=(-b - d**(1/2))/(2*a)
  x2=(-b + d**(1/2))/(2*a)
  print("A primeira raiz é: {:.2f} e a segunda raiz é: {:.2f}".format(x1, x2))
