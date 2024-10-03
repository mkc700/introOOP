class Persona:
    # Constructor para inicializar los atributos de la persona
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo nombre
        self.edad = edad  # Atributo edad

    # Método para mostrar información de la persona
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

    # Método para simular que la persona está saludando
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}.")

    def recibir_saludo(self,env,env2):
        print(f"{env}! te manda saludos {env2}")

# Crear instancias de la clase Persona
persona1 = Persona("pedro", 25)
persona2 = Persona("manuel", 23)

# Usar métodos de las instancias
persona1.mostrar_informacion()  # Salida: Nombre: Juan, Edad: 25
persona1.saludar()  # Salida: Hola, mi nombre es Juan.

persona2.mostrar_informacion()  # Salida: Nombre: Ana, Edad: 30
persona2.saludar()  # Salida: Hola, mi nombre es Ana.

persona1.recibir_saludo(persona1.nombre,persona2.nombre)