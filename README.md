# Laberinto

Dirección del respositorio: [laberinto.git](https://github.com/LeonardoLLP/laberinto)

El código se divide en dos partes. En primer lugar, creamos el laberinto con muros en las coordenadas dadas.
Por otro lado, programamos un "personaje", un referente que va a ir moviéndose por el laberinto y probando los distintos caminos hasta llegar al final.
Una vez hecho esto, solo queda convertir los distintos movimientos del "personaje" y traducirlos a lenguaje comprensible.

Por otro lado, el diagrama de flujo es el siguiente:

<br>
<img height="800" src="https://github.com/LeonardoLLP/laberinto/blob/main/laberinth_true.drawio.png" />
<br>

Antes de mostrar el código, queda relatar un defecto que no me ha dado tiempo a resolver. Aunque el código actual consigue llegar al final, no muestra el camino más corto siempre. He reflexionado un poco acerca de ello y he llegado a dos soluciones. La primera, solución propia, consiste en realizar otra lista junto a las direcciones de las casilas de las coordenadas por las que va pasando el personaje. Cuando el jugador pase otra vez por la misma casilla, significará que el recorrido que ha hecho hasta entonces ha sido en vano, por lo que se podrá borrar todas las instrucciones hechas hasta esa casilla.

El segundo método, fruto de la investigación, consiste en utilizar un método de "pathfinding", usado hoy en día para controlar IAs en videojuegos y simulaciones. Este método encontraría directamente el camino más corto, y podría resolver también "laberintos dentro de laberinto", problema comentado en el código. Aquí dejo un vídeo que me llamó mucho la atención en referencia al pathfinding.
https://www.youtube.com/watch?v=-L-WgKMFuhE&t=501s&ab_channel=SebastianLague

Ambos métodos podrían implementarse en el código, y el primero con mucha facilidad (el segundo requeriría de un poco de investigación), pero con motivos de tiempo no se ha hecho (y el laberinto a resolver es muy sencillo).

A continuación, el código completo.

