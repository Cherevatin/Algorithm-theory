
def backpack(m, W, V, n): 

	K = [[0 for x in range(m + 1)] for x in range(n + 1)] 

	for i in range(n + 1): 
		for w in range(m + 1): 
			if i == 0 or w == 0: 
				K[i][w] = 0
			elif W[i-1] <= w: 
				K[i][w] = max(V[i-1] + K[i-1][w-W[i-1]], K[i-1][w]) 
			else: 
				K[i][w] = K[i-1][w] 

	i,j = n,m
	thgs = []
	while(True):
		if K[i][j]!=K[i-1][j]:
			thgs.append(i-1)
			j=m-W[i-1]
		i-=1
		if i == 0:
			break
	thgs.sort()

	print("\nЛучшим вариантом будет взять такие вещи:\n")

	for i in thgs:
		print("Вещь №"+str(i+1)+" стоимостью",V[i],"и весом",W[i])
	print("\nИх суммарная стоимость составляет:",K[n][m],"\n")
	

V = [16, 19, 23,28] 
W = [2, 3, 4, 5] 
K = 7 

#V = [5,6,3] 
#W = [4,5,2] 
#K = 9 

print("Список доступных вещей:")
for i in range(len(V)):
	print("№"+str(i+1)+" стоимость - "+str(V[i])+", вес - "+str(W[i]))
backpack(K, W, V, len(V))



