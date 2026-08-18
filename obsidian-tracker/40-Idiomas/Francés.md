---
tipo: idioma
idioma: Francés
campo: min_frances
nivel:
objetivo:
estado: en consolidación
---

# 🇫🇷 Francés

> Es el que llevas mejor: aquí el objetivo no es empezar de cero sino **no perder terreno** y subir de nivel con contacto real (lectura, escucha, escritura), no con ejercicios de repaso.

## Nivel y objetivo
- Nivel actual: *(pendiente)*
- Objetivo para diciembre: *(pendiente)*
- ¿Examen oficial en el horizonte? *(pendiente)*

## Materiales en curso
| Tipo | Recurso | Estado |
|---|---|---|
| Lectura |  |  |
| Escucha |  |  |
| Gramática |  |  |
| Conversación |  |  |

## Vocabulario y expresiones
- 

## Minutos registrados

```dataview
TABLE WITHOUT ID
  file.link AS "Día",
  min_frances AS "Min"
FROM "10-Diario"
WHERE tipo = "diario" AND default(min_frances, 0) > 0
SORT fecha DESC
LIMIT 20
```

```dataview
TABLE WITHOUT ID
  key AS "Semana",
  sum(rows.m) AS "Min",
  length(filter(rows.m, (x) => x > 0)) AS "Días con contacto"
FROM "10-Diario"
WHERE tipo = "diario"
FLATTEN default(min_frances, 0) AS m
GROUP BY semana
SORT key DESC
LIMIT 10
```
