#Changelog

##[Versión 0.0.1] - 12/9/23

- Primera versión registrada con un changelog
- Se agregó 1 nuevo parámetro para la clase Board, el cuál puede retornar una lista con los puntos individuales de cada letra en una palabra escrita
- Se modificó el nombre de 2 funciones de la clase board, utilizando "verify" para hacer referencia a que las funciones verifican la existencia de la palabra en la matriz
- Se agregaron 3 nuevas funciones:
    - wordCurrentPoints: Esta función retorna la lista con los puntos individuales de la última palabra escrita en la matriz
    - writeVerticalWord: ESta función escribe en vertical en la matriz la palabra elegida (Aún no verificada, eso se realizará en futuras actualizaciones). Al escribir y sobreescribir las casillas o celdas, esta va calculando el valor de cada casilla, y multiplicando las letras indivuduales en caso de que caiga en una casilla de doble letra o triple letra
    - writeHorizontalWord: ESta función escribe en horizontal en la matriz la palabra elegida (Aún no verificada, eso se realizará en futuras actualizaciones). Al escribir y sobreescribir las casillas o celdas, esta va calculando el valor de cada casilla, y multiplicando las letras indivuduales en caso de que caiga en una casilla de doble letra o triple letra

##[Versión 0.0.2] - 12/9/23

- Se realizó un cambio donde los valores de las Tiles aparecian como una lista, se reemplazó por un diccionario para poder acceder más fácilemente a su valor individual
- Se añadió la letra K a la bolsa de letras para poder probar más combinaciones
- Se cambiaron test a la par de las funciones y se eliminaron otros, ya que hay algunas funciones que no tomarán el rumbo original que se tenía planeado para llevar a cabo el juego

##[Versión 0.0.3] - 14/9/23
    ##[Versión 0.0.3a] 14/9/23 
    - La función de escribir se unificó en una sola, que puede escribir tanto el vertical como en horizontal en la matriz
    - Se introdujo una manera de calcular las celdas y palabras, previamente se podían calcular las palabras dobles, ahora la función de escribir activa una condición cuando la palabra es doble o triple, si cae en un casillero de doble o triple palabra (La implementación de la próxima función llegará con la refactorización de la clase Cell, pero ya es funcional)

    ##[Versión 0.0.3b] 15/9/23
    - Se refactorizó la función de escribir en las celdas, reduciendo su complejidad