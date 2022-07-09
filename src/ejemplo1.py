"""
_______________________________________________________________________________________________________________________________
                                    
                                    EJEMPLO #1 DE WEB SCRAPING CON PYTHON --- BEAUTIFUL SOUP
_______________________________________________________________________________________________________________________________

                                                __________________

                                                TIPOS DE ELEMENTOS
                                                __________________

                                         Tag / Atributo / NavigableString
TAG:
    - Acceso mediante su nombre
    - Pueden contener atributos
        -> Acceso como si fuera un diccionario
        -> Atributo attrs
    - Propiedad string
"""

from bs4 import BeautifulSoup


# Abrimos el fichero html que vamos a utilizar
with open(r'C:\Users\Jhon\OneDrive - Universidad de Valladolid\AAAA_GitHub\Web Scraping - Python\Web_Scraping-Python\src\index.html') as file:
    html = file.read()

"""
Peticion con 'request' a una cierta pagina
r = requests.get('https://webPage.com')
"""

# Nodo raiz del arbol de objetos definido a partir del documento HTML
soup = BeautifulSoup(html, 'lxml')

# A partir del nodo raiz, se realizan consultas para obtener los datos que realmente queremos utilizar

# Acceso a la etiqueta titulo
print(soup.title)

# Accesso al contenido de la etiqueta titulo
print(soup.title.string, "\n")

# Acceso al encabezado h1
print(soup.h1.string, "\n")

# Acceso al primer enlace
print(soup.a['href'], "\n") # Como si fuese un diccionario

# Navegacion a traves de los nodos
print(soup.div.div.div) #¡¡¡PROBLEMA: de esta manera solo recuperamos el primer nodo del arbol!!!

