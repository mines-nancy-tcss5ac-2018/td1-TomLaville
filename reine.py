import numpy as np

##utilise dans fillBoard pour les diagonales
def inBounds(x, y, n):
	if x>=0 and x<n and y>=0 and y<n: 
		return True
	return False


##rempli de 1 pour les cases pouvant etre accedes par la dame en position x, y
def fillBoard(mat, x, y):
	n = len(mat)
	
	mat[x][0] = 1
	
	for i in range(n):
		##lignes et colonnes
		mat[x][i] = 1
		mat[i][y] = 1
		
	##diagonales
	for i in range(-n, n):
		if inBounds(x+i, y+i, n):
			mat[x+i][y+i] = 1

		if inBounds(x-i, y+i, n):
			mat[x-i][y+i] = 1

		if inBounds(x+i, y-i, n):
			mat[x+i][y-i] = 1

		if inBounds(x-i, y-i, n):
			mat[x-i][y-i] = 1

	return mat

##resout les probleme par recursivite

def perform(mat, raw):
	n = len(mat)
	c = 0
	##compte le nombre de positions valides pour la derniere colonne
	if raw == n-1:
		
		for k in range(n):
			if mat[n-1][k] == 0:
				c+= 1
	##pour une colonne entre 0 et n-1: on parcourt les cases de la colonne et on continue sur la colonne suivante en mettant a jour la matrice mat des positions possibles.

	else:
		for k in range(n):
			if mat[raw][k] == 0:
				mat_ = np.array(mat, copy=True)
				mat_ = fillBoard(mat_, raw, k)

				c+= perform(mat_, raw+1)
	return c

def solve(n):
	mat = np.zeros((n, n))
	return perform(mat, 0)

assert solve(8) == 92
print(solve(6))