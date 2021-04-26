---
title: Práctica 6
layout: practice
permalink: /practice/6
---

# Trabajo Práctico 6

Debe entregarse en 15 días, luego del parcial.

## Ejercicio 1 - Loops and prints

Dado la siguiente consigna, implementar y lograr imprimir en pantalla el output esperado.

Para la primera parte, hacer un método llamado printList que dado una lista de Strings lo muestre por pantalla uno por renglón con su número de índice, un punto, un tabulado (\t) y el valor String (ejemplo: "0. DF"). Si el arreglo tiene strings vacíos no debe mostrar nada, ni el renglón correspondiente.

Para la segunda parte, hacer un método llamado printBackwards que dado una lista de strings lo muestre por pantalla uno por renglón, pero la palabra deberia ser imprimida al reves. Por ejemplo, si la palabra es "hola", se debera imprimir "aloh".

## Ejercicio 2

Dado la siguiente consigna, implementar las siguientes funciones:

* Método **indexOfByIndex** que retorne el índice de la primera ocurrencia de un String dentro de una lista de Strings, a partir 
  de un índice dado, incluido en la búsqueda. En caso de no encontrarse ninguna coincidencia retorna el valor -1.

* Método **indexOf** que retorne el índice de la primera ocurrencia de un String dentro de una lista de Strings. En caso 
  de no encontrarse ninguna retorna el valor -1.

* Método **indexOfEmpty** que retorne el índice del primer lugar “vacío” (igual a "") en una lista de Strings, que se le pasa como 
  argumento. De no encontrar ninguno que retorne -1.

* Método **put**, que dado un String y una lista de Strings lo coloque en el primer lugar vacío que encuentre y retorne 
  el índice en donde lo colocó y de no haber lugar retorne -1.

* Método **remove** que dado un String y una lista de Strings, busque el string y lo elimine si lo encuentra, y 
  retorne el número de eliminaciones que ha hecho.