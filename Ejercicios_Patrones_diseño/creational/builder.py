class Director():
	"""Director"""
	
	def __init__(self, builder):
		self._builder = builder
	
	def constructor_carros(self):
		self._builder.crear_nuevo_carro()
		self._builder.agregar_modelo()
		self._builder.agregar_llantas()
		self._builder.agregar_motor()
	
	def obtener_carro(self):
		return self._builder.carro


class Builder():
	"""Construccion abstracta"""
	
	def __init__(self):
		self.carro = None
	
	def crear_nuevo_carro(self):
		self.carro = Carro()


class SkyLarkBuilder(Builder):
	"""Concretar Builder --> provee partes y herramientas de trabajo sobre las partes"""
	
	def agregar_modelo(self):
		self.carro.modelo = "Skylark"
	
	def agregar_llantas(self):
		self.carro.llantas = "Llantas regulares"
	def agregar_motor(self):
		self.carro.motor = "Motor turbo"


class Carro():
	"""Producto"""
	
	def __init__(self):
		self.modelo = None
		self.llantas = None
		self.motor = None
	
	def __str__(self):
		return '{} | {} | {}'.format(self.modelo, self.llantas, self.motor)

builder = SkyLarkBuilder()
director = Director(builder)
director.constructor_carros()
carro = director.obtener_carro()
print(carro)


#Maria Isabel Gallegos González