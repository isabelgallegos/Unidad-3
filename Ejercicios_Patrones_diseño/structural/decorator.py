from functools import wraps


def hacer_parpadeo(funcion):
	"""Definir el decorador"""
	# Hacer el decorador transparente en terminos de esto nombre y docstring
	@wraps(funcion)
	# Definir el interior de la funcion
	def decorator():
		# tomar el valor de retornno de la funcion que se esta decorando
		ret = funcion()
		# Agregar la nueva funcionalidad a la funcion que esta siendo decorada
		return "<blink>" + ret + "</blink>"
	
	return decorator

# Aplicamos el decorador aqui
@hacer_parpadeo
def hola_mundo():
	"""Original funcion"""
	return "Hola, mundo!!!"


# Checar el resultado de el decorador
print(hola_mundo())
# Checar si la el nombre de la funcion es nombrada
print(hola_mundo.__name__)
print(hola_mundo.__doc__)



#Maria Isabel Gallegos González