import math

def removeReplicateItems(vetor, newVector):
  for i in vetor: 
    if i not in newVector:
      newVector.append(i)
  return newVector

def iniciarVetores(matriz):
  distancia = []
  visitado = []
  caminho = []
  for i in range(0, len(matriz)):
    distancia.append(math.inf)
    visitado.append(False)
    caminho.append('')
  return distancia, visitado, caminho

def pegarCaminho(caminho, novoVetorCaminho, fim):
  aux = caminho[fim]
  for i in range(0, len(caminho)):
    novoVetorCaminho.append(aux)
    aux = int(caminho[aux])
  
  reverse = novoVetorCaminho[::-1]
  removeDuplicateArray = [] 
  removeDuplicateArray = removeReplicateItems(reverse, removeDuplicateArray)
  removeDuplicateArray.append(fim)
  caminhoCopy = '-'.join(str(e) for e in removeDuplicateArray)
   
  return caminhoCopy  