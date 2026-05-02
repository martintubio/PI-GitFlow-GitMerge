# Git, GitMerge & GitFlow

Ahora vamos a mergear feat/B sobre develop. Esto nos va a dar merge conflicts. Solucionémoslos.

Una vez mergeado, tendremos que ejecutar los tests con `python3 ./test_order_system.py`. So todo sale correcto, hemos terminado la práctica.

Ejecutar
```bash
python3 ./order_system.py
```

Tras entender el código, tendríamos que ver que, tal como se puede esperar, debe dar 100 y además se escribe `orders.json` al disco.

Ahora, mergeamos la rama `feat/B`.