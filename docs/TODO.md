# PENDIENTES DE VITARÉ — solo lo VIVO

> 🔴 **ABIERTO HOY — 2026-09-03** (medido contra disco, GitHub y el sitio vivo)
>
> REGLA: **lo cerrado se BORRA** (la evidencia vive en git y la bitácora).
> Cada renglón dice cómo se comprueba.

## 1 · Pedir a soporte de GitHub que purgue los objetos viejos del repo

El 03-sep se reescribió el historial y se hizo force push: los 30 archivos privados
ya no están en ningún commit. Pero GitHub sigue sirviendo los objetos viejos si se
conoce el SHA antiguo. Solo soporte de GitHub los borra, y **solo Mario lo manda**
desde https://support.github.com/request con su cuenta.

Cómo se comprueba (debe dar 404; hoy da 200):
```
curl -sI https://raw.githubusercontent.com/MarioRebels/vitare-nourish/6510bc5/assets/src-catalogo.jpeg
```

Texto listo para pegar:
```
Repository: MarioRebels/vitare-nourish

I rewrote the history of this repository with git-filter-repo and
force-pushed to remove files that should not have been published.
The refs are clean, but the old objects are still served through
raw.githubusercontent.com and the commit view when the old SHA is
known (e.g. commit 6510bc5).

Please run garbage collection on this repository and purge the
cached views of the unreachable objects.
```
