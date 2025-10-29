# Sistema Experto en Gastronomía - Resolución SLD

Este proyecto implementa un **sistema experto en gastronomía** utilizando la técnica de **Resolución SLD (Selective Linear Definite-clause Resolution)**.  
El programa permite realizar consultas lógicas sobre una base de conocimiento que contiene **hechos** y **reglas**.

Sinai Cabrera Retana 22760579
Pertenezco al equipo 4: "Gastronomía"
Y las leyes y hechos utilizados son los siguientes:
   Leyes:
   Una receta es muy picante si contiene chile habanero, secos, pasilla 
   Una receta ligera es aquella con tiempo de preparación menor a 40 minutos.
   Hechos:
-    ("incluye", "tostadas_de_tinga", "pollo_desmenuzado"),
-    ("incluye", "tostadas_de_tinga", "tostadas"),
-    ("incluye", "tostadas_de_tinga", "jitomates"),
-    ("incluye", "tostadas_de_tinga", "cebolla"),
-    ("incluye", "tostadas_de_tinga", "ajo"),
-    ("incluye", "tostadas_de_tinga", "lechuga"),
-    ("incluye", "tostadas_de_tinga", "chile_chipotle"),
-    ("incluye", "flautas_de_pollo", "pollo_desmenuzado"),
-    ("incluye", "flautas_de_pollo", "tortillas_de_maíz"),
-    ("incluye", "flautas_de_pollo", "lechuga"),
-    ("incluye", "flautas_de_pollo", "jitomate"),
-    ("incluye", "fajitas_de_pollo", "pollo"),
-    ("incluye", "fajitas_de_pollo", "tortillas_de_maíz"),
-    ("incluye", "fajitas_de_pollo", "pimiento_rojo"),
-    ("incluye", "fajitas_de_pollo", "pimiento_verde"),
-    ("incluye", "fajitas_de_pollo", "cebolla"),
-    ("incluye", "sopes_mexicanos", "carne_deshebrada"),
-    ("incluye", "sopes_mexicanos", "masa_de_maíz"),
-    ("incluye", "sopes_mexicanos", "lechuga"),
-    ("incluye", "sopes_mexicanos", "jitomate"),
-    ("incluye", "enchiladas_verdes", "pollo_desmenuzado"),
-    ("incluye", "enchiladas_verdes", "tortillas_de_maíz"),
-    ("incluye", "enchiladas_verdes", "tomates_verdes"),
-    ("incluye", "enchiladas_verdes", "chile_jalapeño"),
-    ("incluye", "enchiladas_verdes", "cebolla"),
-    ("incluye", "enchiladas_verdes", "cilantro"),
-    ("incluye", "pechuga_empanizada", "pechugas_de_pollo"),
-    ("incluye", "pechuga_empanizada", "harina"),
-    ("incluye", "pechuga_empanizada", "pan_molido"),
-    ("incluye", "pechuga_empanizada", "lechuga"),
-    ("incluye", "pechuga_empanizada", "jitomate"),
-    ("incluye", "chiles_rellenos", "carne_molida (picadillo)"),
-    ("incluye", "chiles_rellenos", "harina"),
-    ("incluye", "chiles_rellenos", "chiles_poblanos"),
-    ("incluye", "chiles_rellenos", "jitomate"),
-    ("incluye", "chiles_rellenos", "ajo"),
-    ("incluye", "chiles_rellenos", "cebolla"),
-    ("incluye", "milanesa_de_res_con_ensalada", "milanesas_de_res"),
-    ("incluye", "milanesa_de_res_con_ensalada", "pan_molido"),
-    ("incluye", "milanesa_de_res_con_ensalada", "lechuga"),
-    ("incluye", "milanesa_de_res_con_ensalada", "jitomate"),
-    ("incluye", "milanesa_de_res_con_ensalada", "pepino"),
-    ("incluye", "pollo_con_brocoli_y_zanahoria", "pechuga_de_pollo"),
-    ("incluye", "pollo_con_brocoli_y_zanahoria", "brócoli"),
-    ("incluye", "pollo_con_brocoli_y_zanahoria", "zanahoria"),
-    ("incluye", "pollo_con_brocoli_y_zanahoria", "cebolla"),
-    ("incluye", "tortitas_de_atun_en_salsa", "atun_en_lata"),
-    ("incluye", "tortitas_de_atun_en_salsa", "huevo"),
-    ("incluye", "tortitas_de_atun_en_salsa", "pan_molido"),
-    ("incluye", "tortitas_de_atun_en_salsa", "jitomates"),
-    ("incluye", "tortitas_de_atun_en_salsa", "cebolla"),
-    ("incluye", "tortitas_de_atun_en_salsa", "ajo"),
-    ("incluye", "tortitas_de_atun_en_salsa", "chile_serrano"),
-    ("incluye", "tortitas_de_atun_en_salsa", "perejil"),
   ### Tiempos de preparación en minutos
