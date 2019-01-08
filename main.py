import cv2
from IndexInverse import InvIndex
import numpy as np
from matplotlib import pyplot as plt
import math
from list_filenames import list_files
import joblib
import sys



def similarity(des1, des2):
	array1 = np.array(des1, dtype = np.float32)
	array1 /= np.linalg.norm(array1,2)
	
	array2 = np.array(des2, dtype = np.float32)
	array2 /= np.linalg.norm(array2,2)

	return np.dot(array1, array2)
	
def Ejercicio2(filenames, predict_filenames):
	#Map filename to indice
	filename_to_idx = {}


	#Rellenamos el map
	for i in range(0, len(filenames)):
		filename_to_idx[filenames[i]] = i

	print("Listo Filename to Index")	

	#Creamos la bolsa de palabras
	with open("wordBag.plk", "rb") as f:
		bolsa = joblib.load(f)

	print("Cargada bolsa de palabras")

	

	#Creamos el indice
	index = InvIndex(bolsa)

	

	#bolsa = None

	print("Listo indice invertido")

	#with open("tfWeight.plk", "rb") as f:
	#	tfweight = joblib.load(f)



	#print("Listo TF-Weight")

	for label in predict_filenames:

		print("Comienza prediccion de " + label)
		idx_label = filename_to_idx[label]
		bolsa_label = bolsa[idx_label]
		posible_img = []
		related_img = []

		matches = np.nonzero(bolsa_label)
		print("Listos los Matches")


		for m in matches[0]:

			for img in index[m]:
				if(img not in posible_img and img != idx_label):
					posible_img.append(img)

		print("Lista la lista de posibles imagenes")


		for img in posible_img:
			related_img.append((img, similarity(bolsa[img], bolsa_label)))

		print("Anadida tasa de similaridad")

		related_img = sorted(related_img, key = lambda x : x[1], reverse = True)
		
		names_img = []
		for img in related_img[:5]:
			names_img.append(filenames[img[0]])

		print(label + ": " + str(names_img[:20]) + "\n")
			

def main():
	filenames = list_files(sys.argv[1])
	idx = filenames.index(sys.argv[1] + "/all_souls_000026.jpg")
	idx1 = filenames.index(sys.argv[1] + "/ashmolean_000305.jpg")

	predict_filenames = [filenames[idx], filenames[idx1]]

	print("Comienza Ejercicio 2: ")
	Ejercicio2(filenames, predict_filenames)


if __name__ == '__main__':
	main()
