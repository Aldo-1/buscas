from modules.buscas import Buscas

##Para mudar o fim da gulosa é preciso alterar o heuristicaVector
##Para colocar um novo local de para basta alterar a posição do 0
##Pois gulosa vai ate o vertice que tem a heuristica 0

def init(matriz, heuristicaVector):
  while(True):
    resposta = int(input('Escolha o tipo da busca que deseja usar no grafo:\n'+ 
    '1)Custo Uniforme\n'+
    '2)Gulosa\n'+
    '3)A*\n'+
    '4)Acabar programa\n'))
    if(resposta != 4):
      inicio = int(input('Digite o inicio: '))
      if(resposta != 2):
        fim = int(input('Digite o fim: '))
    if(resposta == 1):
      print(buscas.custoUniforme(matriz, inicio, fim))
    elif(resposta == 2):
      print(buscas.gulosa(matriz, inicio, heuristicaVector))
    elif(resposta == 3):
      print(buscas.a_asterisco(matriz,inicio ,heuristicaVector, fim))
    elif(resposta == 4):
      break
##Para testar em outros grafos basta colocar aqui , esse ja esta par teste
matriz = [
  [0, 4, 2, 0 ],
  [4, 0, 1, 0 ],
  [2, 1, 0, 3 ],
  [0, 0, 3, 0 ],
]

heuristicaVector = [
  50,40,20,0
]

buscas = Buscas()

init(matriz,heuristicaVector)

