import numpy as np
import math
import joblib
from time import clock

def tfWeight(bolsa):
	shape = bolsa.shape
	tf = np.zeros(shape, dtype = np.float16)

	IDF2_L = []
	TF2_L = []

	indices = np.nonzero(bolsa)

	print("Preparando IDF2_L")
	print(shape[1])
	for i in range(shape[1]):
		IDF2_L.append(0)


	for j in indices[1]:
		IDF2_L[j] += 1

	print("Preparando TF2")
	for i in range(shape[0]):
		TF2_L.append(0)

	for i, j in zip(indices[0], indices[1]):
		TF2_L[i] += bolsa[i,j]
		

	IDF = np.array(IDF2_L, dtype = np.float16)
	IDF = np.true_divide(bolsa.shape[0],IDF)
	IDF = np.log(IDF)


	for d in range(shape[0]):
		print("TfWeight Document: " + str(d)) 
		TF = np.true_divide(bolsa[d,:], TF2_L[d])
		for t in range(shape[1]):	
			tf[d,t] = TF[t] * IDF[t]


	return tf


def main():
	with open("wordBag.plk", "rb") as f:
		bolsa = joblib.load(f)

	print("Leida Bolsa")

	tf = tfWeight(bolsa)

	with open("tfWeight.plk", "wb") as f:
		joblib.dump(tf, f)


if __name__ == '__main__':
	main()


