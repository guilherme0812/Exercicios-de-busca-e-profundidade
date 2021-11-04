mD = {
0: 'F-0',
1: 'MO-1',
2: 'JU-2',
3: 'P-3',
4: 'N-4',
5: 'CG-5',
6: 'JP-6',
7: 'A-7',
8: 'CA-8',
9: 'JP-9',
10: 'R-10',
11: 'MA-11'}

grafo = [ [2, 1], # vizinhos do noh 0
	 [5, 4, 0],  # vizinhos do no 1
	 [3, 0], #vizinhos do noh 2
	 [7, 5, 2], #vizinhos do noh 3
	 [6, 1], #vizinhos do noh 4
	 [8, 6, 3, 1], #vizinhos do noh 5
	 [10, 5, 4], #vizinhos do noh 6
	 [11, 3], #vizinhos do noh 7
	 [11, 10, 5], #vizinhos do noh 8
	 [10, 5, 4], #vizinhos do noh 9
	 [11, 8, 6], #vizinhos do noh 10
	 [10, 8, 7]] #vizinhos do noh 11

def buscaEmLargura(nohDePartida, nohDeChegada):
	fila = [] #começa com "0"
	fila.append(nohDePartida)
	while len(fila) > 0:
		noh = fila.pop(0) #dequeue
		nohsVisitados[noh] = 1
		print(mD[noh])
		#print(grafo[noh])
		if noh == nohDeChegada:
			print("Chegou ao destino")
			break
		for n in grafo[noh]:
			if nohsVisitados[n] == 0:
				nohsVisitados[n] = 1
				fila.append(n)
				print("Nós visitados")
				print(nohsVisitados)
				print("Fila:")
				print(fila)
                
nohDePartida = 0
nohDeChegada = 11
nohsVisitados = [0,0,0,0,0,0,0,0,0,0,0,0]

buscaEmLargura(nohDePartida, nohDeChegada)
