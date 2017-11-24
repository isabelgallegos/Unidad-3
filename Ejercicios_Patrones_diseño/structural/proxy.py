import time

class Producer:
	"""Define el 'resource-intesive' objecto a instanciar"""
	def produce(self):
		print("Producer esta trabajando dificil")
	def meet(self):
		print("producer has time to meet you now!!!")
class Proxy:
	"""Define the 'relatively-intensive' proxy to instantiate as a middleman"""
	def __init__(self):
		self.ocupado = 'No'
		self.productor = None
		
	def produce(self):
		"""Checa si el productor esta disponible"""
		print("Checando artista si el productor esta disponible")
		
		if self.ocupado == 'No':
			#Si el productor esta disponible, crear un nuevo objeto productor
			self.producer=Producer()
			time.sleep(2)
			#Hacer el productor conozca al invitado
			self.producer.meet()
		
		else:
			
			time.sleep(2)
			print("Productor esta ocupado")
			
p = Proxy()

p.produce()
p.ocupado = 'Yes'
p.produce()



#Maria Isabel Gallegos González