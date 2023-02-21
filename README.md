# Juego de la Vida de Conway
Juago de la vida de Conway por Juan José Creus Ramos (2019)

Este código fue un trabajo de universidad para la asignatura de Python.

El Juego de la Vida fue inventado por el matemático John Conway en 1970. Su objetivo era crear un sistema que simulase la vida y su naturaleza impredecible. La forma en la que representa la vida es muy sencilla. Una cuadrícula de células, algunas están vivas, otras están muertas. Cada célula tiene ocho células vecinas, en vertical, horizontal y en las diagonales. Este sistema aparentemente tan simple puede generar patrones complejos e impredecibles gracias a unas sencillas reglas.

Conway probó a aplicar muchas y distintas reglas, algunas hacían que las células murieran muy pronto y otras hacían que nunca murieran. Las reglas de la versión final del juego mantienen un equilibrio. Esto hace que, a simple vista, sea muy difícil saber si un grupo de células vivirán o morirán después de cierto tiempo.

![Vida](https://user-images.githubusercontent.com/108018294/220268369-6950df64-2ae8-49e3-b655-a0a63883755c.gif)

## Reglas
Las reglas del juego son las siguientes:

• Si una célula está viva y tiene dos o tres vecinas vivas, sobrevive.

• Si una célula está muerta y tiene tres vecinas vivas, nace.

• Si una célula está viva y tiene más de tres vecinas vivas, muere.


Este proceso se puede ejecutar de manera indefinida.



![Gospers_glider_gun](https://user-images.githubusercontent.com/108018294/220268857-a0cc4493-249d-41f7-a47a-760b2a6e36ac.gif)
