# Informe de proyecto #2 - Inteligencia Artificial: Relaciones de Etimología
#### Realizado Por:
1. José Miguel Mora Rodríguez
2. Dylan Rodríguez Barboza
3. Karina Zeledón Pinell
#### Profesor:
Juan Manuel Esquivel Rodríguez, Ph. D.

# Descripción del Proyecto
El objetivo primario del proyecto el procesamiento de datos mediante un motor de derivación lógico. Para el desarrollo se utilizaron dos elementos primarios: un lenguaje de lógica sobre Python(pyDatalog) y una base de datos de relaciones etimológicas. Con ellos, se desarrolló una aplicación para responder preguntas sobre relaciones entre diferentes palabras contenidas en la base de datos.
La "Etymological Wordnet" es una base de datos basada en en.wiktionary.org que recopila relaciones entre palabras en múltiples idiomas (aunque iniciando desde inglés). Tomando estos datos, se puede construyó un sistema el cual, basado en proposiciones lógicas, permite responder preguntas relacionadas con orígen común de palabras, similitud entre lenguajes, etc. 
La base de datos mencionada anteriormente posee entradas de la siguiente forma:
- idioma: palabra rel:tipo_de_relacion idioma: palabra

Las siguientes relaciones son las que se encuentran dentro de la base de datos:

|Relación|Cantidad en la base de datos|Descripción
|--------|----------------------------|-------------
a rel:derived b | 2| "a" deriva a "b"
a rel:etymologically b |1| "a" está relacionado etimológicamente con "b"
a rel:etymologically_related b|538558| "a" está relacionado etimológicamente con "b"
a rel:etymological_origin_of b|473433|"a" es la palabra de origen de "b"
rel:etymology |473433| Inversa a "rel:etymological_origin_of"
a rel:has_derived_form b |2264744| "a" deriva a "b"
a rel:is_derived_from b |2264744| Inversa de "rel:has_derived_form"
a rel:variant:orthography b |16516| A es una variante ortográfica de b

En total hay 6,031,431 relaciones en la base de .


# Descripción de la instalación

# Manual de usuario

# Operaciones implementadas
Las siguientes operaciones fueron implementadas dentro de la aplicación, por cada una se describirá un resultado interesante o bien alguna particularidad de la operación:
## Operaciones entre dos palabras
- **Determinar si dos palabras son heman@s**
- **Determinar si dos palabras son prim@s**
- **Determinar si una palabra es hij@ de otra**
- **Determinar si una palabra es ti@**
- **Determinar si son prim@s y en qué grado**.
## Operaciones entre palabras e idiomas
- **Determinar si una palabra está relacionada con un idioma**.
- **Obtener el conjunto de todas las palabras en un idioma originadas por una palabra
específica**: Se obtuvieron las palabras generadas por la palabra en inglés "dog", debido a la gran cantidad de palabras obtenidas se facilita un link a un archivo de texto el cual contiene las mismas, cabe destacar que las palabras están emparejadas (palabra, idioma): https://drive.google.com/open?id=18OsLD5YnjKptsjCwf8H0V9HNS9ka1TET 
- **Listar los idiomas relacionados con una palabra**: Los siguientes son los idiomas relacionados con la palabra "dog" en inglés: **tpi, ita, tcs, spa, rus, fra, enm y vol**. La palabra dog aparece en ambos lados de las relaciones para los idiomas listados.
## Operaciones de comparación de idiomas
- **Contar todas las palabras comunes entre dos idiomas y listar todas las palabras comunes entre dos idiomas**: Las siguientes son las palabras en común(según la base de datos) entre el idioma alemán y polaco : **puste, brat, Adam, Bhutan, Haiti, Laos, Europa, patent, Kuba, Magdalena, Emilia, Big Mac, Nauru, Ghana, Nigeria, Roman, Jemen, Kenia, Berlin, wart, Sudan, Mauritius, Barbados, Togo, Malawi, Somalia, Julia, Pandora, Niger, fort, Anna, je, Malta, Koran, Mali, mit, Polka, wie, Gambia, San Marino, Madagaskar, Lesotho, herb, elegant, handel, Angola, Liberia, Kamerun, Panama, Namibia, brutto, Paulina, Iran, Irak, Marian, Nepal, Benin, Grenada, Kata, start, Pakistan, Korea, Peru, Kanad', Sebastian, Internet, park, Oman,  Turkmenistan, Samoa, planet, bar, Tonga, Hypnos, Troja, Belize, Kanton, bunt, Magda, Olga, nagle, absurd, Honduras, Burundi, Uganda, Barbara, Hanna, Singapur, krem, Sparta y nur**. Como se puede observar gran parte de las palabras son nombres de países o nombres propios por lo que se podría llegar a dos conclusiones: aunque son países vecinos(Alemania y Polonia), el intercambio cultural en términos de léxico no es o no fue muy rico entre estos países o bien la base de datos simplemente no contiene esas palabras en común.
- **Idioma que más aportó a otro basado en porcentaje y listar todos los idiomas que aportaron a otro:** Debido a la gran cantidad de tiempo computacional requerido para la operación no se documentó ningún resultado interesante, sin embargo en la siguiente sección se hace una observación entorno a su implementación para reducir lo expuesto anteriormente.


