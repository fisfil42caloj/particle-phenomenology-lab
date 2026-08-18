---
tipo: examenes
convocatoria: enero 2027
---

# Exámenes — convocatoria de enero 2027

> Rellena el campo `examen:` de cada asignatura (formato `2027-01-DD`) y esta cuenta atrás se completa sola.

## Cuenta atrás

```dataview
TABLE WITHOUT ID
  file.link AS "Asignatura",
  examen AS "Fecha",
  (date(examen) - date(today)).days AS "Días"
FROM "20-Universidad"
WHERE tipo = "asignatura" AND examen
SORT examen ASC
```

## Sin fecha todavía

```dataview
LIST
FROM "20-Universidad"
WHERE tipo = "asignatura" AND !examen
```

## Plan de repaso
Con el semestre de septiembre a diciembre y los exámenes en enero, el reparto que funciona es:

- **Septiembre–diciembre**: seguimiento al día, sin acumular. La métrica que importa es *problemas resueltos por tema*, no horas leídas.
- **Última semana de diciembre**: cerrar temario. Ninguna asignatura debería llegar a enero con temas sin tocar.
- **Enero**: repaso por bloques + exámenes resueltos de años anteriores. Prioriza en orden inverso a la fecha del examen, pero **empieza por la que peor lleves**, no por la primera que caiga.

### Estado por asignatura
| Asignatura | Temario cubierto | Problemas hechos | Confianza (1-5) |
|---|---|---|---|
| [[Física Cuántica I]] |  |  |  |
| [[Electromagnetismo I]] |  |  |  |
| [[Física Matemática]] |  |  |  |
| [[Mecánica Analítica]] |  |  |  |
| [[Óptica I]] |  |  |  |
