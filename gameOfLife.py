import numpy as np
import time
import os
import Config

def isAlive(x, y):
	if initialGrid[x, y] == 1:
		return 1
	else:
		return 0

def findNewState(x, y, numberOfNeighbors):
	if numberOfNeighbors<2 and isAlive(x,y) == 1:
		newState = 0
	elif numberOfNeighbors>3 and isAlive(x,y) == 1:
		newState = 0
	elif numberOfNeighbors == 3 and isAlive(x,y) == 0:
		newState = 1
	else:
		newState = isAlive(x, y)

	return newState

def findNeighbors(x, y, initialGrid):
	neighbors = 0
	for i in range(x-1, x+2):
		for j in range(y-1, y+2):
			#print('loop', i, j)
			try:
				element = initialGrid[i, j]
				if isAlive(i, j) == 1:
					if i == x and j == y:
						continue
					else:
						#print('n')
						neighbors = neighbors + 1 
			except Exception as exception:
				#print(exception)
				continue

	return neighbors


def changeState(x, y, initialGrid, finalGrid):
	numberOfNeighbors = findNeighbors(x, y, initialGrid)
	newState = findNewState(x, y, numberOfNeighbors)
	finalGrid[x, y] = newState


if __name__ == '__main__':

	finalGrid = np.array([[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]])
	initialGrid = np.array(Config.initialGrid)
	size = 5
	n = Config.generations
	t = Config.shiftSpeed

	gen = 0
	while gen < n:
		for i in range(size):
			for j in range(size):
				changeState(i, j, initialGrid, finalGrid)

		print(finalGrid)
		time.sleep(t)
		os.system('cls')

		initialGrid = finalGrid
		finalGrid = np.array([[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]])

		gen += 1