##Programa que dado um valor ele retornara o numero minimo de cedulas a sacar
valores = [200,100,50,20,10,5,2]
valor = float(input("Digite o valor a sacar: \n"))
i = 0
contador = 0
while valor>=2:
  if valor >= valores[i]:
    valor-=valores[i]
    contador+=1
  else: i+=1
print("Você vai sacar",contador,"notas")
