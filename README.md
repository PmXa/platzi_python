---
Escuela: Programación y desarrollo de software
Profesor: Facundo García Martoni
---

# Curso de Python: comprehensions, lambdas y manejo de errores

[TOC]

## El Zen de Python 🙏

Importando el módulo `this`, se puede mostrar el zen (los principios más importantes de python). Se creó en 1999 por Tim Peters. El zen es:

1. Beautiful is better than ugly.
2. Explicit is better than implicit.
3. Simple is better than complex.
4. Complex is better than complicated.
5. Flat is better than nested.
6. Sparse is better than dense.
7. Readability counts.
8. Special cases aren't special enough to break the rules.
9. Although practicality beats purity.
10. Errors should never pass silently.
11. Unless explicitly silenced.
12. In the face of ambiguity, refuse the temptation to guess.
13. There should be one -and preferably only one- obvious way to do it.
14. Although that way may not be obvious at first unless you're Dutch.
15. Now is better than never.
16. Although _never_ is often better than _right_ now.
17. If the implementation is hard to explain, it's a bad idea.
18. If the implementation is easy to explain, it may be a good idea.
19. Namespaces are one honking great idea -- let's do more of those!

## Entornos virtuales 💻

Es como *clonar* la instalación de python para cada proyecto que tengamos. De esta manera, podemos instalar, actualizar o remover versiones de python y de sus módulos sin afectar la dependencia de otros proyectos.

``` bash
# En python, <-m> se usa para llamar a un módulo
# Por convención se llama <venv> al ambiente virtual
python3 -m venv <nombre_del_ambiente>

# Para activar el ambiente
source <nombre_del_ambiente>/bin/activate

# Para desactivar el ambiente
deactivate
```

Por supuesto, se puede definir un *alias* para no tener que escribir todo el comando de activación/desactivación cada vez.

> 💡 El ambiente virtual sólo funciona en nuestra computadora, por lo que debería ignorarse si se sube el proyecto a GitHub con un `.gitignore`.

### PIP 🐍

Con pip podemos instalar módulos de forma global o individualmente para cada ambiente virtual. También podemos exportar a un archivo los módulos instalados para que otra persona sepa y después pueda instalar los módulos necesarios para el proyecto ¡incluso si esta al otro lado del mundo!

```python
# Listemos los paquetes que tenemos instalados y exportémoslos a un archivo
pip freeze > requirements.txt

# Para instalar los archivos especificados del archivo
pip install -r requirements.txt
```

## Comprehension lists & dicts 📖

Primero debemos recordar que , como las listas, tuplas y diccionarios son todos objetos de Python, pueden anidarse y usarse unos dentro de otros:

```python
# Diccionarios en listas
pepes_nerd = [
    {"number": "1", "name":"Guty"},
    {"number": "2", "name":"Armando"},
    {"number": "3", "name":"Marco"},
    {"number": "4", "name":"Shake"},
    {"number": "5", "name":"Pol"},
    {"number": "6", "name":"Jorge"},
    {"number": "7", "name":"Bean"},
    {"number": "8", "name":"Edgar"},
    {"number": "9", "name":"Mooze"},
    {"number": "10", "name":"MMM"},
    {"number": "11", "name":"Brendita"},
    {"number": "12", "name":"Lisset"},
]

# Listas en diccionarios
number_families = {
    "natural": [0, 1, 2, 3, 4, 5],
    "integer": [-2, -1, 0 , 1, 2],
    "real": [-4.5, -2.53, 2.718, 3.14]
}
```

Las *comprehension lists* son estructuras que se usan para crear nuevas listas y siguen la sintaxis `[element for element in iterable if condition]`  y se lee primero el ciclo, luego el elemento y luego la condición: *para cada **elemento** del **iterable** guarda el **elemento** sólo si se cumple la siguiente **condición***.

Por ejemplo, si queremos obtener el cuadrado de los números del 1 al 100 que **NO** sean divisibles entre 3 podemos resolver el problema de dos formas:

