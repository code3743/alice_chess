# Alice Chess IA

## Integrantes

- Pedro Bernal Londoño - 2259548
- Jota E. López - 2259394
- Esmeralda Rivas Guzmán - 2259580

## Descripción del Proyecto

Este proyecto implementa una inteligencia artificial para jugar ajedrez utilizando el motor `alicechess`, la IA se basa en el algoritmo **Minimax** con poda **Alpha-Beta**, que permite a la máquina tomar decisiones optimizadas en función de las jugadas posibles. A continuación, se describe cómo funciona la heurística utilizada para evaluar las posiciones y cómo esto ayuda en la toma de decisiones dentro del juego.

## Heurística Utilizada

La heurística es el conjunto de reglas o criterios que la IA usa para evaluar el valor de una posición en el tablero, en este caso, la evaluación de la posición se basa en varios factores, como el valor de las piezas, su posición en el tablero, y el desarrollo estratégico del juego.

### Componentes de la Heurística

1. **Valoración de las piezas**:
   Cada tipo de pieza tiene un valor básico, que varía dependiendo de su tipo, estos valores se modifican según su posición en el tablero. Las piezas tienen diferentes valores dependiendo de si están cerca del centro del tablero, de la parte trasera, o de otras piezas, este valor depende de una tabla de evaluación predefinida para cada tipo de pieza.

   - **Peón**: Su valor aumenta a medida que avanza en el tablero, con una bonificación por acercarse a la octava fila (donde puede ser promovido a otra pieza).
   - **Caballo**: Se favorece cuando está en el centro del tablero, ya que tiene más opciones de movimiento.
   - **Alfil**: Similar al caballo, con un enfoque en las posiciones más abiertas del tablero.
   - **Torre**: Se valora más en las filas y columnas abiertas, donde puede moverse más libremente.
   - **Reina**: Tiene un valor muy alto debido a su gran capacidad de movimiento. Su valoración depende de la proximidad al centro y su capacidad de controlar muchas casillas.
   - **Rey**: El rey tiene una valoración basada principalmente en su seguridad. Un rey expuesto es un signo de peligro, por lo que se valora más en las posiciones traseras.

2. **Tablas de Evaluación de Posición**:
   Cada pieza tiene una tabla que ajusta su valor dependiendo de su ubicación. Por ejemplo, los peones tienen una evaluación que varía según la fila en la que se encuentren, ya que las filas más cercanas a la octava fila (para el peón blanco) o primera fila (para el peón negro) tienen un valor mayor debido a la posibilidad de promoverse a una reina u otra pieza.

   - **Peón**: El valor de los peones depende de su cercanía a la octava fila, favoreciendo las posiciones avanzadas.
   - **Caballo, Alfil, Torre, Reina, y Rey**: Cada uno tiene tablas específicas que ajustan su valor dependiendo de su ubicación en el tablero. Por ejemplo, los caballos suelen ser más valiosos en el centro debido a su capacidad de moverse a muchas casillas.

3. **Evaluación General del Tablero**:
   La función `evaluate_board()` calcula el valor total de todas las piezas, considerando su tipo y su posición en el tablero. Este cálculo ayuda a determinar qué tan favorable o desfavorable es una posición para el jugador que está tomando el turno.

   El objetivo de la IA es maximizar su valoración mientras minimiza la del oponente, lo que se refleja en las decisiones tomadas por el algoritmo Minimax.

### Cómo la Heurística Ayuda en la Toma de Decisiones

La heurística ayuda a la IA a evaluar y decidir las jugadas más convenientes mediante el siguiente proceso:

1. **Exploración de Movimientos**: 
   La IA genera todas las jugadas posibles para una posición dada, para cada una de estas jugadas, evalúa la nueva posición del tablero utilizando la función de evaluación.

2. **Profundización**: 
   La IA no solo evalúa la jugada actual, sino que también simula las respuestas del oponente y sus posibles jugadas a futuro, el algoritmo Minimax explora hasta una profundidad de tres movimientos (esto puede ajustarse) para analizar las consecuencias de cada jugada. 

3. **Poda Alpha-Beta**:
   A medida que la IA explora las posibles jugadas, utiliza la poda Alpha-Beta para optimizar el proceso, esto significa que se descartan ciertas jugadas que no son útiles, lo que permite reducir el número de movimientos que deben analizarse y, por lo tanto, hacer que el proceso de decisión sea más rápido y eficiente.

4. **Selección de la Mejor Jugada**:
   Al final del proceso de exploración, la IA elige la jugada que tiene la mejor evaluación (máxima si está jugando como el jugador que maximiza, o mínima si está jugando como el oponente), esto asegura que la IA tome la decisión más favorable según su análisis de las posiciones.


## Referencias

- [Chess Variants](https://www.chessvariants.com/other.dir/alice.html)
- [Chess Programming Wiki](https://www.chessprogramming.org/Main_Page)
- [Alice Chess Engie](https://github.com/josephlou5/alicechess/)