import joblib
from time import clock
import numpy as np

def InvIndex(bolsa):
	index = []

	word_file = np.transpose(bolsa)

	#Se crea una lista de listas. Cada una de estas listas contiene las imagenes en las que aparece el descriptor correspondiente
	idx = np.nonzero(word_file)

	for i in range(word_file.shape[0]):
		index.append([])

	for i,j in zip(idx[0], idx[1]):
		index[i].append(j)	


	return index


def escribirIndex(index):
	with open("index12.txt", "w") as f:
		f.write(str(len(index)))

		for i in range(len(index)):
			s = str(i)
			for j in range(len(index[i])):
				s = s + " " + str(index[i][j])
	
			f.write(s + "\n")


		f.close()				
		

def leerIndex(file_index):
	index = []

	with open(file_index, "r") as f:

		lenth = int(f.readline())

		for i in range(lenth):
			index.append([])

		
		s = f.readline()

		while(s != ""):

			word_list = results = list(map(int, s.split()))
			wordID = word_list[0]

			for idx_file in word_list[1:]:
				index[wordID].append(idx_file)
			
		


		f.close()	

	return index			
