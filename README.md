---
Escuela: Programaci贸n y desarrollo de software
Profesor: Facundo Garc铆a Martoni
---

# Curso de python: comprehensions, lambdas y manejo de errores

[TOC]

## El zen de python馃檹

Importando el m贸dulo `this`, se puede mostrar el zen (los principios m谩s importantes de python). Se cre贸 en 1999 por Tim Peters. El zen es:

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

## Entornos virtuales 馃捇

Es como *clonar* la instalaci贸n de python para cada proyecto que tengamos. De esta manera, podemos instalar, actualizar o remover versiones de python y de sus m贸dulos sin afectar la dependencia de otros proyectos.

``` bash
# En python, <-m> se usa para llamar a un m贸dulo
# Por convenci贸n se llama <venv> al ambiente virtual
python3 -m venv <nombre_del_ambiente>

# Para activar el ambiente
source <nombre_del_ambiente>/bin/activate

# Para desactivar el ambiente
deactivate
```

Por supuesto, se puede definir un *alias* para no tener que escribir todo el comando de activaci贸n/desactivaci贸n cada vez.

> 馃挕 El ambiente virtual s贸lo funciona en nuestra computadora, por lo que deber铆a ignorarse si se sube el proyecto a GitHub con un `.gitignore`.

### PIP 馃悕

Con pip podemos instalar m贸dulos de forma global o individualmente para cada ambiente virtual. Tambi茅n podemos exportar a un archivo los m贸dulos instalados para que otra persona sepa y despu茅s pueda instalar los m贸dulos necesarios para el proyecto 隆incluso si esta al otro lado del mundo!

```python
# Listemos los paquetes que tenemos instalados y export茅moslos a un archivo
pip freeze > requirements.txt

# Para instalar los archivos especificados del archivo
pip install -r requirements.txt
```

## Comprehension lists & dicts 馃摉

Primero debemos recordar que , como las listas, tuplas y diccionarios son todos objetos de python, pueden anidarse y usarse unos dentro de otros:

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

Las *comprehension lists* son estructuras que se usan para crear nuevas listas y siguen la sintaxis `[element for element in iterable if condition]`  y se lee primero el ciclo, luego el elemento y luego la condici贸n: *para cada **elemento** del **iterable** guarda el **elemento** s贸lo si se cumple la siguiente **condici贸n***.

Por ejemplo, si queremos obtener el cuadrado de los n煤meros del 1 al 100 que **NO** sean divisibles entre 3 podemos resolver el problema de dos formas:

```python
# M茅todo 1: cl谩sico
squares =[]
for i in range(1, 101):
    if (i%3 != 0):
        squares.append(i**2)
        
# M茅todo 2: comprehension list
squares = [i**2 for i in range(1, 101) if (i%3 != 0)]
```

Y podemos hacer ejemplos m谩s complejos, como crear una lista de todos los m煤ltiplos de 4, 6 y 9 menores a 5 d铆gitos:

```python
overly_complicated_list = [i for i in range(1, 99999) if (i%4 == 0 and i%6 == 0 and i%9 == 0)]
```

Un concepto similar se aplica a los diccionarios, con la sintaxis `{key: value for value in iterable if condition}`. De igual manera, la lectura es *para cada **elemento** del **iterable**, guarda ese **elemento** como la llave y valor s贸lo si se cumple la **condici贸n***. Por ejemplo, para crear un diccionario tal que:

- sus llaves sean no divisibles entre 3 de entre los primeros 100 n煤meros naturales y
- sus valores sean el valor de la llave al cubo

```python
comp_dict = {i: i**3 for i in range(1, 101) if i%3 != 0}
```

## Funciones 馃敡

### Funciones an贸nimas 馃暤锔忊?嶁檪锔?

Tambi茅n se conocen como funciones lambda y son funciones de una s贸la linea con la sintaxis `<identificador> = lambda <argumentos>: <expresi贸n>`. El objeto funci贸n se almacena en el identificador y as铆 es como podemos invocarla:

