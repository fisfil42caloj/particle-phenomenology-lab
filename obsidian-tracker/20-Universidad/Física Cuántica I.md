---
tipo: asignatura
asignatura: Física Cuántica I
campo: min_cuantica
tag: cuantica
curso: 3
periodo: 2026-09 / 2026-12
examen:
profesor:
creditos:
---

# Física Cuántica I

> Convocatoria: **enero de 2027** (fecha exacta pendiente → rellena `examen:` en el frontmatter con formato `2027-01-DD` y aparecerá la cuenta atrás en [[Panel Universidad]]).

## Temario
1. Crisis de la física clásica y postulados
2. Ecuación de Schrödinger y pozos en 1D
3. Formalismo: espacios de Hilbert, operadores, observables
4. Oscilador armónico
5. Momento angular y espín
6. Átomo de hidrógeno

## Bibliografía de referencia
- Griffiths, *Introduction to Quantum Mechanics*
- Sakurai, *Modern Quantum Mechanics* (consulta)
- Galindo & Pascual (formalismo)

## Conceptos que tengo que dominar sí o sí
- 

## Dudas abiertas
> Cada duda que apuntes en un diario con `#cuantica` aparece aquí hasta que la taches.

```dataview
TASK
FROM "10-Diario"
WHERE !completed AND contains(text, "#cuantica")
```

## Horas registradas

```dataview
TABLE WITHOUT ID
  file.link AS "Día",
  min_cuantica AS "Min"
FROM "10-Diario"
WHERE tipo = "diario" AND default(min_cuantica, 0) > 0
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
FLATTEN default(min_cuantica, 0) AS m
GROUP BY semana
SORT key DESC
LIMIT 10
```
