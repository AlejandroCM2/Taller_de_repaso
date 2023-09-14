
## Clase `Elemento`

La clase `Elemento` se define utilizando el decorador `@dataclass` y tiene las siguientes características:

- **Atributo `nombre`:** Un atributo de tipo `str` que almacena el nombre del elemento.

- **Método de igualdad `__eq__`:** Se implementa un método especial `__eq__` que permite comparar dos objetos de la clase `Elemento` y determinar si sus nombres son iguales.

## Clase `Conjunto`

La clase `Conjunto` tiene las siguientes características:

- **Atributo de instancia `elementos`:** Representa una lista de objetos de la clase `Elemento`. Se inicializa como una lista vacía.

- **Atributo de instancia `nombre`:** Contiene el nombre del conjunto, que se establece mediante un parámetro en el método inicializador.

- **Atributo de clase `contador`:** Lleva un registro del número de instancias creadas de la clase `Conjunto`. Se incrementa en uno cada vez que se crea una nueva instancia.

- **Atributo privado `__id`:** Un atributo privado que se inicializa con el valor actual del atributo de clase `contador` al momento de la inicialización. Se define una propiedad de solo lectura para este atributo.

- **Método de instancia `contiene`:** Recibe un objeto de la clase `Elemento` como parámetro y devuelve un valor booleano que indica si el conjunto contiene un elemento con el mismo nombre.

- **Método de instancia `agregar_elemento`:** Recibe un objeto de la clase `Elemento` como parámetro y lo agrega a la lista de elementos del conjunto si no está contenido ya en el conjunto.

- **Método de instancia `unir`:** Recibe otro conjunto como parámetro y agrega sus elementos a la lista de elementos del conjunto actual, asegurándose de que no haya elementos repetidos. Se implementa también la operación de unión mediante el operador `+`.

- **Método de clase `intersectar`:** Recibe dos conjuntos como parámetros y retorna un nuevo conjunto con los elementos de la intersección de los conjuntos dados. El nombre del conjunto resultante se forma como "<Nombre Conjunto 1> INTERSECTADO <Nombre Conjunto 2>".

- **Método `__str__`:** Retorna una representación legible del conjunto con un formato específico: "Conjunto `<nombre>`: (`<nombre elemento 1>`, `<nombre elemento 2>`, ..., `<nombre elemento n>`)".

