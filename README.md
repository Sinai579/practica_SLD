# Sistema Experto en Gastronomía - Resolución SLD

Este proyecto implementa un **sistema experto en gastronomía** utilizando la técnica de **Resolución SLD (Selective Linear Definite-clause Resolution)**.  
El programa permite realizar consultas lógicas sobre una base de conocimiento que contiene **hechos** y **reglas**, aplicando conceptos de **inteligencia artificial simbólica**.

---

## Estructura del Proyecto

El sistema se compone de **dos archivos principales**:

- `main.py` → Contiene la implementación del motor SLD y la lógica principal.
- `base_conocimiento.py` → Define los **HECHOS** y **REGLAS** del dominio gastronómico (por ejemplo, ingredientes, tiempos de preparación, tipos de platillos, etc.).

---

## Cómo Ejecutar el Programa

1. Asegúrese de tener **Python 3.x** instalado (no se requiere ninguna librería externa).
2. Coloque ambos archivos (`main.py` y `base_conocimiento.py`) en la **misma carpeta**.
3. Abra una terminal o consola en esa carpeta.
4. Ejecute el programa con el siguiente comando:

   ```bash
   python main.py

## Funcionamiento del sistema

El programa se basa en el mecanismo de resolución lógica SLD, el cual busca demostrar consultas (queries) a partir de los hechos y reglas disponibles.

El flujo general es el siguiente:

- Consulta inicial
Se define una meta (por ejemplo, **("muy_picante", "enchiladas_verdes")**).

- Verificación directa en los hechos
Se comprueba si la meta coincide con algún hecho en la base de conocimiento.

- Aplicación de reglas
Si no se encuentra coincidencia directa, se buscan reglas cuya cabeza (head) coincida con la consulta.

    - Si se encuentra una, se resuelven las submetas (body) de forma recursiva.

- Unificación
El motor intenta igualar predicados, buscando sustituciones que hagan equivalentes los términos (por ejemplo, **?X = enchiladas_verdes**).

- Resultado
Si todas las submetas se satisfacen, la consulta se considera verdadera y se devuelve la sustitución resultante.

## Uso del for y recursividad

En el código original se utilizaron estructuras for para recorrer listas de hechos y reglas, sin embargo en comentariso de bloque se muestra el equivalente a si se hubiera hecho con recursividad:)
