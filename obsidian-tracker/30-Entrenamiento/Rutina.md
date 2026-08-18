---
tipo: rutina
ciclo: Espalda / Brazos / Pecho / Brazos / Pierna
finisher: Abdomen ↔ Cuello (alterna cada sesión)
estado: esqueleto - faltan ejercicios
---

# Rutina

## El ciclo

Cinco sesiones rotativas, sin días fijos de la semana:

1. **Espalda**
2. **Brazos**
3. **Pecho**
4. **Brazos**
5. **Pierna**

Y al final de cada sesión, un finisher que alterna **Abdomen ↔ Cuello**.

## Ojo: el ciclo real es de 10 sesiones, no de 5

Como el ciclo de músculos tiene 5 sesiones (impar) y el finisher alterna cada 2, el emparejamiento se desplaza en cada vuelta. El patrón completo no se repite hasta la sesión 11:

| # | Día | Finisher |
|---|---|---|
| 1 | Espalda | Abdomen |
| 2 | Brazos | Cuello |
| 3 | Pecho | Abdomen |
| 4 | Brazos | Cuello |
| 5 | Pierna | Abdomen |
| 6 | Espalda | Cuello |
| 7 | Brazos | Abdomen |
| 8 | Pecho | Cuello |
| 9 | Brazos | Abdomen |
| 10 | Pierna | Cuello |

Es una buena propiedad, no un fallo: en 10 sesiones cada grupo muscular recibe los dos finishers, así que ni el abdomen ni el cuello caen siempre después del mismo día pesado. Abdomen y cuello salen 5 y 5.

**Reparto por vuelta de 10:** Brazos ×4, Espalda ×2, Pecho ×2, Pierna ×2.

Dos cosas que el patrón implica, por si te sirven cuando me pases los ejercicios:
- Los brazos llevan el doble de frecuencia que el resto. Intencionado o no, conviene que lo sepas.
- Espalda→Brazos encadena bíceps dos sesiones seguidas, y Pecho→Brazos encadena tríceps. Si notas que el segundo día de brazos rinde peor, ahí está la causa probable.

## Ejercicios

> ⚠️ **Pendiente**: me dijiste que los detalles vienen después. Cuando me los pases relleno estas tablas y añado la progresión de cargas.

### Espalda
| Ejercicio | Series | Reps | Notas |
|---|---|---|---|
|  |  |  |  |

### Brazos
| Ejercicio | Series | Reps | Notas |
|---|---|---|---|
|  |  |  |  |

### Pecho
| Ejercicio | Series | Reps | Notas |
|---|---|---|---|
|  |  |  |  |

### Pierna
| Ejercicio | Series | Reps | Notas |
|---|---|---|---|
|  |  |  |  |

### Finisher — Abdomen
| Ejercicio | Series | Reps | Notas |
|---|---|---|---|
|  |  |  |  |

### Finisher — Cuello
| Ejercicio | Series | Reps | Notas |
|---|---|---|---|
|  |  |  |  |

## ¿Dónde voy del ciclo?

```dataview
TABLE WITHOUT ID
  file.link AS "Día",
  entreno_dia AS "Sesión",
  entreno_finisher AS "Finisher",
  default(entreno_rpe, "—") AS "RPE"
FROM "10-Diario"
WHERE tipo = "diario" AND entreno = true
SORT fecha DESC
LIMIT 12
```
