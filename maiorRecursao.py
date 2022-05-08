##AQUI ESTA UM EXEMPLO DE ALGORITIMO QUE TRAZ COMO RETORNO O MENOR ELEMENTO DE UMA LISTA, SEJA DO TIPO QUE FOR A LISTA
##NESTE EXEMPLO UTILIZEI DE RECURSAO EM CAUDA

def maior(lista):
  head = lista[0]
  tail = lista[1:len(lista)]
  if lista == []:
    return []
  if lista == [lista[0]]:
    return [head]
  if head < tail[0]:
    return maior(tail)
  else:
    return maior([head] + tail[1:len(tail)])