-    ("tiempo_preparacion", "chilaquiles_verdes", 40),
-    ("tiempo_preparacion", "arroz_con_pollo", 50),
-    ("tiempo_preparacion", "tacos_carne_asada", 30),
-    ("tiempo_preparacion", "ceviche", 20),
-    ("tiempo_preparacion", "tamales", 90),
-    ("tiempo_preparacion", "carne_de_res_salteada", 30),
-    ("tiempo_preparacion", "enchiladas_rojas", 45),
-    ("tiempo_preparacion", "tacos_al_pastor", 60),
-    ("tiempo_preparacion", "quesadillas_flor_calabaza", 30),
-    ("tiempo_preparacion", "enchiladas_vegetarianas", 45),
-    ("tiempo_preparacion", "tacos_de_champiñones", 25),
-    ("tiempo_preparacion", "tacos_de_lentejas", 40),
-    ("tiempo_preparacion", "pimiento_relleno", 50),
-    ("tiempo_preparacion", "sopa_de_tortilla", 35),
-    ("tiempo_preparacion", "molinetes_mexicanos", 30),
-    ("tiempo_preparacion", "ceviche_de_mango", 20),
-    ("tiempo_preparacion", "picadillo_de_soya_mexicano", 25),
-    ("tiempo_preparacion", "tortitas_de_papa_rellena", 50),
-    ("tiempo_preparacion", "calabacitas_al_horno", 40),
-    ("tiempo_preparacion", "coctel_de_camaron", 40),
-    ("tiempo_preparacion", "ensalada_de_quinoa", 25),
-    ("tiempo_preparacion", "curry_de_garbanzos", 40),
-    ("tiempo_preparacion", "hamburguesas_de_frijol_negro", 50),
-    ("tiempo_preparacion", "spaghetti_con_pure_de_berenjena", 35),
-    ("tiempo_preparacion", "enchiladas_de_queso", 45),
-    ("tiempo_preparacion", "omelette_de_espinaca_y_champiñones", 25),
-    ("tiempo_preparacion", "lasagna_de_vegetales", 60),
-    ("tiempo_preparacion", "sopa_de_brocoli_y_queso", 30),
-    ("tiempo_preparacion", "mole poblano", 180),
-    ("tiempo_preparacion", "pozole", 120),
-    ("tiempo_preparacion", "chiles en nogada", 150),
-    ("tiempo_preparacion", "cochinita pibil", 240),
-    ("tiempo_preparacion", "birria", 300),
-    ("tiempo_preparacion", "huevos rancheros", 30),
-    ("tiempo_preparacion", "caldo de res", 120),
-    ("tiempo_preparacion", "chicharrón en salsa verde", 45),
-    ("tiempo_preparacion", "tacos de pescado", 40),
-    ("tiempo_preparacion", "albóndigas en chipotle", 60),
-    ("tiempo_preparacion", "tostadas_de_tinga", 35),
-    ("tiempo_preparacion", "flautas_de_pollo", 40),
-    ("tiempo_preparacion", "fajitas_de_pollo", 30),
-    ("tiempo_preparacion", "sopes_mexicanos", 40),
-    ("tiempo_preparacion", "enchiladas_verdes", 50),
-    ("tiempo_preparacion", "pechuga_empanizada", 30),
-    ("tiempo_preparacion", "chiles_rellenos", 60),
-    ("tiempo_preparacion", "milanesa_de_res_con_ensalada", 40),
-    ("tiempo_preparacion", "pollo_con_brocoli_y_zanahoria", 35),
-    ("tiempo_preparacion", "tortitas_de_atun_en_salsa", 40),
 ### Chiles poco picantes
-    ("chile_poco", "chile_jalapeno"),
-    ("chile_poco", "chile_poblano"),
-    ("chile_poco", "aji_amarillo"),
 ### Chiles picantes
-    ("chile_picante", "chile_serrano"),
-    ("chile_picante", "chile_guajillo"),
-    ("chile_picante", "chile_ancho"),
-    ("chile_picante", "chile_mulato"),
   


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

- Consulta inicial: 
Se define una meta (por ejemplo, **("muy_picante", "enchiladas_verdes")**).

- Verificación directa en los hechos: 
Se comprueba si la meta coincide con algún hecho en la base de conocimiento.

- Aplicación de reglas: 
Si no se encuentra coincidencia directa, se buscan reglas cuya cabeza (head) coincida con la consulta.

    - Si se encuentra una, se resuelven las submetas (body) de forma recursiva.

- Unificación: 
El motor intenta igualar predicados, buscando sustituciones que hagan equivalentes los términos (por ejemplo, **?X = enchiladas_verdes**).

- Resultado: 
Si todas las submetas se satisfacen, la consulta se considera verdadera y se devuelve la sustitución resultante.

## Uso del for y recursividad

En el código original se utilizaron estructuras for para recorrer listas de hechos y reglas, sin embargo en comentarios de bloque se muestra el equivalente a si se hubiera hecho con recursividad:)
