# Methods
# Attributes describe an object, and methods allow you to interact with an object. 
# Methods are functions you define as part of a class. In the previous section, you created an object and applied some attributes to it. 
# Example 4-1 shows how you can work with an object by using methods. 
# A method that allows you to see the details hidden within an object without typing a bunch of commands 
# over and over would be a useful method to add to a class. Building on the previous example, 
# Example 4-1 adds a new function called getdesc() to format and print the key attributes of your router. 
# Notice that you pass self to this function only, as self can access the attributes applied during initialization.

#ejemplo 1
print('Ejemplo 1 - Methods')

class Router:
    '''Router Class'''
    def __init__(self, model, swversion, ip_add):
        '''initialize values'''
        self.model = model
        self.swversion = swversion
        self.ip_add = ip_add

    def getdesc(self):
        '''return a formatted description of the router'''
        desc = f'Router Model             :{self.model}\n'\
               f'Software Version         :{self.swversion}\n'\
               f'Router Management Address:{self.ip_add}'
        return desc

rtr1 = Router('iosV', '15.6.7', '10.10.10.1')
rtr2 = Router('isr4221', '16.9.5', '10.10.10.5')

print('Rtr1\n', rtr1.getdesc(), '\n', sep='')
print('Rtr2\n', rtr2.getdesc(), sep='')



# ## Descripcion del codigo 
#Definición de la clase Router
#   class Router:  Definición de la clase Router
#   '''Router Class''': Se define una clase llamada Router. El comentario dentro de las comillas triples ('''Router Class''') es un docstring que describe brevemente el propósito de la clase.
#   
#Método __init__ (constructor)
#   def __init__(self, model, swversion, ip_add): Es el constructor de la clase, que se ejecuta automáticamente cuando se crea una nueva instancia (objeto) de la clase.
#   self: Hace referencia al objeto actual que se está creando.
#   model, swversion, ip_add: Son los parámetros que se pasan al crear el objeto. Estos valores se asignan a los atributos de la clase.

# Atributos:
#   self.model: Guarda el modelo del router.
#   self.swversion: Guarda la versión del software del router.
#   self.ip_add: Guarda la dirección IP de gestión del router.

# Método getdesc
#     def getdesc(self): Es un método que devuelve una descripción formateada del router.
#     Se utiliza f-strings para crear una cadena de texto con el formato deseado. 
#     Cada línea de texto describe uno de los atributos del router:
#     self.model: El modelo del router.
#     self.swversion: La versión del software.
#     self.ip_add: La dirección IP de gestión.
#     desc: Almacena la cadena formateada que se devuelve como descripción.
#     return desc: Devuelve la descripción formateada.

# Creación de instancias de la clase Router
#         rtr1 = Router('iosV', '15.6.7', '10.10.10.1')
#         rtr2 = Router('isr4221', '16.9.5', '10.10.10.5')