```python
# Para checar si una palabra es un pal铆ndromo
p_check = lambda word: word == word[::-2]

p_check("ana") # True
```

Un ejemplo peculiar de las funciones an贸nimas es al hacer la *fusi贸n* de diccionarios. Para cada *entrada de diccionario* `worker`, a帽ade una *llave* llamada `old` cuyo *valor* sea la evaluaci贸n (`True` o `False`) de si su edad es mayor a 70 a帽os:

```python
lambda worker: worker | {"old": worker["age"] >= 70}
```

> 馃挕 El operador "`|`" es el *pipe operator* y es nuevo de python 3.9. Es el equivalente a sumar listas, pero con diccionarios.

Por supuesto, el c贸digo anterior es mucho m谩s 煤til si lo aplicamos con (spoiler 馃憖) [la funci贸n map](#`map`).

### Funciones de orden superior

Una funci贸n es de orden superior cuyo argumento incluye otra funci贸n, por ejemplo:

```python
# Funci贸n de orden superior
def run(func):
    func()

# Funci贸n com煤n, gen茅rica y corriente
def holi():
    print("Holi! 馃槂")
    
# Funci贸n com煤n, gen茅rica y corriente 2
def bye():
    print("Adi贸s 馃檨")
    
run(holi)	# "Holi! 馃槂"
run(bye)	# "Adi贸s 馃檨"
```

Las tres funciones de orden superior m谩s importantes son:

#### `filter`

Sirve para aplicar una funci贸n (primer argumento) como criterio a un iterable (segundo argumento) cualquier cosa que pueda recorrerse en python). Por ejemplo, podemos *filtrar* los elementos impares:

```python
my_list = [1,2,4,5,6,8,9,11]
odd_only = list(filter(lambda x: x%2 != 0, my_list))
print(odd) # [1,5,9,11]
```

#### `map`

Nos permite aplicar una funci贸n a cada elemento de un iterable con la misma sintaxis que con `filter`, usando una funci贸n en el primer argumento y el iterable en el segundo uwu. Por ejemplo, podemos elevar al cuadrado *cada* elemento de `my_list`:

```python
my_list = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, my_list))
print(squared) # [1, 4, 9, 16, 25]
```

#### `reduce`

Esta funci贸n *colapsa* o *reduce* todos los elementos a un 煤nico resultado aplicando una funci贸n con **dos** argumentos: el primero de ellos actuar谩 como el *resultado acumulado final* y, el segundo, ser谩 el siguiente elemento del iterable.

> 馃挕 隆La funci贸n `reduce` debe importarse del m贸dulo `functools`!

Por ejemplo, podemos *reducir* `[2, 2, 2, 2]` a 16 mediante:

```python
from functools import reduce
my_list = [1, 2, 3, 4, 5, 6]
product = reduce(lambda a,b: a*b, my_list)
print(product) # 720
```

