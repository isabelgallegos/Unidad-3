class Perro:
	def speak(self):
		return "Woof!"
	
	def __str__(self):
		return "Perro"


class PerroFactory:
	"""Fábrica de Conctretar"""
	
	def obtener_pet(self):
		"""Regresa un objeto de perro"""
		return Perro()
	
	def obtener_food(self):
		"""Regresa Un objeto comida del perro """
		return "Comida del perro!!"


class Tienda_pet:
	"""Petstore alberga nuestra fábrica abstracta"""
	
	def __init__(self, pet_factory = None):
		self._pet_factory = pet_factory
	
	def mostrar_pet(self):
		"""Mestra de los objetos de objeto retornado por PerroFactory"""
		pet = self._pet_factory.obtener_pet()
		pet_comida = self._pet_factory.obtener_food()
		print("Nuestro pet es'{}'!".format(pet))
		print("Nuestro pet dice hola por '{}'".format(pet.speak()))
		print("La comida de esto es'{}'!".format(pet_comida))


factory = PerroFactory()

shop = Tienda_pet(factory)

shop.mostrar_pet()


#Maria Isabel Gallegos González