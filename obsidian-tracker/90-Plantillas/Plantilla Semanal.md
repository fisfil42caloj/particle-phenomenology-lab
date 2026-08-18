---
semana: "{{date:gggg-[W]ww}}"
tipo: revision-semanal
---

# Revisión semana {{date:gggg-[W]ww}}

## Números de la semana

```dataview
TABLE WITHOUT ID
  file.link AS "Día",
  (default(min_cuantica,0)+default(min_em,0)+default(min_fismat,0)+default(min_mecanica,0)+default(min_optica,0)) AS "Estudio",
  choice(entreno, entreno_dia + " + " + entreno_finisher, "—") AS "Entreno",
  default(min_frances,0) AS "FR",
  default(min_ruso,0) AS "RU",
  default(sueno_h,"—") AS "Sueño"
FROM "10-Diario"
WHERE tipo = "diario" AND semana = this.semana
SORT fecha ASC
```

## Reparto de estudio por asignatura

```dataview
TABLE WITHOUT ID
  sum(rows.c) AS "Cuántica",
  sum(rows.e) AS "EM",
  sum(rows.f) AS "Fís. Mat.",
  sum(rows.m) AS "Mecánica",
  sum(rows.o) AS "Óptica"
FROM "10-Diario"
WHERE tipo = "diario" AND semana = this.semana
FLATTEN default(min_cuantica,0) AS c
FLATTEN default(min_em,0) AS e
FLATTEN default(min_fismat,0) AS f
FLATTEN default(min_mecanica,0) AS m
FLATTEN default(min_optica,0) AS o
GROUP BY true
```

## Tareas que quedaron pendientes

```dataview
TASK
FROM "10-Diario"
WHERE !completed AND semana = this.semana
```

## Preguntas de revisión
- ¿Qué asignatura se quedó corta y por qué?
- ¿El entrenamiento respetó el ciclo o se saltó algún día?
- ¿El ruso tuvo contacto diario (aunque fueran 10 min)?
- ¿Qué cambio concreto hago la semana que viene?

## Plan de la semana siguiente
- 
