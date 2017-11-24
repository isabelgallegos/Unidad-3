def count_to(count):
	"""Nuestra implementación de iterador"""
	
	# Nuestra lista
	numbers_in_german = ["eins", "zwei", "drei", "vier", "funf"]
	
	# Nuestro iterador incorporado
	# Crea una tupla como (1, "eins")
	iterator = zip(range(count), numbers_in_german)
	
	# Itera a través de nuestra lista iterable
	# Extrae los números alemanes
	# Póngalos en un generador llamado número
	for position, number in iterator:
		# Devuelve un 'generador' que contiene números en alemán
		yield number
	
	# Probemos el generador devuelto por nuestro iterador


for num in count_to(3):
	print("{}".format(num))

for num in count_to(4):
	print("{}".format(num))



#Maria Isabel Gallegos González