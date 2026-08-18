---
tipo: panel
---

# 🏛️ Panel de universidad

## Cuenta atrás a enero

```dataview
TABLE WITHOUT ID
  file.link AS "Asignatura",
  examen AS "Examen",
  (date(examen) - date(today)).days AS "Días"
FROM "20-Universidad"
WHERE tipo = "asignatura" AND examen
SORT examen ASC
```

## Reparto de horas por asignatura (total del periodo)

```dataview
TABLE WITHOUT ID
  round(sum(rows.c)/60, 1) AS "Cuántica",
  round(sum(rows.e)/60, 1) AS "EM",
  round(sum(rows.f)/60, 1) AS "Fís. Mat.",
  round(sum(rows.m)/60, 1) AS "Mecánica",
  round(sum(rows.o)/60, 1) AS "Óptica"
FROM "10-Diario"
WHERE tipo = "diario"
FLATTEN default(min_cuantica,0) AS c
FLATTEN default(min_em,0) AS e
FLATTEN default(min_fismat,0) AS f
FLATTEN default(min_mecanica,0) AS m
FLATTEN default(min_optica,0) AS o
GROUP BY true
```

> Esta tabla es la que hay que mirar cada domingo. La asignatura que se queda corta tres semanas seguidas es la que te va a doler en enero.

## Últimos 7 días, por asignatura

```dataview
TABLE WITHOUT ID
  file.link AS "Día",
  default(min_cuantica,0) AS "Cuánt.",
  default(min_em,0) AS "EM",
  default(min_fismat,0) AS "F.Mat.",
  default(min_mecanica,0) AS "Mec.",
  default(min_optica,0) AS "Ópt."
FROM "10-Diario"
WHERE tipo = "diario" AND fecha >= date(today) - dur(7 days)
SORT fecha DESC
```

## Todas las dudas abiertas

```dataview
TASK
FROM "10-Diario"
WHERE !completed AND (contains(text, "#cuantica") OR contains(text, "#em") OR contains(text, "#fismat") OR contains(text, "#mecanica") OR contains(text, "#optica"))
```

## Asignaturas
- [[Física Cuántica I]]
- [[Electromagnetismo I]]
- [[Física Matemática]]
- [[Mecánica Analítica]]
- [[Óptica I]]
- [[Horario]] · [[Exámenes]]
