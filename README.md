# Web Scraping - Python
Web Scraping en Python (Introducción)

## ¿Qué es Web Scraping?
Es una técnica que permite extraer datos e información de una web de manera automatizada.

## Campos de aplicación
Técnica utilizada especialmente en las primeras fases de proyectos relacionados con:
- **Big Data**
- **Machine Learning**
- **Análisis de datos**
- **NLP**

### Reputación online, Análisis de Tendencias

## Técnica
- Petición URL
- Obtener el HTML (contenido)
- Analizar el contenido (etiquetas, atributos)
- Extraer datos (Navegación + consultas)
- Procesamiento de los datos

## Buenas prácticas
- **Bots legítimos**
  - Identificarnos como un bot **User-Agent**
  - No bloquear el sitio web
  - Respetar el archivo *robots.txt*
 - **Usar un API siempre que esté disponible**
    - Uniformidad de los datos (JSON, XML, ...)
    - Documentación
    - Independencia de cambios en la web
    - No influye en las estadísticas de uso del sitio


## Beautiful Soup
- **Librería (HTML, XML)**
- Especificar un  parser. Transforma el doc en un **árbol de objetos Python (lxml)**
- En combinación con **request**

### Instalación de Beautiful Soup
```python
pip install beautifulsoup4
pip install lxml
pip install requests
```

## Scrapy
Es un Framework open-source de Python que permite realizar web scraping.

