# Genera las versiones WebP optimizadas del sitio.
# Se puede volver a ejecutar cuando se cambien las imagenes originales:
#     python _optimizar.py
import os
from PIL import Image

U = "uploads/Pagina tia nusi"

# fotos usadas por la pagina -> nombre limpio (sin espacios ni acentos)
FOTOS = {
    f"{U}/WhatsApp Image 2026-07-16 at 5.53.42 PM (1).jpeg": "linea-completa",
    f"{U}/WhatsApp Image 2026-07-16 at 5.53.42 PM (2).jpeg": "instructivo-dia",
    f"{U}/WhatsApp Image 2026-07-16 at 5.53.42 PM (3).jpeg": "catalogo",
    f"{U}/WhatsApp Image 2026-07-16 at 5.53.43 PM (5).jpeg": "ficha-caldo",
    f"{U}/WhatsApp Image 2026-07-16 at 5.53.43 PM (3).jpeg": "ficha-shots",
    f"{U}/WhatsApp Image 2026-07-16 at 5.53.43 PM (2).jpeg": "beneficios",
}
ANCHOS = [512, 768, 1024]     # variantes responsive; la de 1024 es la del lightbox

os.makedirs("assets/fotos", exist_ok=True)

antes = despues = 0
print("--- FOTOS (JPEG -> WebP, 3 anchos) ---")
for src, slug in FOTOS.items():
    im = Image.open(src).convert("RGB")
    antes += os.path.getsize(src)

    # El hero se recorta a 4:5 por CSS (object-fit: cover). Recortarlo aqui evita
    # enviar pixeles que el navegador va a descartar igualmente.
    if slug == "linea-completa":
        w0, h0 = im.size
        alto_util = round(w0 * 5 / 4)
        if h0 > alto_util:                      # recorte centrado
            top = (h0 - alto_util) // 2
            im = im.crop((0, top, w0, top + alto_util))
    q = 82              # todas llevan texto impreso: no bajar de aqui

    w0, h0 = im.size
    for w in ANCHOS:
        if w > w0:
            continue
        h = round(h0 * w / w0)
        out = f"assets/fotos/{slug}-{w}.webp"
        im.resize((w, h), Image.LANCZOS).save(out, "WEBP", quality=q, method=6)
        despues += os.path.getsize(out)
    big = f"assets/fotos/{slug}-{min(ANCHOS[-1], w0)}.webp"
    print(f"  {slug:18s} {w0}x{h0} -> {os.path.getsize(big)/1024:5.0f} KB (grande)")

print("\n--- PRODUCTOS (PNG con transparencia -> WebP 560) ---")
for f in sorted(os.listdir("assets/prod")):
    if not f.endswith(".png"):
        continue
    src = f"assets/prod/{f}"
    im = Image.open(src).convert("RGBA")
    antes += os.path.getsize(src)
    out = src[:-4] + ".webp"
    im.save(out, "WEBP", quality=85, method=6, exact=False)
    despues += os.path.getsize(out)
    print(f"  {f:20s} {os.path.getsize(src)/1024:5.0f} KB -> {os.path.getsize(out)/1024:5.0f} KB")

print("\n--- VISTA PREVIA para WhatsApp / redes (og:image) ---")
# 1200x630 es el formato que esperan WhatsApp, Facebook y X. El cartel es
# vertical, asi que se centra completo sobre una version difuminada de si mismo
# en vez de recortarlo (recortarlo cortaria el logotipo).
from PIL import ImageFilter, ImageEnhance

OG_W, OG_H = 1200, 630
cartel = Image.open(next(iter(FOTOS))).convert("RGB")

escala = max(OG_W / cartel.width, OG_H / cartel.height)
fondo = cartel.resize((round(cartel.width * escala), round(cartel.height * escala)), Image.LANCZOS)
izq = (fondo.width - OG_W) // 2
arr = (fondo.height - OG_H) // 2
fondo = fondo.crop((izq, arr, izq + OG_W, arr + OG_H))
fondo = fondo.filter(ImageFilter.GaussianBlur(28))
fondo = ImageEnhance.Brightness(fondo).enhance(0.72)

alto = OG_H - 24
frente = cartel.resize((round(cartel.width * alto / cartel.height), alto), Image.LANCZOS)
fondo.paste(frente, ((OG_W - frente.width) // 2, (OG_H - alto) // 2))
fondo.save("assets/og.jpg", "JPEG", quality=86, optimize=True, progressive=True)
despues += os.path.getsize("assets/og.jpg")
print(f"  assets/og.jpg  {OG_W}x{OG_H}  {os.path.getsize('assets/og.jpg')/1024:.0f} KB")

print(f"\nOriginales : {antes/1024/1024:.2f} MB")
print(f"Optimizado : {despues/1024/1024:.2f} MB  (todas las variantes juntas)")
