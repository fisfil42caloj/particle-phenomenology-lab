---
tipo: asignatura
asignatura: Física Matemática
campo: min_fismat
tag: fismat
curso: 3
periodo: 2026-09 / 2026-12
examen:
profesor:
creditos:
---

# Física Matemática

> Convocatoria: **enero de 2027** (fecha exacta pendiente → rellena `examen:` en el frontmatter con formato `2027-01-DD` y aparecerá la cuenta atrás en [[Panel Universidad]]).

## Temario
1. Variable compleja y teorema de los residuos
2. Series de Fourier y transformadas integrales
3. Ecuaciones diferenciales ordinarias y funciones especiales
4. Problemas de Sturm–Liouville
5. Funciones de Green
6. Ecuaciones en derivadas parciales de la física

## Bibliografía de referencia
- Arfken & Weber, *Mathematical Methods for Physicists*
- Riley, Hobson & Bence
- Butkov, *Mathematical Physics*

## Conceptos que tengo que dominar sí o sí
- 

## Dudas abiertas
> Cada duda que apuntes en un diario con `#fismat` aparece aquí hasta que la taches.

```dataview
TASK
FROM "10-Diario"
WHERE !completed AND contains(text, "#fismat")
```

## Horas registradas

```dataview
TABLE WITHOUT ID
  file.link AS "Día",
  min_fismat AS "Min"
FROM "10-Diario"
WHERE tipo = "diario" AND default(min_fismat, 0) > 0
SORT fecha DESC
LIMIT 25
```

```dataview
TABLE WITHOUT ID
  key AS "Semana",
  sum(rows.m) AS "Min",
  round(sum(rows.m) / 60, 1) AS "Horas"
FROM "10-Diario"
WHERE tipo = "diario"
FLATTEN default(min_fismat, 0) AS m
GROUP BY semana
SORT key DESC
LIMIT 10
```
