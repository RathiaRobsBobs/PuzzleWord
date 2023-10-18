# PuzzleWord

Juego educativo basado en teoría de conjuntos y el concepto de permutación para mejorar la construcción de oraciones coherentes.

## Descripción del proyecto

PuzzleWord se desarrolló utilizando el lenguaje de programación Python en el entorno de desarrollo Visual Studio Code, haciendo uso de diversas bibliotecas estándar de Python, como itertools, os, random y time. El proyecto, denominado "PUZZLEWORD", se centra en la creación de un juego educativo diseñado para ayudar a los jugadores a comprender y practicar la construcción de oraciones coherentes a partir de palabras desordenadas. Así pues, aborda un problema de la vida real relacionado con la comprensión y construcción de oraciones correctamente estructuradas en un idioma brindando una solución interactiva y divertida.

## Funcionalidades del proyecto

- Los usuarios que serán hostings del juego pueden ingresar conjuntos de palabras.
- El juego genera permutaciones de las palabras en cada conjunto y permite al hosting establecer las respuestas correctas.
- Los jugadores deben seleccionar las permutaciones correctas para formar oraciones coherentes.
- Se proporciona retroalimentación inmediata sobre el desempeño del jugador tras marcar una respuesta.
- El juego calcula una puntuación final basada en el número de aciertos y se muestran sus errores y aciertos.

## Problema

El problema que aborda este proyecto radica en la dificultad que enfrentan las personas que están aprendiendo un nuevo idioma o que tienen desafíos en la comprensión de la gramática para construir oraciones coherentes a partir de palabras desordenadas. Esta problemática es especialmente relevante en el contexto de la enseñanza y el aprendizaje de idiomas, donde la práctica constante y efectiva es fundamental para el desarrollo de habilidades lingüísticas sólidas.

El problema que aborda este proyecto radica en la dificultad que enfrentan las personas que están aprendiendo un nuevo idioma o que tienen desafíos en la comprensión de la gramática para construir oraciones coherentes a partir de palabras desordenadas. Esta problemática es especialmente relevante en el contexto de la enseñanza y el aprendizaje de idiomas, donde la práctica constante y efectiva es fundamental para el desarrollo de habilidades lingüísticas sólidas.

PuzzleWord aborda este problema de la vida real al proporcionar a las personas, en particular a aquellos que aprenden español como idioma no nativo, una herramienta efectiva para mejorar su gramática y comprensión lectora. Al enfrentarse al desafío de organizar palabras en oraciones coherentes, los jugadores deben comprender las reglas gramaticales y sintácticas del español. Esto es esencial para estudiantes de idiomas extranjeros y personas que desean fortalecer sus habilidades de escritura y comunicación en español.

La falta de ejercicios prácticos y entretenidos que aborden este problema de manera efectiva puede obstaculizar el progreso en el aprendizaje de un idioma, lo que justifica la necesidad de una solución educativa que sea tanto informativa como atractiva.

Además, "PUZZLEWORD" ofrece una solución versátil al permitir que el anfitrión o hosting del juego establezca criterios específicos para las combinaciones correctas. Esto significa que el juego se adapta a diferentes niveles de habilidad y necesidades educativas. Los criterios  pueden incluir la identificación de oraciones con hipérbaton (figura literaria que involucra el desorden de la estructura estándar de una oración: artículo + sustantivo + verbo + objeto directo + complementos), por ejemplo, o la selección de oraciones donde ciertas palabras estén en posiciones particulares. Esta flexibilidad facilita la adaptación del juego a entornos educativos y de práctica.

Por último, el juego ofrece retroalimentación inmediata sobre el desempeño del jugador. Al ver los resultados al final del juego, los jugadores pueden evaluar su comprensión y progreso, lo que es esencial para el aprendizaje autodirigido.

## Objetivos

### Objetivo general

El objetivo general de este proyecto es desarrollar un juego educativo basado en permutaciones, utilizando la técnica de matemática discreta, que mejore la capacidad de los usuarios para construir oraciones coherentes a partir de palabras desordenadas. Este juego tiene como propósito principal proporcionar una solución efectiva y entretenida para abordar la problemática de la construcción de oraciones en contextos de aprendizaje de idiomas y gramática.

### Objetivos específicos

- Implementar un generador de opciones que tome los conjuntos de palabras proporcionados por el usuario y genere las múltiples permutaciones posibles. Estas combinaciones servirán como desafíos para los jugadores y deben ser presentadas de manera aleatoria y variada.
- Desarrollar un sistema de evaluación que permita al juego verificar las respuestas proporcionadas por el usuario. Esto implica la comparación de las selecciones del jugador con las respuestas correctas establecidas previamente para determinar si son correctas o incorrectas.
- Facilitar la autoevaluación y retroalimentación al jugador. Al proporcionar retroalimentación inmediata sobre el desempeño del jugador y mostrar la puntuación final, se fomenta el aprendizaje autodirigido y la mejora continua de las habilidades lingüísticas en español.
- Permitir que el juego se adapte a diferentes niveles de habilidad y necesidades educativas. Esto implica la capacidad de configurar desafíos específicos, como identificar oraciones con estructuras gramaticales particulares o seleccionar oraciones donde ciertas palabras estén en posiciones específicas, lo cual será posible mediante el previo establecimiento de las respuestas correctas por parte del anfitrión y el informe de las reglas hacia los que jugarán.

## Meta

La meta principal es mejorar la habilidad de los usuarios para construir oraciones coherentes a partir de palabras desordenadas en al menos un 60%. Esto podría medirse a través de un seguimiento del progreso de los usuarios por parte de los anfitriones a medida que avanzan en el juego y adquieren experiencia en la construcción de oraciones correctamente  estructuradas.

## Prerrequisitos

Este programa utiliza funcionalidades específicas de la terminal interactiva, como: **`os.system('cls'  if os.name == 'nt'  else  'clear')`**, para limpiar la pantalla de la terminal antes de mostrar la siguiente salida. Por lo que no se ejecutará correctamente en Google Colab u otros entornos que carezcan de una terminal interactiva. Se recomienda ejecutar este programa en un entorno local de Python.

<img width="826" alt="image" src="Vista previa.png">



