class Strategy:
	"""La clase de patrón de estrategia"""
	
	def __init__(self, function = None):
		self.name = "Default Strategy"
	
	# Si se proporciona una referencia a una función, reemplace el método execute () con la función dada
	
	
	def execute(self):  # Esto se reemplaza por otra versión si se proporciona otra estrategia.
		"""El método defait que imprime el nombre de la estrategia que se está utilizando"""
		print("{} is used!".format(self.name))


# Método de reemplazo 1
def strategy_one(self):
	print("{} is used to execute method 1".format(self.name))


# Método de reemplazo 2
def strategy_two(self):
	print("{} is used to execute method 2".format(self.name))


# Vamos a crear nuestra estrategia predeterminada
s0 = Strategy()
# Vamos a ejecutar nuestra estrategia predeterminada
s0.execute()

# Creemos la primera variante de nuestra estrategia predeterminada proporcionando un nuevo comportamiento
s1 = Strategy(strategy_one)
# Vamos a poner su nombre
s1.name = "Strategy One"
# Vamos a ejecutar la estrategia
s1.execute()

s2 = Strategy(strategy_two)
s2.name = "Strategy Two"
s2.execute()


#Maria Isabel Gallegos González