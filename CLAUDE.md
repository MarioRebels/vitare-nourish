# CLAUDE.md — Vitaré página

Sitio estático de **Vitaré Nourish** (cosmética, Sonora): https://www.vitarenourish.com/
Repo público `MarioRebels/vitare-nourish`, publicado con GitHub Pages: HTML/CSS/JS sin
build. **Un push a `main` publica el sitio.** El dominio ya está completo (HTTPS,
renovación 2027-08-02); el detalle vive en la memoria del proyecto.

## Cómo medir el estado de ESTE negocio

- Sitio vivo: `curl -sL https://www.vitarenourish.com/` y mirar el `<title>`, no solo el 200.
- Pendientes: `docs/TODO.md` (los lee `pendientes.py`). Solo lo abierto, lo cerrado se borra.
- Anchos: **375 px** (celular) y PC antes de dar algo por listo.
- Fotos: los originales (`uploads/`, `assets/prod/*.png`) NO se publican; los `.webp`
  de `assets/prod/` SÍ los usa el sitio. Regenerar con `python _optimizar.py`.

## Reglas de la casa

1. 🏟️ Esta carpeta es SOLO de Vitaré. Lo de otro proyecto va a su carpeta.
2. Explicaciones básicas y en español.
3. Avisar ANTES de `git commit`/push y esperar OK: el push publica el sitio.
4. El historial del repo se reescribió el 2026-09-03 para purgar 30 archivos privados.
   El historial viejo está en `~/.claude/backups/vitare-nourish-historial-viejo-20260903.bundle`.
   No volver a subir esos archivos: el `.gitignore` los cubre.
