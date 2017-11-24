class Subject(object):  # Representa lo que se está 'observando'
	
	def __init__(self):
		self._observers = []  # Esto donde las referencias a todos los observadores se mantienen
	
	# Tenga en cuenta que esta es una relación de uno a muchos: habrá un tema para ser observado por múltiples observadores
	
	def attach(self, observer):
		if observer not in self._observers:  # Si el observador no está ya en la lista de observadores
			self._observers.append(observer)  # anexar al observador a la lista
	
	def detach(self, observer):  # Simplemente elimine al observador
		try:
			self._observers.remove(observer)
		except ValueError:
			pass
	
	def notify(self, modifier = None):
		for observer in self._observers:  # Para todos los observadores en la lista
			if modifier != observer:  # No notifique al observador que está actualizando la temperatura
				observer.update(self)  # Alerta a los observadores!


class Core(Subject):  # Hereda de la clase Asunto
	
	def __init__(self, name = ""):
		Subject.__init__(self)
		self._name = name  # Establecer el nombre del núcleo
		self._temp = 0  # Inicializa la temperatura del núcleo
	
	@property  # Getter que obtiene la temperatura central
	def temp(self):
		return self._temp
	
	@temp.setter  # Setter que establece la temperatura central
	def temp(self, temp):
		self._temp = temp
		self.notify()  # Notificar a los observadores cada vez que alguien cambie la temperatura central


class TempViewer:
	def update(self, subject):  # Método de alerta que se invoca cuando se invoca el método notify () en un tema concreto
		print("Temperature Viewer: {} has Temperature {}".format(subject._name, subject._temp))


# Vamos a crear nuestros temas
c1 = Core("Core 1")
c2 = Core("Core 2")

# Creemos nuestros observadores
v1 = TempViewer()
v2 = TempViewer()

# Adjuntemos nuestros observadores al primer núcleo
c1.attach(v1)
c1.attach(v2)

# Cambiemos la temperatura de nuestro primer núcleo
c1.temp = 70
c1.temp = 100


#Maria Isabel Gallegos González