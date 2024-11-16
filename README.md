# Implementacion_a_epsilon
Este repositorio contiene el código de implementación del algoritmo A-epsilon aplicado al transporte de mercancías entre diferentes ubicaciones. Desarrollado como parte de un proyecto en **Inteligencia Artificial**, el objetivo de este proyecto es encontrar la ruta óptima para transportar productos desde el **Museo de Arte Moderno** hasta la **Estación de Transporte**, utilizando heurísticas ajustadas para optimizar el proceso de búsqueda.

## Descripción del Proyecto
El algoritmo A-epsilon es una variante del algoritmo A*, que combina el costo acumulado y la heurística estimada para encontrar el camino más eficiente en un grafo. En este caso, se aplica a un sistema de rutas entre diferentes ubicaciones dentro de una ciudad, tal como **Museo de Arte Moderno**, **Depósito Central**, **Galería Norte**, **Galería Sur**, **Centro de Restauración** y **Estación de Transporte**.

La implementación incluye la posibilidad de ajustar el valor de epsilon para experimentar con diferentes aproximaciones de búsqueda. Al variar el valor de epsilon, podemos influir en el balance entre la precisión de la heurística y el costo real de las rutas, permitiendo encontrar soluciones óptimas o subóptimas dependiendo del valor seleccionado.

## Objetivos del Proyecto
- Implementar el algoritmo A-epsilon para encontrar la ruta más eficiente entre el **Museo de Arte Moderno** y la **Estación de Transporte**.
- Comparar los resultados obtenidos para diferentes valores de epsilon (1 y 3).
- Mostrar la diferencia en el costo de las rutas encontradas utilizando A-epsilon con diferentes epsilon y cómo esto afecta la decisión entre rutas óptimas y subóptimas.
