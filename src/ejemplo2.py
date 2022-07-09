"""
_______________________________________________________________________________________________________________________________
                                    
                                    EJEMPLO #2 DE WEB SCRAPING CON PYTHON --- BEAUTIFUL SOUP
_______________________________________________________________________________________________________________________________

                                                __________________

                                                    NAVEGACIÓN
                                                __________________

                                         
DESCENDIENTES (TAG):
    - contents: Lista con hijos de primer nivel.
    - children: Iterador con hijos de primer nivel.
    - descendant: Generador con todos los hijos.

ANCESTROS:
    - parent: Objeto padre.
    - parents: Generador con objetos padre.
"""

from bs4 import BeautifulSoup
import bs4


# Abrimos el fichero html que vamos a utilizar
with open(r'Web_Scraping-Python\src\index.html') as file:
    html = file.read()

# Nodo raiz del arbol de objetos definido a partir del documento HTML
soup = BeautifulSoup(html, 'lxml')

# A partir del nodo raiz, se realizan consultas para obtener los datos que realmente queremos utilizar

# Acceso a los hijos de primer nivel del bloque div.div.div
for d in soup.div.div.div.children:
    #Filtramos por elemento de tipo etiqueta
    if isinstance(d, bs4.element.Tag):
        print(d)


"""                                             __________________

                                                    BÚSQUEDAS
                                                __________________

                                         
BÚSQUEDAS :
    - find_all(): Lista de objetos.
    - find(): Un único elemento.

    Buscan entre los descendientes de un tag que cumplen un filtro:
     - Filtro por etiqueta
     - Filtro por atributos
     - Filtro por clases

     ¡Cuidado con los documentos GRANDES!
"""

# Busqueda para obtener todos los enlaces de un documento html
print(soup.find_all('a'))

# Obtener el bloque id = footer (1)
footer = soup.find(id='footer')
print("\n", footer)

# Obtener los bloques div con clase 'links' (2)
links = soup.find_all('div', class_='links') #Como la palabra class es una palabra reservada, se utiliza un guion final(_) para buscar.
print("\n", links)

# La diferencia entre las búsqueda anteriores es que de la primera forma (1) obtendriamos todas las etiquetas con clase 'links', sean o no sean bloques, mientras que
# de la menera (2), se obtiene solamente los bloques div con clase 'links'.