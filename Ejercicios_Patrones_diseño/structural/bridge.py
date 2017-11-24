class DrawingAPIOne(object):
	"""Abstracción específica de la implementación: clase 1 concreta"""
	
	def draw_circle(self, x, y, radius):
		print("API 1 drawing a circle at ({}, {} with radius {}!)".format(x, y, radius))


class DrawingAPITwo(object):
	"""Abstracción específica de la implementación: clase concreta dos"""
	
	def draw_circle(self, x, y, radius):
		print("API 2 drawing a circle at ({}, {} with radius {}!)".format(x, y, radius))


class Circle(object):
	"""Abstracción independiente de la implementación: por ejemplo, ¡podría haber una clase rectangular!"""
	
	def __init__(self, x, y, radius, drawing_api):
		"""Inicializa los atributos necesarios"""
		self._x = x
		self._y = y
		self._radius = radius
		self._drawing_api = drawing_api
	
	def draw(self):
		"""Abstracción específica de la implementación cuidada por otra clase: DrawingAPI"""
		self._drawing_api.draw_circle(self._x, self._y, self._radius)
	
	def scale(self, percent):
		"""Implementación-independiente"""
		self._radius *= percent


# Construye el primer objeto Circle usando API One
circle1 = Circle(1, 2, 3, DrawingAPIOne())
# Dibuja un circulo
circle1.draw()

# Construye el segundo objeto Circle usando API Two
circle2 = Circle(2, 3, 4, DrawingAPITwo())
# Dibuja un circulo



#Maria Isabel Gallegos González