# Python Classes
# In Python, you use classes to describe objects. 
# Think of a class as a tool you use to create your own data structures that contain information about something; 
# you can then use functions (methods) to perform operations on the data you describe. 
# A class models how something should be defined and represents an idea or a blueprint for creating objects in Python.

# Creating a Class
# Say that you want to create a class to describe a router. The first thing you have to do is define it. 
# In Python, you define a class by using the class keyword, giving the class a name, and then closing with a colon. 
# Pep8 recommends capitalizing a class name to differentiate it from a variable. 

# Here is a simple example of creating a class in Python:



class Router:
    '''Router Class'''
    def __init__(self, model, swversion, ip_add):
        '''initialize values'''
        self.model = model
        self.swversion = swversion
        self.ip_add = ip_add

rtr1 = Router('iosV', '15.6.7', '10.10.10.1')

print(f'El modelo de R1 es: {rtr1.model}')
print('El modelo de R1 es: ' + rtr1.model)

"""
#Explicacion del codigo
class Router::      Define una nueva clase llamada Router.
'''Router Class''': Es un comentario (docstring) que explica qué hace la clase. 
                    En este caso, nos dice que la clase es un "Router", pero puedes personalizar este comentario para agregar más detalles sobre su propósito.
El método __init__
def __init__(self, model, swversion, ip_add):: El __init__ es el constructor de la clase. Es un método especial que se llama automáticamente cuando se crea una nueva instancia (objeto) de la clase.
self: Es una referencia al objeto que se está creando. Permite acceder a los atributos y métodos de la instancia.
model, swversion, ip_add: Son los parámetros que se pasan al crear un objeto. Estos parámetros se usan para inicializar los atributos de la clase.
self.model = model: Asigna el valor del parámetro model al atributo model de la instancia.
self.swversion = swversion: Asigna el valor del parámetro swversion al atributo swversion de la instancia.
self.ip_add = ip_add: Asigna el valor del parámetro ip_add al atributo ip_add de la instancia.
"""



rtr2= Router('isr4221', '16.9.5', '10.10.10.5')
print('El modelo de R2 es: ' + rtr2.model)