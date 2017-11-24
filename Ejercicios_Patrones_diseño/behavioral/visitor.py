class House(object):  # La clase que se visita
	def accept(self, visitor):
		"""Interfaz para aceptar un visitante"""
		visitor.visit(self)  # Desencadena la operación de visita!
	
	def work_on_hvac(self, hvac_specialist):
		print(self, "worked on by",
			  hvac_specialist)  # Tenga en cuenta que ahora tenemos una referencia al objeto especialista HVAC en el objeto de la casa.
	
	def work_on_electricity(self, electrician):
		print(self, "worked on by",
			  electrician)  # ¡Tenga en cuenta que ahora tenemos una referencia al objeto electricista en el objeto de la casa!
	
	def __str__(self):
		"""Simplemente devuelva el nombre de la clase cuando se imprima el objeto de la casa"""
		return self.__class__.__name__


class Visitor(object):
	"""Visitante abstracto"""
	
	def __str__(self):
		"""Simplemente devuelva el nombre de la clase cuando se imprima el objeto Visitor"""
		return self.__class__.__name__


class HvacSpecialist(Visitor):  # Hereda de la clase principal, Visitante
	"""Visitante concreto: especialista HVAC"""
	
	def visit(self, house):
		house.work_on_hvac(self)  # Tenga en cuenta que el visitante ahora tiene una referencia al objeto de la casa


class Electrician(Visitor):  # Hereda de la clase principal, Visitante
	"""Visitante concreto: electricista"""
	
	def visit(self, house):
		house.work_on_electricity(self)  # Tenga en cuenta que el visitante ahora tiene una referencia al objeto de la casa


# Crear un especialista en HVAC
hv = HvacSpecialist()
# Crea un electricista
e = Electrician()

# Crea una casa
home = House()

# Deje que la casa acepte al especialista en HVAC y trabaje en la casa invocando el método visit ()
home.accept(hv)

# Deje que la casa acepte al electricista y trabaje en la casa invocando el método visit ()
home.accept(e)



#Maria Isabel Gallegos González