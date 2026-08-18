---
tipo: panel
---

# 🧭 Panel diario

## Hoy
```dataview
LIST
FROM "10-Diario"
WHERE tipo = "diario" AND fecha = date(today)
```

## Tareas abiertas (últimos 14 días)
```dataview
TASK
FROM "10-Diario"
WHERE !completed AND fecha >= date(today) - dur(14 days)
SORT fecha DESC
```

## Últimas dos semanas de un vistazo

```dataview
TABLE WITHOUT ID
  file.link AS "Día",
  (default(min_cuantica,0)+default(min_em,0)+default(min_fismat,0)+default(min_mecanica,0)+default(min_optica,0)) AS "Estudio",
  choice(entreno, entreno_dia + " + " + entreno_finisher, "—") AS "Entreno",
  default(min_frances,0) AS "FR",
  default(min_ruso,0) AS "RU",
  default(sueno_h,"—") AS "Sueño",
  default(energia,"—") AS "Energía"
FROM "10-Diario"
WHERE tipo = "diario"
SORT fecha DESC
LIMIT 14
```

## Resumen por semana

```dataview
TABLE WITHOUT ID
  key AS "Semana",
  sum(rows.est) AS "Estudio (min)",
  round(sum(rows.est)/60, 1) AS "Horas",
  length(filter(rows.ent, (x) => x = true)) AS "Entrenos",
  sum(rows.idi) AS "Idiomas (min)"
FROM "10-Diario"
WHERE tipo = "diario"
FLATTEN (default(min_cuantica,0)+default(min_em,0)+default(min_fismat,0)+default(min_mecanica,0)+default(min_optica,0)) AS est
FLATTEN default(entreno, false) AS ent
FLATTEN (default(min_frances,0)+default(min_ruso,0)) AS idi
GROUP BY semana
SORT key DESC
LIMIT 12
```

## Accesos
- [[Horario]] · [[Exámenes]] · [[Rutina]]
- [[Panel Universidad]] · [[Panel Entrenamiento]] · [[Panel Idiomas]]
