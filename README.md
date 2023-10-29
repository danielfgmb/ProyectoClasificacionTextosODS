# Proyecto Clasificacion Textos ODS

## Integrantes
- Daniel Fernando Gómez Barrera
- Lindsay Pinto
- Yei Hong Zhang

## Introducción

### Objetivos del Negocio

- El objetivo principal del proyecto es desarrollar un modelo de clasificación basado en técnicas de aprendizaje automático que permita relacionar automáticamente textos con los Objetivos de Desarrollo Sostenible (ODS) de la Agenda 2030 de la ONU.
- Crear una aplicación que facilite la interacción con los resultados del modelo, permitiendo a UNFPA interpretar y analizar la información textual recopilada en procesos de planeación participativa para el desarrollo a nivel territorial.
### Criterios de Éxito
- El modelo debe tener una alta precisión y recall en la clasificación de textos según los ODS, con métricas de evaluación superiores al 90%.
- La aplicación desarrollada debe ser intuitiva y eficiente en la presentación de resultados, lo que se reflejará en una alta tasa de adopción y satisfacción por parte de los usuarios de UNFPA.
### Descripción de los ODS involucrados y su impacto en Colombia
En el contexto de la Agenda 2030, los Objetivos de Desarrollo Sostenible (ODS) son metas globales que buscan abordar desafíos sociales, económicos y ambientales para lograr un mundo más equitativo y sostenible. Para este proyecto, es esencial identificar los ODS específicos que se abordarán:
- ODS 6 - Agua Limpia y Saneamiento: Este ODS se centra en garantizar la disponibilidad y gestión sostenible del agua y el saneamiento para todos. En Colombia, abordar este objetivo puede tener un impacto significativo en la calidad de vida de las comunidades, especialmente en áreas donde el acceso al agua potable y saneamiento básico es limitado.
- ODS 7 - Energía Asequible y No Contaminante: Este ODS busca asegurar el acceso a una energía asequible, fiable, sostenible y moderna para todos. En Colombia, abordar este objetivo puede contribuir a la mejora de la infraestructura energética y a la reducción de la dependencia de fuentes contaminantes.
- ODS 16 - Paz, Justicia e Instituciones Sólidas: Este ODS tiene como objetivo promover sociedades pacíficas e inclusivas para el desarrollo sostenible, proporcionar acceso a la justicia para todos y construir instituciones eficaces, responsables e inclusivas a todos los niveles. En Colombia, este ODS es especialmente relevante para fortalecer el sistema de justicia y promover la paz en áreas afectadas por conflictos.

## Despligue de Aplicación

Antes de iniciar se recomienda crear un entorno virtual y activarlo.
```bash
python -m venv venv
venv\Scripts\activate
```
Antes de iniciar la aplicación debe instalar todos los paquetes de Python requeridos. En la carpeta base se encuentra un archivo con todos los paquetes necesarios. Para instalarlos utilice el siguiente comando.

```bash
pip install requirements.txt
```
La aplicacion está diseñada en Django. Por lo que deberá estar en la carpeta base del repositorio y ejecutar el siguiente comando para correr el servidor.
```bash
python manage.py runserver
```
Por defecto el servidor corre en el puerto 8000. Si está corriendo en localhost verifique en la siguiente dirección http://localhost:8000/




