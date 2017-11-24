class Borg:
	"""clase Borg haciendo atributos globales"""
	_shared_state = {}
	
	def __init__(self):
		self.__dict__ = self._shared_state


class Singleton(Borg):
	"""Esta clase compartira todos los atributos entre varias instancias"""
	
	# Esto esencialmente hace el singleton objetos un objeto orientado a variables globales
	def __init__(self, **kwargs):
		Borg.__init__(self)
		# Actualiza el diccionario de atributos por insercion a una nueva llave de valor
		self._shared_state.update(kwargs)
	
	def __str__(self):
		# Regresa el diccionario de atrbutos para imprimir
		return str(self._shared_state)


# Vamos a crear un objeto singleton y agregar nuestros primeros acronys
x = Singleton(HTTP = "Hyper text transfer protocol")
# Vamos a crear otro objeto singleton y si se refiere al mismo diccionario de atributos agregando otro acroym
y = Singleton(SNMP = "Simple administrador de protocolo de red")
print(x)
# Imprimir el objeto
print(y)



#Maria Isabel Gallegos González