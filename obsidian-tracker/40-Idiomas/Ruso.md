---
tipo: idioma
idioma: Ruso
campo: min_ruso
nivel: principiante
objetivo:
estado: fase inicial
---

# 🇷🇺 Ruso

> Recién empezado. En esta fase la métrica que importa **no son los minutos sino los días seguidos con contacto**: 15 min diarios rinden mucho más que dos horas el domingo. El alfabeto y la fonética son la inversión que desbloquea todo lo demás, así que van primero.

## Nivel y objetivo
- Nivel actual: principiante
- Objetivo para diciembre: *(pendiente)*

## Hitos de la fase inicial
- [ ] Alfabeto cirílico: leer en voz alta sin dudar
- [ ] Cursiva manuscrita (leerla, aunque sea a duras penas)
- [ ] Fonética: acentuación móvil y reducción vocálica (*аканье*)
- [ ] Los 6 casos: reconocerlos, aunque todavía no producirlos
- [ ] Presente de verbos: primera y segunda conjugación
- [ ] Aspecto verbal (imperfectivo/perfectivo): entender la idea
- [ ] Primeras 300 palabras de alta frecuencia

## Materiales en curso
| Tipo | Recurso | Estado |
|---|---|---|
| Manual |  |  |
| Audio |  |  |
| Tarjetas / SRS |  |  |

## Vocabulario
- 

## Minutos registrados

```dataview
TABLE WITHOUT ID
  file.link AS "Día",
  min_ruso AS "Min"
FROM "10-Diario"
WHERE tipo = "diario" AND default(min_ruso, 0) > 0
SORT fecha DESC
LIMIT 20
```

```dataview
TABLE WITHOUT ID
  key AS "Semana",
  sum(rows.m) AS "Min",
  length(filter(rows.m, (x) => x > 0)) AS "Días con contacto"
FROM "10-Diario"
WHERE tipo = "diario"
FLATTEN default(min_ruso, 0) AS m
GROUP BY semana
SORT key DESC
LIMIT 10
```
