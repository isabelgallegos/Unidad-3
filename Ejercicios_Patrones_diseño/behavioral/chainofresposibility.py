class Handler:  # Controlador abstracto
	"""Controlador abstracto"""
	
	def __init__(self, successor):
		self._successor = successor  # Aqui se define quién sera el próximo controlador
	
	def handle(self, request):
		handled = self._handle(request)
		
		# Aqui de lo contrario, sigue adelante
		if not handled:
			self._successor.handle(request)
	
	def _handle(self, request):
		raise NotImplementedError('Must provide implementation in subclass!')


class ConcreteHandler1(Handler):  # Hereda del controlador abstracto

	
	def _handle(self, request):
		if 0 < request <= 10:  # Se proporciona una condición para el manejo
			print("Request {} handled in handler 1".format(request))
			return True  # En esta parte indica que la solicitud ha sido manejada


class DefaultHandler(Handler):  # Hereda del controlador abstracto
	"""Controlador predeterminado"""
	
	def _handle(self, request):
		"""Si no hay ningún controlador disponible"""
		# Sin comprobación de condición, ya que este es un controlador predeterminado
		print("End of chain, no handler for {}".format(request))
		return True  # Indica que la solicitud ha sido manejada


class Client:  # Uso de controladores
	def __init__(self):
		self.handler = ConcreteHandler1(DefaultHandler(None))  # Crea manejadores y úsalos en la secuencia que quieras

	# Tenga en cuenta que el controlador predeterminado no tiene sucesor
	
	def delegate(self, requests):  # Envíe sus solicitudes una a la vez para que los manejadores manejen
		for request in requests:
			self.handler.handle(request)


# Se crea un cliente
c = Client()

# Se crean las solicitudes
requests = [2, 5, 30]

# Se enviar las solicitudes
c.delegate(requests)


#Maria Isabel Gallegos González