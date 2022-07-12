_author_ = 'Jhon'

from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader


""""
PROBLEMA: Extraer información de StackOverFlow - Preguntas
"""

# Definimos la estructura de nuestros Items: que es la información que queremos almacenar de cada uno de nuestros Items
class Pregunta(Item):
    pregunta = Field() # Objeto de tipo campo
    id = Field() # numero de la pregunta

# Implementacion del Spider
class StackOverFlowSpider(Spider): # Como vamos a extraer informacion de una sola pagina web utilizamos la clase Spider
        name = "PrimerSpider"
        start_urls = {'https://es.stackoverflow.com/?tags=python'}

        # Metodo parse
        def parse(self, response): # response: respuesta en formato xml de la url
            # Creamos un selector
            sel = Selector(response)

            #preguntas = sel.xpath('//div[@id="question-mini-list"]') # Ahora nuestro selector va a tener todas las preguntas en un solo elemento
            # Pero lo que queremos conseguir es que cada elemento de la lista 'preguntas' sea cada una de las preguntas

            # De esta manera seleccionamos todas las preguntas hijas, ya que todas tienen el formato div
            preguntas = sel.xpath('//div[@id="question-mini-list"]/div/div')

            # Iteramos sobre todas las preguntas - Enumarate para tener el id secuencial de cada pregunta
            for i, elem in enumerate(preguntas):
                # Creamos nuestro item
                item = ItemLoader(Pregunta(), elem)
                # Agregamos los campos mediante xpath y valor directo
                item.add_xpath('pregunta', './/div[@class="s-post-summary--content"]/h3/a/text()')
                item.add_value('id', i)

                yield item.load_item() # Escribe en la salida cada uno de los campos del Item
