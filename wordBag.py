import numpy as np
from list_filenames import list_filenames
import sys
import joblib


def BolsaPalabras(filenames):
	#Se inicializa la bolsa de palabras a 0
	bolsa_palabras = np.zeros((len(filenames), 1000000), dtype = np.uint8)

	#Para cada imagen se rellena su bolsa de palabras
	for i in range(0, len(filenames)):
		f = open(filenames[i], "r")

		s = f.readline()
		s = f.readline()

		s = f.readline()


		while(s != ""):
			idx = s.find(" ")
			wordID = int(s[:idx]) - 1

			bolsa_palabras[i][wordID] += 1

			s = f.readline()
		
		f.close()

		
	
		print("Anadido " + filenames[i] + " a la bolsa de palabras")


	return bolsa_palabras

def main():
	if(len(sys.argv) != 3):
		print("Uso: " + sys.argv[0]  + "<images_path> <word_path>")
		sys.exit(1)

	filenames = list_filenames(sys.argv[1])

	filenames_word = []

	for f in filenames:
		filenames_word.append(sys.argv[2] + "oxc1_" + f[:-4] + ".txt")

	bolsa = BolsaPalabras(filenames_word)

	with open("wordBag.plk", "wb") as f:
		joblib.dump(bolsa, f)


if __name__ == '__main__':
	main()
