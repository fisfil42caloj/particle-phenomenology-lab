---
tipo: panel
---

# 🗣️ Panel de idiomas

[[Francés]] · [[Ruso]]

## Últimos 14 días

```dataview
TABLE WITHOUT ID
  file.link AS "Día",
  default(min_frances,0) AS "🇫🇷 FR",
  default(min_ruso,0) AS "🇷🇺 RU"
FROM "10-Diario"
WHERE tipo = "diario"
SORT fecha DESC
LIMIT 14
```

## Constancia semanal

```dataview
TABLE WITHOUT ID
  key AS "Semana",
  sum(rows.fr) AS "FR min",
  length(filter(rows.fr, (x) => x > 0)) AS "FR días",
  sum(rows.ru) AS "RU min",
  length(filter(rows.ru, (x) => x > 0)) AS "RU días"
FROM "10-Diario"
WHERE tipo = "diario"
FLATTEN default(min_frances,0) AS fr
FLATTEN default(min_ruso,0) AS ru
GROUP BY semana
SORT key DESC
LIMIT 12
```

> En ruso la columna que importa es **RU días**, no **RU min**. Estando en la fase inicial, siete días de 15 minutos valen más que un atracón de dos horas: lo que estás construyendo es reconocimiento automático del alfabeto y del sonido, y eso se consolida con repetición espaciada, no con volumen.
>
> En francés puedes permitirte sesiones más largas y espaciadas, porque ya no estás automatizando nada básico.
