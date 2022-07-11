from bs4 import BeautifulSoup
import requests

#Link/Pagina de la que extraemos la data
web = 'https://subslikescript.com/movie/Titanic-120338'

#Peticion con 'request' a la pagina
respuesta = requests.get(web)

# Para obtener el texto del resultado utilizamos '.text'
text = respuesta.text # Obtencion del texto en BeautifulSoup

# Nodo raiz del arbol de objetos definido a partir del documento HTML
soup = BeautifulSoup(text, 'lxml')

# Mostrar el codigo HTML que hemos extraido de la pagina
"print(soup.prettify())"

"""
    #1 Imprimimos el titulo de la pelicula y el guion de la pelicula
"""

# Comenzamos obteniendo la caja que contiene el codigo que nos interesa
box = soup.find('article', class_= "main-article")

# Si hubiesen mas tag 'h1' fuera del cuadro que nos interesa, podemos obtener el titulo
# que deseamos de la siguiente manera
title = box.find('h1').get_text()
#print(title)

# Obtenemos el guion de la pelicula
script = box.find('div', class_= "full-script").get_text(strip=True, separator=' ')
# Para eliminar los espacios en blanco que haya al comienzo o final de cada frase utilizamos los parametros 'strip' y 'separator'
#print(script)


"""
    #2 Exportacion a un archivo .txt
"""
with open(f'{title}.txt', 'w', encoding = "utf-8") as file:
    file.write(script)