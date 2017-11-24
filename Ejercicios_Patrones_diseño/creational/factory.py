class Perro:
	"""clase perro"""
	
	def __init__(self, nombre):
		self._nombre = nombre
	
	def speak(self):
		return "Ladrido"


class Gato:
	"""Clase gato"""
	
	def __init__(self, nombre):
		self._nombre = nombre
	
	def speak(self):
		return "Miau"


def obtener_pet(pet = "perro"):
	"""Metodo factory"""
	pets = dict(perro = Perro("Hope"), gato = Gato("Peace"))
	return pets[pet]


d = obtener_pet("perro")
print(d.speak())

c = obtener_pet("gato")
print(c.speak())


#Maria Isabel Gallegos González