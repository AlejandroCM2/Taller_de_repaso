from dataclasses import dataclass

@dataclass
class Elemento:
    nombre: str

    def comparar_nombres(self, otro_elemento):
        return self.nombre == otro_elemento.nombre

class Conjunto:
    contador = 0

    def __init__(self, nombre):
        self.elementos = []
        self.nombre = nombre
        Conjunto.contador += 1
        self.__id = Conjunto.contador

    @property
    def id(self):
        return self.__id

    def agregar_elemento(self, elemento):
        if not any(e.nombre == elemento.nombre for e in self.elementos):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto):
        for elemento in otro_conjunto.elementos:
            self.agregar_elemento(elemento)

    def __add__(self, otro_conjunto):
        resultado = Conjunto(f"{self.nombre} + {otro_conjunto.nombre}")
        resultado.unir(self)
        resultado.unir(otro_conjunto)
        return resultado

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        nombre_resultante = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        elementos_interseccion = [
            elemento for elemento in conjunto1.elementos if elemento in conjunto2.elementos
        ]
        resultado = cls(nombre_resultante)
        resultado.elementos = elementos_interseccion
        return resultado

    def __str__(self):
        elementos_str = ", ".join([elemento.nombre for elemento in self.elementos])
        return f"Conjunto {self.nombre}: ({elementos_str})"

elemento1 = Elemento("A")
elemento2 = Elemento("B")
elemento3 = Elemento("C")

conjunto1 = Conjunto("Conjunto A")
conjunto2 = Conjunto("Conjunto B")

conjunto1.agregar_elemento(elemento1)
conjunto1.agregar_elemento(elemento2)

conjunto2.agregar_elemento(elemento2)
conjunto2.agregar_elemento(elemento3)

conjunto_interseccion = Conjunto.intersectar(conjunto1, conjunto2)

print(conjunto_interseccion)  # Conjunto Conjunto A INTERSECTADO Conjunto B: (B)
