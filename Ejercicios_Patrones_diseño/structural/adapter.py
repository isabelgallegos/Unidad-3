class Korean:
	"""habla koreano"""
	
	def __init__(self):
		self.name = "Koreano"
	
	def speak_korean(self):
		return "An-neyong?"


class British:
	"""Habla ingles"""
	
	def __init__(self):
		self.name = "British"
	
	# Realizamos la diferencia del metodo que se esta nombrado aqui:
	def speak_english(self):
		return "Hello!"


class Adapter:
	"""Esto cambia el nombre del método genérico a nombres de métodos individualizados"""
	
	def __init__(self, object, **adapted_method):
		"""Aqui se cambia el nombre del método"""
		self._object = object
		
		# Aqui see agrego un nuevo elemento de diccionario que establezca la asignación entre el nombre del método genérico: speak () y el método concreto.
		# Por ejemplo, speak () se traducirá a speak_korean () si el mapeo lo dice
		self.__dict__.update(adapted_method)
	
	def __getattr__(self, attr):
		"""Aqui simplemente devuelve el resto de los atributos!"""
		return getattr(self._object, attr)


# Se encuentra la lista para almacenar objetos de altavoz
objects = []

# En esta parte se crear un objeto coreano
korean = Korean()

# En esta parte se crea un objeto británico
british = British()

# En esta parte se anexan los objetos a la lista de objetos
objects.append(Adapter(korean, speak = korean.speak_korean))
objects.append(Adapter(british, speak = british.speak_english))

for obj in objects:
	print("{} says '{}'\n".format(obj.name, obj.speak()))




#Maria Isabel Gallegos González