```python
# Método 1: clásico
squares =[]
for i in range(1, 101):
    if (i%3 != 0):
        squares.append(i**2)
        
# Método 2: comprehension list
squares = [i**2 for i in range(1, 101) if (i%3 != 0)]
```

Y podemos hacer ejemplos más complejos, como crear una lista de todos los múltiplos de 4, 6 y 9 menores a 5 dígitos:

```python
overly_complicated_list = [i for i in range(1, 99999) if (i%4 == 0 and i%6 == 0 and i%9 == 0)]
```

Un concepto similar se aplica a los diccionarios, con la sintaxis `{key: value for value in iterable if condition}`. De igual manera, la lectura es *para cada **elemento** del **iterable**, guarda ese **elemento** como la llave y valor sólo si se cumple la **condición***. Por ejemplo, para crear un diccionario tal que:

- sus llaves sean no divisibles entre 3 de entre los primeros 100 números naturales y
- sus valores sean el valor de la llave al cubo

```python
comp_dict = {i: i**3 for i in range(1, 101) if i%3 != 0}
```

## Funciones ⚙

### Funciones anónimas

También se conocen como funciones lambda y son funciones de una sóla linea con la sintaxis `<identificador> = lambda <argumentos>: <expresión>`. El objeto función se almacena en el identificador y así es como podemos invocarla:

```python
# Para checar si una palabra es un palíndromo
p_check = lambda word: word == word[::-2]

p_check("ana") # True
```

Un ejemplo peculiar de las funciones anónimas es al hacer la *fusión* de diccionarios. Para cada *entrada de diccionario* `worker`, añade una *llave* llamada `old` cuyo *valor* sea la evaluación (`True` o `False`) de si su edad es mayor a 70 años:

``` python
lambda worker: worker | {"old": worker["age"] >= 70}
```

> 💡 El operador "`|`" es el *pipe operator* y es nuevo de python 3.9. Es el equivalente a sumar listas, pero con diccionarios.

Por supuesto, el código anterior es mucho más útil si lo aplicamos con (spoiler 👀) [la función map](#`map`).

### Funciones de orden superior

Una función es de orden superior cuyo argumento incluye otra función, por ejemplo:

```python
# Función de orden superior
def run(func):
    func()

# Función común, genérica y corriente
def holi():
    print("Holi! 😃")
    
# Función común, genérica y corriente 2
def bye():
    print("Adiós 🙁")
    
run(holi)	# "Holi! 😃"
run(bye)	# "Adiós 🙁"
```

Las tres funciones de orden superior más importantes son:

#### `filter`

Sirve para aplicar una función (primer argumento) como criterio a un iterable (segundo argumento) cualquier cosa que pueda recorrerse en Python). Por ejemplo, podemos *filtrar* los elementos impares:

```python
my_list = [1,2,4,5,6,8,9,11]
odd_only = list(filter(lambda x: x%2 != 0, my_list))
print(odd) # [1,5,9,11]
```

#### `map`

Nos permite aplicar una función a cada elemento de un iterable con la misma sintaxis que con `filter`, usando una función en el primer argumento y el iterable en el segundo uwu. Por ejemplo, podemos elevar al cuadrado *cada* elemento de `my_list`:

```python
my_list = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, my_list))
print(squared) # [1, 4, 9, 16, 25]
```

#### `reduce`

Esta función *colapsa* o *reduce* todos los elementos a un único resultado aplicando una función con **dos** argumentos: el primero de ellos actuará como el *resultado acumulado final* y, el segundo, será el siguiente elemento del iterable.

> 💡 ¡La función `reduce` debe importarse del módulo `functools`!

Por ejemplo, podemos *reducir* `[2, 2, 2, 2]` a 16 mediante:

```python
from functools import reduce
my_list = [1, 2, 3, 4, 5, 6]
product = reduce(lambda a,b: a*b, my_list)
print(product) # 720
```

![filter, map and reduce functions](https://miro.medium.com/max/1200/1*DreeF8a4h2pvxRly39HjAA.jpeg)