# Detalles de implementación y diseño para mejorar la eficiencia de la aplicación

Debido a la gran cantidad de entradas en la base de datos y tomando en cuenta que el paradigma de programación lógico implica una alta tasa de procesamiento computacional se tomaron las siguientes medidas con el fin de alivianar dicha carga:

- Uso de objetos de la librería: La librería pyDatalog permite el uso de objetos como parte del kb del programa(para mayor información ingresar a: https://sites.google.com/site/pydatalog/Datalog-in-python). Se implementó una clase con el fin de representar las relaciones dentro de la base de datos:
    
    - Atributos: 
        
        -  first_lan : String: primer idioma de la relacion.
        -  first_word : String: Primera palabra en la relación.
        -  r_type: String: tipo de la relación.
        -  second_lan: List: Segundo lenguaje de la relación.
        -  second_word: Segunda palabra dentro de la relación.
    - Métodos:
    
        - _(): Método anónimo donde se definen las reglas de las operaciones posibles por cada relación. Todas las operaciones fueron implementadas en este espacio.

    El uso de objetos permite la carga de toda la base de datos en un tiempo estimado de entr 60 s - 120 s por lo que se reduce de forma significativa el tiempo de carga de la base de datos en comparación a la utilización de la función assert_fact() de la librería para agregar al Knowledge Base.
- Análisis del comportamiento de la Biblioteca: Utilizando la biblioteca en conjunto con los objetos se observó que a la hora de realizar un procesamiento se añadían "facts" al kb dependiendo del query que se realizara. Por ejemplo si se quería obtener si Parent(X,Word1,Word2) (X es una variable en la cual se obtendran todas las relaciones en el KB) se utiliza la siguiente relación(es una de las posibles clausulas):
    
      
    Relation.parent(X,Word1,Word2) <=  (Relation.second_word[X]==Word2) & (Relation.first_word[X]==Word1) & (Relation.r_type[X]=='rel:is_derived_from')

La anterior relación se interpreta como: Para todo X donde second_word es igual a Word2 y first_word es igual a Word1 y el tipo de relación es 'rel:is_derived_from'(). La biblioteca verificara la primera parte de la cláusula (Relation.second_word[X]==Word2) dejando como posible resultado solo aquellas relaciones donde se cumpla lo anterior. En cambio si se utilizara la siguiente relación:

         Relation.parent(X,Word1,Word2) <=  (Relation.r_type[X]=='rel:is_derived_from') & (Relation.second_word[X]==Word2) & (Relation.first_word[X]==Word1)

El motor lógico verificaría todas las filas donde se cumpla que la relación es is_derived_from de las cuáles existen más de dos millones de filas implicando mayor costo computacional. Todas las relaciones fueron construidas teniendo lo anterior en cuenta.

- Carga de idioma por idioma en las operaciones del tipo de comparación de idioma con idioma: En dichas operaciones se carga al KB todas las relaciones del segundo idioma, se realizan las operaciones, se vacía el KB y se cargan los del siguiente sucesivamente.


# Descripción de la distribución de trabajo

La siguiente fue la distribución del trabajo del grupo:

|Estudiante|Tareas|Calificación
|----------|------|------------
José Miguel Mora Rodríguez| Diseño de las operaciones lógicas, carga de tsv y creación de los objetos para agregar al kb, implementación de las operaciones de palabra con idioma e idioma con idioma| 100
Dylan Rodríguez Barboza| Diseño de las operaciones lógicas, carga de tsv y creación de objetos, diseño e implementación de la interfaz, conexión interfaz y lógica.
Karina Zeledón Pinell| Diseño de las operaciones lógicas, implementación de las operaciones de relación de parentezco, unit testing|100

