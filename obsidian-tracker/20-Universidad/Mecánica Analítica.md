---
tipo: asignatura
asignatura: Mecánica Analítica
campo: min_mecanica
tag: mecanica
curso: 3
periodo: 2026-09 / 2026-12
examen:
profesor:
creditos:
---

# Mecánica Analítica

> Convocatoria: **enero de 2027** (fecha exacta pendiente → rellena `examen:` en el frontmatter con formato `2027-01-DD` y aparecerá la cuenta atrás en [[Panel Universidad]]).

## Temario
1. Ligaduras y principio de d'Alembert
2. Formalismo lagrangiano
3. Simetrías y teorema de Noether
4. Fuerzas centrales y sólido rígido
5. Formalismo hamiltoniano y corchetes de Poisson
6. Transformaciones canónicas y Hamilton–Jacobi

## Bibliografía de referencia
- Goldstein, *Classical Mechanics*
- Landau & Lifshitz, *Mecánica*
- Taylor, *Classical Mechanics*

## Conceptos que tengo que dominar sí o sí
- 

## Dudas abiertas
> Cada duda que apuntes en un diario con `#mecanica` aparece aquí hasta que la taches.

```dataview
TASK
FROM "10-Diario"
WHERE !completed AND contains(text, "#mecanica")
```

## Horas registradas

```dataview
TABLE WITHOUT ID
  file.link AS "Día",
  min_mecanica AS "Min"
FROM "10-Diario"
WHERE tipo = "diario" AND default(min_mecanica, 0) > 0
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
FLATTEN default(min_mecanica, 0) AS m
GROUP BY semana
SORT key DESC
LIMIT 10
```
