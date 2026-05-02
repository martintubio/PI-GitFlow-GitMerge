# Git, GitMerge & GitFlow

## Descripción

Esta práctica tiene como objetivo aprender a trabajar con flujos de trabajo colaborativos en Git, concretamente con **GitFlow** y la resolución de **conflictos de merge**.

### ¿Qué se practica?

El repositorio simula un entorno de desarrollo real en el que dos ramas de funcionalidades (`feat/A` y `feat/B`) se desarrollan en paralelo a partir de una rama `develop` común:

- **`feat/A`** introduce descuentos porcentuales, cambia la estructura de los items y añade validaciones.
- **`feat/B`** añade persistencia en JSON, modifica la estructura de items y amplía `OrderManager` con nuevos métodos.

Al intentar mergear ambas ramas en `develop`, se producen **conflictos de merge** ya que ambas features modifican las mismas partes del código. El objetivo es resolverlos manualmente de forma coherente, de manera que el sistema final funcione correctamente y pase todos los tests.

### ¿Qué aprendí?

- Cómo estructurar un repositorio siguiendo la metodología **GitFlow** (ramas `main`, `develop` y `feat/*`).
- Cómo identificar, entender y resolver **conflictos de merge** en Git de forma manual.
- La importancia de los **tests automatizados** como criterio de corrección tras una integración: si los tests pasan, el merge es correcto.
- Cómo coordinar cambios paralelos que afectan a las mismas partes del código sin romper la funcionalidad existente.

### ¿Para qué sirve?

Este tipo de flujo de trabajo es el estándar en equipos de desarrollo profesionales. Saber gestionar ramas, integrar cambios y resolver conflictos es una habilidad fundamental para trabajar en proyectos colaborativos con control de versiones.


## Pruebas

Una vez mergeado, tendremos que ejecutar los tests con `python3 ./test_order_system.py`. So todo sale correcto, hemos terminado la práctica.

Ejecutar
```bash
python3 ./order_system.py
```

Tendríamos que ver que, tal como se puede esperar, que la salida debe ser 100 y además se escribe `orders.json` al disco.
