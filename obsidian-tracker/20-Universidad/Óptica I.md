---
tipo: asignatura
asignatura: Óptica I
campo: min_optica
tag: optica
curso: 3
periodo: 2026-09 / 2026-12
examen:
profesor:
creditos:
---

# Óptica I

> Convocatoria: **enero de 2027** (fecha exacta pendiente → rellena `examen:` en el frontmatter con formato `2027-01-DD` y aparecerá la cuenta atrás en [[Panel Universidad]]).

## Temario
1. Naturaleza de la luz y ecuaciones de ondas
2. Reflexión y refracción, ecuaciones de Fresnel
3. Óptica geométrica: matrices ABCD, sistemas ópticos
4. Interferencia
5. Difracción (Fraunhofer y Fresnel)
6. Polarización

## Bibliografía de referencia
- Hecht, *Óptica*
- Born & Wolf (consulta)
- Guenther, *Modern Optics*

## Conceptos que tengo que dominar sí o sí
- 

## Dudas abiertas
> Cada duda que apuntes en un diario con `#optica` aparece aquí hasta que la taches.

```dataview
TASK
FROM "10-Diario"
WHERE !completed AND contains(text, "#optica")
```

## Horas registradas

```dataview
TABLE WITHOUT ID
  file.link AS "Día",
  min_optica AS "Min"
FROM "10-Diario"
WHERE tipo = "diario" AND default(min_optica, 0) > 0
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
FLATTEN default(min_optica, 0) AS m
GROUP BY semana
SORT key DESC
LIMIT 10
```
