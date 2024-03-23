# SEMANA 15
'''Utilizar diccionarios en Python para representar información estructurada y realizar operaciones comunes.'''

# Crea un diccionario 
mi_diccionario= [
  {"nombres": "Juan", "edad": 30, "ciudad": "El Coca", "profesion": "Ingeniero en Tecnologías de la información"},
  {"nombres": "Pepita", "edad": 24, "ciudad": "Riobamba", "profesion": "Físico"},
  {"nombres": "Patricia", "edad": 36, "ciudad": "Tena", "profesion": "Economía"},
  {"nombres": "Anthony", "edad": 17, "ciudad": "Quito", "profesion": "Mecánico"}
]
# Acceder y modificar elementos del diccionario
# Modificar la ciudad El Coca por la ciudad Puyo
mi_diccionario[0]["ciudad"] = "Puyo"

# Agregar una nueva clave-valor que represente la profesion de la persona 
mi_diccionario[1]["profesion"] = "Ingeniero en Sistemas"

# Verifica si la clave "telefono" existe en el diccionario. Si no existe, agrégala con un número de teléfono ficticio.
if "telefono" not in mi_diccionario[2]:
  mi_diccionario[2]["telefono"] = "0994568792"

# Elimina la clave "edad" del diccionario, ya que esa información no es necesaria.
del mi_diccionario[3]["edad"]

# Imprime el diccionario completo
print(mi_diccionario)