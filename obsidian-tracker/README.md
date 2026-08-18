# Tracker de Obsidian — Curso 3.º de Física (sept–dic 2026, exámenes enero 2027)

Sistema de seguimiento diario para universidad, entrenamiento e idiomas. Todo son ficheros Markdown planos: se copian dentro de una bóveda de Obsidian y funcionan tal cual.

## Instalación (5 minutos)

1. **Copia las carpetas** (`00-Panel`, `10-Diario`, `20-Universidad`, `30-Entrenamiento`, `40-Idiomas`, `90-Plantillas`) dentro de tu bóveda. Si usas Obsidian Sync, se propagarán solas al resto de tus dispositivos.
2. **Instala Dataview** (Ajustes → Complementos de la comunidad → buscar «Dataview» → instalar y activar). Es el único plugin externo que hace falta; sin él las tablas se ven como bloques de código.
3. **Activa las plantillas** (complemento interno «Plantillas»): carpeta de plantillas → `90-Plantillas`.
4. **Activa las notas diarias** (complemento interno «Notas diarias»):
   - Formato de fecha: `YYYY-MM-DD`
   - Ubicación de notas nuevas: `10-Diario`
   - Plantilla: `90-Plantillas/Plantilla Diaria`
5. Abre **[[Panel Diario]]** y ancla la nota. Ese es tu punto de entrada.
6. Borra `10-Diario/2026-09-14.md` cuando ya no lo necesites: es un día de ejemplo para que veas los paneles con datos.

> Las notas de `90-Plantillas` muestran un aviso de propiedad inválida en Obsidian: es normal,
> los marcadores `{{date:...}}` no son YAML válido hasta que Obsidian los sustituye. Las notas
> que se generan a partir de ellas salen correctas.

> Si prefieres Templater al plugin de plantillas nativo, funciona igual: sustituye `{{date:YYYY-MM-DD}}` por `<% tp.date.now("YYYY-MM-DD") %>` en las plantillas.

## Cómo se usa a diario

Sólo hay una regla: **rellena el frontmatter de la nota diaria**. Los números de las cabeceras `min_*`, `entreno`, `sueno_h`, etc. son de donde se alimentan todos los paneles. El cuerpo de la nota es para ti; la cabecera es para las tablas.

| Campo | Qué va | Ejemplo |
|---|---|---|
| `min_cuantica`, `min_em`, `min_fismat`, `min_mecanica`, `min_optica` | minutos **de trabajo real** por asignatura | `90` |
| `min_frances`, `min_ruso` | minutos de idioma | `25` |
| `entreno` | ¿entrenaste? | `true` / `false` |
| `entreno_dia` | Espalda / Brazos / Pecho / Pierna | `Espalda` |
| `entreno_finisher` | Abdomen / Cuello | `Abdomen` |
| `entreno_rpe` | esfuerzo 1–10 | `8` |
| `sueno_h`, `energia`, `animo` | horas y escalas 1–5 | `7.5`, `4`, `4` |
| `semana` | semana ISO, la rellena la plantilla | `2026-W38` |

Etiqueta las dudas con `#cuantica`, `#em`, `#fismat`, `#mecanica`, `#optica` y aparecerán solas en la nota de cada asignatura y en el [[Panel Universidad]] hasta que las taches.

## Estructura

```
00-Panel/            Los cuatro cuadros de mando (empieza por Panel Diario)
10-Diario/           Una nota por día — el único sitio donde escribes datos
20-Universidad/      Las cinco asignaturas + Horario + Exámenes
30-Entrenamiento/    Rutina (ciclo completo) + Sesiones detalladas
40-Idiomas/          Francés y Ruso
90-Plantillas/       Plantillas diaria, semanal, sesión de entreno, asignatura
```

## Lo que todavía está pendiente

Tres cosas que dijiste que llegarían más tarde. El esqueleto está montado para recibirlas:

- **Horario de la universidad** → `20-Universidad/Horario.md`. Con él se puede derivar el reparto semanal de estudio y detectar los huecos aprovechables entre clases.
- **Detalles del entrenamiento** (ejercicios, series, cargas) → `30-Entrenamiento/Rutina.md`.
- **Detalles de idiomas** (nivel, materiales, objetivos) → `40-Idiomas/Francés.md` y `Ruso.md`.

Además, las **fechas de examen de enero**: en cuanto las tengas, ponlas en el campo `examen:` de cada asignatura y las cuentas atrás se rellenan solas.

## Decisiones de diseño, por si las quieres cambiar

- **Minutos, no horas.** Registrar en minutos hace que las sesiones cortas cuenten, que es justo lo que necesita el ruso en fase inicial.
- **Sin días fijos de entrenamiento.** El ciclo avanza por sesiones, no por días de la semana, porque una semana de exámenes o de prácticas no debe romper la rotación. El [[Panel Entrenamiento]] te dice siempre cuál toca.
- **Una sola fuente de datos.** Todo se escribe en la nota diaria; el resto de notas sólo consultan. Así no hay dos sitios que puedan contradecirse.
- **El diario no lleva el temario.** Los apuntes de contenido van en las notas de asignatura, que sobreviven al semestre; el diario es registro, no material de estudio.
