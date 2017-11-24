import copy


class Prototype:
	def __init__(self):
		self._objectos = {}
	
	def registrar_objecto(self, nombre, obj):
		"""Registrar un objecto"""
		self._objectos[nombre] = obj
	
	def cancelar_registro(self, nombre):
		"""Cancelar objecto"""
		del self._objectos[nombre]
	
	def clonar(self, nombre, **attr):
		"""Clonar un objecto registrado y actualizar estos atributos"""
		obj = copy.deepcopy(self._objectos.get(nombre))
		obj.__dict__.update(attr)
		return obj


class Carro:
	def __init__(self):
		self.nombre = "Skylark"
		self.color = "Rojo"
		self.opciones = "Ex"
	
	def __str__(self):
		return '{} | {} | {}'.format(self.nombre, self.color, self.opciones)


c = Carro()
prototype = Prototype()
prototype.registrar_objecto('skylark', c)

c1 = prototype.clonar('skylark')
print(c1)


#Maria Isabel Gallegos González