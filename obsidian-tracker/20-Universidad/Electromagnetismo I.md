---
tipo: asignatura
asignatura: Electromagnetismo I
campo: min_em
tag: em
curso: 3
periodo: 2026-09 / 2026-12
examen:
profesor:
creditos:
---

# Electromagnetismo I

> Convocatoria: **enero de 2027** (fecha exacta pendiente → rellena `examen:` en el frontmatter con formato `2027-01-DD` y aparecerá la cuenta atrás en [[Panel Universidad]]).

## Temario
1. Electrostática en el vacío
2. Métodos de resolución: imágenes, separación de variables, multipolos
3. Medios dieléctricos
4. Magnetostática
5. Medios magnéticos
6. Inducción y ecuaciones de Maxwell

## Bibliografía de referencia
- Griffiths, *Introduction to Electrodynamics*
- Jackson, *Classical Electrodynamics* (consulta)
- Reitz–Milford–Christy

## Conceptos que tengo que dominar sí o sí
- 

## Dudas abiertas
> Cada duda que apuntes en un diario con `#em` aparece aquí hasta que la taches.

```dataview
TASK
FROM "10-Diario"
WHERE !completed AND contains(text, "#em")
```

## Horas registradas

```dataview
TABLE WITHOUT ID
  file.link AS "Día",
  min_em AS "Min"
FROM "10-Diario"
WHERE tipo = "diario" AND default(min_em, 0) > 0
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
FLATTEN default(min_em, 0) AS m
GROUP BY semana
SORT key DESC
LIMIT 10
```
