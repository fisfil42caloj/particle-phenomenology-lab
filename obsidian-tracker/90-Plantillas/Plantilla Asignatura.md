---
tipo: asignatura
codigo:
curso: 3
cuatrimestre: 1
periodo: 2026-09 / 2026-12
examen:
profesor:
creditos:
---

# 

## Temario
1. 

## Bibliografía
- 

## Mapa de conceptos
- 

## Problemas y entregas
```dataview
TASK
FROM "10-Diario" OR "20-Universidad"
WHERE !completed AND contains(text, this.file.name)
```

## Registro de horas

> Sustituye `min_XXX` por el campo de la asignatura (`min_cuantica`, `min_em`,
> `min_fismat`, `min_mecanica`, `min_optica`) y ponlo también en `campo:` arriba.

```dataview
TABLE WITHOUT ID
  file.link AS "Día",
  min_XXX AS "Min"
FROM "10-Diario"
WHERE tipo = "diario" AND default(min_XXX, 0) > 0
SORT fecha DESC
LIMIT 25
```
