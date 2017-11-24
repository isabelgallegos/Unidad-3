class Component(object):
	"""Clase abstracta"""
	
	def __init__(self, *args, **kwargs):
		pass
	
	def component_function(self):
		pass


class Child(Component):  # Hereda de la clase abstracta, Componente
	"""Clase de hormigón"""
	
	def __init__(self, *args, **kwargs):
		Component.__init__(self, *args, **kwargs)
		
		# ¡Aquí es donde almacenamos el nombre de su artículo hijo!
		self.name = args[0]
	
	def component_function(self):
		# ¡Imprima el nombre de su artículo hijo aquí!
		print("{}".format(self.name))


class Composite(Component):  # Hereda de la clase abstracta, Componente
	"""Clase de hormigón y mantiene la estructura recursiva del árbol"""
	
	def __init__(self, *args, **kwargs):
		Component.__init__(self, *args, **kwargs)
		
		# Aquí es donde almacenamos el nombre del objeto compuesto
		self.name = args[0]
		
		# Aquí es donde guardamos nuestros artículos para niños
		self.children = []
	
	def append_child(self, child):
		"""Método para agregar un nuevo elemento secundario"""
		self.children.append(child)
	
	def remove_child(self, child):
		"""Método para eliminar un elemento hijo"""
		self.children.remove(child)
	
	def component_function(self):
		# Imprime el nombre del objeto compuesto
		print("{}".format(self.name))
		
		# Itere a través de los objetos secundarios e invoque la función de sus componentes imprimiendo sus nombres
		for i in self.children:
			i.component_function()


# Construye un submenú compuesto 1
sub1 = Composite("submenu1")

# Crea un nuevo hijo sub_submenu 11
sub11 = Child("sub_submenu 11")
# Crear un nuevo sub_submenu de niño 12
sub12 = Child("sub_submenu 12")

# Agregue el sub_submenú 11 al submenú 1
sub1.append_child(sub11)
# Agregue el sub_submenú 12 al submenú 1
sub1.append_child(sub12)

# Crea un menú compuesto de alto nivel
top = Composite("top_menu")

# Construye un submenú 2 que no sea un compuesto
sub2 = Child("submenu2")

# Agregue el submenú compuesto 1 al menú compuesto de nivel superior
top.append_child(sub1)

# Agregue el submenú simple 2 al menú compuesto de nivel superior
top.append_child(sub2)

# ¡Probemos si nuestro patrón Compuesto funciona!
top.component_function()




#Maria Isabel Gallegos González