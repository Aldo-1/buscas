import math
from utils.utils import *

class Buscas:

  def custoUniforme(self,matriz, inicio, fim):
    ##Iniciando os vetores de distancia, visitado e caminho
    distancia, visitado, caminho = iniciarVetores(matriz)

    ##Iniciando os vetores na posicao inicial com 0
    distancia[inicio] = 0
    caminho[inicio] = 0
    
    ##Criando esse vetor pois no futuro irei inverter o original
    novoVetorCaminho = []

    while(False in visitado):
    
      menorNumero = math.inf
      menorIndex = 0

      ##Calculando o menor numero e o menorIndice para pegar
      ##Suas respectivas arestas
      for i in range(0, len(matriz)):
        if(menorNumero > distancia[i] and not(visitado[i])):
          menorNumero = distancia[i]
          menorIndex = i

      
      ##Condicao para ver se matriz esta correta.
      if(len(matriz[menorIndex]) != len(matriz)):
        return 'matriz incorreta'

      

      ##Colocando os menores pesos no vetor de distancia e criando o caminho. 
      ##2
      for w in range(0, len(matriz[menorIndex])):
        pesoAresta = matriz[menorIndex][w]
        soma = distancia[menorIndex] + pesoAresta
        if(distancia[w] > soma and pesoAresta != 0):
          distancia[w] = soma
          caminho[w] = menorIndex
      visitado[menorIndex] = True
      
    
    ##Pegando o caminho
    caminhoCopy = pegarCaminho(caminho, novoVetorCaminho, fim)
    
    ##Retornando o caminho
    return 'Caminho final custo unirforme-> ' + caminhoCopy + ':' + str(distancia[fim])
    
  def gulosa(self,matriz,inicio, heuristica):
    ##Iniciando os vetores de distancia, visitado e caminho
    distancia, visitado,caminho = iniciarVetores(matriz)
    ##Iniciando os vetores na posicao inicial com 0
    distancia[inicio] = heuristica[inicio]

    ##achando o fim
    for i in range(0, len(heuristica)):
      if(heuristica[i] == 0):
        fim = i

    ##Iniciando os vetores na posicao inicial com 0
    caminho[inicio] = 0
    novoVetorCaminho = []

    while(False in visitado):
      
      menorNumero = math.inf
      menorIndex = 0
      heuristicaVertice = 0

      ##Calculando o menor numero e o menorIndice para pegar
      ##Suas respectivas arestas
      for i in range(0, len(matriz)):
        if(menorNumero > distancia[i] and not(visitado[i])):
          menorNumero = distancia[i]
          menorIndex = i

      caminho.append(menorIndex)

      ##Calculando o menor numero e o menorIndice para pegar
      ##Suas respectivas arestas
      if(len(matriz[menorIndex]) != len(matriz)):
        return 'matriz incorreta'

      ##Se ele pegar na distancia o menor index 0 , ja para.
      if(distancia[menorIndex] == 0): 
        novoVetorCaminho = pegarCaminho(caminho, novoVetorCaminho, fim)
        return 'Caminho final heuristica-> ' + novoVetorCaminho + ':' + str(distancia[fim])

      ##Achando o vertice para pegar sua heuristica e colocar no vetor
      ##De distancias
      for w in range(0, len(matriz[menorIndex])):
        if(matriz[menorIndex][w] != 0):
            heuristicaVertice = w
        if(distancia[w] > heuristica[heuristicaVertice] and matriz[menorIndex][w] != 0):
          distancia[w] = heuristica[heuristicaVertice]
          caminho[w] = menorIndex
      
      visitado[menorIndex] = True
    
  def a_asterisco(self,matriz, inicio, heuristica, fim):
    ##Iniciando os vetores de distancia, visitado e caminho
    distancia, visitado,caminho = iniciarVetores(matriz)
    ##Iniciando os vetores na posicao inicial com 0
    auxDistancia = []
    distancia[inicio] = 0 + heuristica[inicio]
    caminho[inicio] = 0
    for i in range(0, len(matriz)):
      auxDistancia.append(math.inf)

    ##Criei uma auxiliar para a distancia pois se nao criasse o vetor 
    ##Na segunda rodada ->
    ##Quando fosse verificar a soma novamente ele nao seria o Peso + a Helvetica 
    ##E sim seria o Peso + Helvetica + Helvetica, criei esse vetor para evitar isso.
    ##Armazendo nele como se fosse calculando o custo uniforme normal.
    ##E na distancia o fica o calculo do custo uniforme + a heuretica.
    auxDistancia[inicio] = 0

    ##Iniciando os vetores na posicao inicial com 0
    
    novoVetorCaminho = []

    while(False in visitado):
      
      menorNumero = math.inf
      menorIndex = 0
      heuristicaVertice = 0

      ##Calculando o menor numero e o menorIndice para pegar
      ##Suas respectivas arestas
      for i in range(0, len(matriz)):
        if(menorNumero > distancia[i] and not(visitado[i])):
          menorNumero = distancia[i]
          menorIndex = i

      caminho.append(menorIndex)

      ##Calculando o menor numero e o menorIndice para pegar
      ##Suas respectivas arestas
      if(len(matriz[menorIndex]) != len(matriz)):
        return 'matriz incorreta'

      ##Se ele pegar na distancia o menor index 0 , ja para.
      if(distancia[menorIndex] == 0): 
        novoVetorCaminho = pegarCaminho(caminho, novoVetorCaminho, fim)
        return 'Caminho final heuristica-> ' + novoVetorCaminho + ':' + str(distancia[fim])

      ##Achando o vertice para pegar sua heuristica e colocar no vetor
      ##De distancias
      for w in range(0, len(matriz[menorIndex])):
        if(matriz[menorIndex][w] != 0):
            heuristicaVertice = w
        soma = auxDistancia[menorIndex] + matriz[menorIndex][w]
        if(distancia[w] >  soma + heuristica[heuristicaVertice] and matriz[menorIndex][w] != 0):
          distancia[w] = soma + heuristica[heuristicaVertice]
          auxDistancia[w] = soma
          caminho[w] = menorIndex
      
      visitado[menorIndex] = True

      novoVetorCaminho = pegarCaminho(caminho, novoVetorCaminho, fim)
      return 'Caminho final custo unirforme-> ' + novoVetorCaminho + ':' + str(distancia[fim])