![filter, map and reduce functions](https://miro.medium.com/max/1200/1*DreeF8a4h2pvxRly39HjAA.jpeg)

## Manejo de errores 馃拃

### Cuando python **no** nos avisa que cometimos un error 馃槬

Cuando python **no** nos avisa del error, lo m谩s seguro es que tengamos un error de l贸gica en nuestro algoritmo, por lo que se recurre al *debugging* para *depurar* el programa. Muchos editores de texto e IDEs tienen herramientas incluidas para *depurar*, como pausar el c贸digo, avanzar l铆nea por l铆nea, *entrar* a una funci贸n, revisar los valores instant谩neos de las variables y m谩s 馃槂

### Cuando python nos avisa que tenemos un error 馃槂

Cuando python nos avisa del error lo hace a trav茅s de un *traceback*. Esto puede ser culpa ya sea de un `SyntaxError` o de un `Exception`.

```mermaid
flowchart LR

Errores --> SyntaxError & Exception
```

#### `SyntaxError`

Un `SyntaxError` es de los errores m谩s comunes y se refiere a un error de escritura o *typo*. Por ejemplo, escribir "`far`" en vez de "`for`" o "`lamda`" en vez de "`lambda`". Cuando tenemos un `SyntaxError` el programa **no** se ejecuta en absoluto, ya que el motor de python analiza todas las l铆neas de c贸digo a priori.

#### `Exceptions`

Las excepciones ocurren cuando, a pesar de estar perfectamente escrita, una expresi贸n se encuentra con un error de alg煤n tipo al *intentar* ejecutarse. Por ello, cuando ocurre una excepci贸n, el c贸digo se ejecuta normalmente hasta que ocurra una de ellas en alguna l铆nea espec铆fica.

Algunas de las excepciones m谩s comunes son:

```mermaid
flowchart

Exception --> KeyboardInterrupt & KeyError & IndexError & FileNotFoundError & ZeroDivisionError & ImportError
```

- `KeyboardInterrupt`:
  Al presionar `Ctrl + C` en la terminal para terminar el proceso, python *eleva* esta excepci贸n para cancelar todo.

- `KeyError`:
  Al tratar de acceder a una llave de un diccionario que no existe (la llave, no el diccionario).

- `IndexError`:
  Cuando se intenta acceder al 铆ndice de un iterable fuera de rango (como `x[4]` cuando `x = [0, 1]`.

- `FileNotFoundError `:
  Al tratar de manipular un archivo que no existe.

- `ZeroDivisionError`:
  Al tratar de dividir entre 0 (y el universo explota 馃挜馃寣)

- `ImportError`:
  Al salir mal la importaci贸n de un m贸dulo.

Y muchas otras...

>  馃挕 隆Hay m谩s de 50 [excepciones incluidas](https://docs.python.org/3/library/exceptions.html#bltin-exceptions) en python!

La forma en la que python nos da detalles del error es mediante un *traceback* como el siguiente:

```python
# Te lo advert铆 馃挜馃寣
1/0

"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
"""
```

1. Este *traceback* nos dice qu茅 excepci贸n ocurri贸 (`ZerDivisionError`) y un breve resumen de qu茅 significa (division by zero).
2. Se nos indica en qu茅 archivo ocurri贸 el error (`stdin` significa que fue mediante la consola), en qu茅 l铆nea y en qu茅 m贸dulo.
3. Y finalmente se nos da d贸nde ocurre la *traza del error*. Cuando ocurre una excepci贸n que no se maneja, python la *eleva* a la siguiente funci贸n. Si en esa funci贸n "superior" tampoco se maneja, se vuelve a *elevar* a la funci贸n contenedora y as铆, sucesivamente, hasta llegar a la funci贸n principal. Si en esa funci贸n principal (que puede ser `run()` o `main()`, etc.) no se maneja, el programa se corta y se muestra el *traceback*.

>  馃挕 Un *traceback* se lee de abajo hacia arriba.

Para el manejo de excepciones incluidas en python usamos `try` y `except`. Por ejemplo, para un detector de pal铆ndromos s贸lo deber铆amos aceptar cadenas de caracteres. Si un usuario ingresara un n煤mero, obtendr铆amos un `TypeError`. Para alertar al usuario de buena manera (sin asustarlo con un *traceback* que puede que no entienda) usamos la sintaxis siguiente:

```python
def check_if_palindrome(message):
  return message == message[::-1]


try:
    print(check_if_palindrome(my_string))
except TypeError:
    print("Debes ingresar una palabra o mensaje")
```

Pero, si imaginamos un caso en el que el usuario ingrese una cadena vac铆a (`""`), python devolver谩 un `True` a pesar de que, intuitivamente, nosotros reconozcamos que es un error. En casos como este, usamos `raise` para generar un error **con nuestro propio mensaje** para el error:

```python
def check_if_palindrome(message):
	try:
		if len(message) == 0:
			raise ValueError("No se admiten cadenas vac铆as")
		return message == message[::-1]
    except ValueError as ve:
        print(ve)
        return False


try:
    print(check_if_palindrome(my_string))
except TypeError:
    print("Debes ingresar una palabra o mensaje")
```

En este c贸digo, guardamos el mensaje del `ValueError` en `ve` (que viene de *value error*). Se leer铆a algo como "Intenta ... excepto que ocurra un error al que llamamos `ve`; de ser as铆, ejecuta ...". 

Tambi茅n podemos a帽adir un bloque `else` que se ejecuta **si y s贸lo si** no hubo ning煤n error dentro del bloque `try`. Finalmente, se usa `finally` (Ba Dum Tss 馃) para cerrar archivos, cerrar conexiones a bases de datos o liberar recursos despu茅s de los bloques `try ... except`.

> 馃挕 El bloque `finally` se ejecuta **pase o no pase** un error.

Una estructura m谩s completa, entonces se ver铆a algo as铆:

```python
try:
	if (condici贸n):
		raise <Exception>("Hiciste algo que t茅cnicamente es legal pero no 馃槕")
	except <Exception>:
		print("Hiciste algo mal 馃槧")
	else:
		print("Aqu铆 no pas贸 nada 馃樁")
	finally:
		print("Esto tengo que hacerlo de cualquier forma 炉\_(銉?)_/炉")
```

### Assert Statements 馃

Las *afirmaciones* en python son una alternativa al manejo de errores con `try... except`. Se leen como "afirmo que *condici贸n* y, si no, mandar茅 este *mensaje de error*" y se presentan de la forma:

```python
assert condici贸n, "mensaje de error"
```

```mermaid
flowchart TB

Code1[C贸digo] --> AS[Assert Statement]
AS --> Error & Code2[C贸digo]
```

De esta forma, podemos manejar errores *en una sola l铆nea de c贸digo*:

```python
def palindrome(string):
    assert len(string) > 0 , "No se admiten cadenas vac铆as"
    return string == string[::-1]

print(palindrome("")) # AssertionError: No se admiten cadenas vac铆as
```

> 馃挕 Al usarse `assert` se muestra **todo** el *traceback* del error.

驴Cu谩ndo usar `assert` y cu谩ndo usar `try ... except`? En realidad no hay una regla s贸lida. Se pueden intercambiar, aunque los bloques `try ... except` son mucho m谩s comunes y los `assert` est谩n m谩s orientados a testeo y errores *del y para* el programador, tal como argumenta Al Sweigart:

> In plain English, an assert statement says 鈥?*I assert that this condition holds true, and if not, there is a bug somewhere in the program*.鈥? Unlike exceptions, your code should not handle assert statements with try and except; if an assert fails, your program should crash. By failing fast like this, you shorten the time between the original cause of the bug and when you first notice the bug. This will reduce the amount of code you will have to check before finding the code that鈥檚 causing the bug. Assertions are for programmer errors, not user errors. For errors that can be recovered from (such as a file not being found or the user enter-ing invalid data), raise an exception instead of detecting it with an assertstatement.
>
> "How to automate the boring stuff with Python" - Al Sweigart

## Manejo de archivos 馃搫

A grosso modo tenemos dos tipos de archivos:

```mermaid
flowchart TB
Archivos --> A(Texto Plano \n .txt .csv. xml \n .md .py .json)
Archivos --> B(Binarios \n .jpg .mp3 .mkv .dll)
```

Normalmente en python **no** nos metemos con archivos binarios, pero s铆 con los de texto plano. Hay 3 modos en los que se puede abrir un archivo:

- R: lectura
- W: escritura (sobrescribiendo)
- A: escritura (de a帽adir, no sobrescribir)

Para abrir un archivo en python (ya sea en modo `"r"`, `"w"` o `"a"`) y guardarlo en una variable `file_name`, usamos:

```python
with open("ruta", "r") as file_name:
```

La palabra clave `with` es un *manejador contextual*; lo que hace es que, si se cierra de forma inesperada nuestro programa, el archivo no se rompe.

> 馃挕 Usar `encoding="utf-8"` como 3掳 argumento en `open` ayuda para tener mejor compatibilidad con caracteres extra帽os.