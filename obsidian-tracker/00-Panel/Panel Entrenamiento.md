---
tipo: panel
---

# 🏋️ Panel de entrenamiento

Ciclo y patrón completo en [[Rutina]].

## Últimas sesiones

```dataview
TABLE WITHOUT ID
  file.link AS "Día",
  entreno_dia AS "Sesión",
  entreno_finisher AS "Finisher",
  default(entreno_rpe, "—") AS "RPE"
FROM "10-Diario"
WHERE tipo = "diario" AND entreno = true
SORT fecha DESC
LIMIT 15
```

**La última línea de esta tabla te dice cuál toca hoy**: avanza un paso en la lista de [[Rutina]] y cambia el finisher.

## Frecuencia por grupo muscular

```dataview
TABLE WITHOUT ID
  key AS "Sesión",
  length(rows) AS "Veces"
FROM "10-Diario"
WHERE tipo = "diario" AND entreno = true
GROUP BY entreno_dia
SORT length(rows) DESC
```

## Reparto del finisher

```dataview
TABLE WITHOUT ID
  key AS "Finisher",
  length(rows) AS "Veces"
FROM "10-Diario"
WHERE tipo = "diario" AND entreno = true
GROUP BY entreno_finisher
```

> Deberían quedar prácticamente empatados. Si el cuello se queda muy por detrás, es que se está cayendo al final de las sesiones largas.

## Entrenos por semana

```dataview
TABLE WITHOUT ID
  key AS "Semana",
  length(rows) AS "Entrenos"
FROM "10-Diario"
WHERE tipo = "diario" AND entreno = true
GROUP BY semana
SORT key DESC
LIMIT 12
```

## Sesiones detalladas
```dataview
LIST
FROM "30-Entrenamiento/Sesiones"
SORT file.name DESC
LIMIT 10
```
