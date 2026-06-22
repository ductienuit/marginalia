# Generates og-image.png (1200x630) for social/AI sharing.
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
ink = (23, 32, 51)
blue = (37, 99, 235)
blue_d = (29, 78, 216)
slate = (96, 112, 134)
amber = (251, 191, 36)
white = (255, 255, 255)

# vertical gradient background
top = (248, 251, 255)
bot = (238, 243, 250)
img = Image.new("RGB", (W, H), top)
px = img.load()
for y in range(H):
    t = y / (H - 1)
    r = round(top[0] + (bot[0] - top[0]) * t)
    g = round(top[1] + (bot[1] - top[1]) * t)
    b = round(top[2] + (bot[2] - top[2]) * t)
    for x in range(W):
        px[x, y] = (r, g, b)

d = ImageDraw.Draw(img, "RGBA")

# soft blue glow top-right
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
gd.ellipse([W - 380, -220, W + 160, 320], fill=(37, 99, 235, 26))
img.paste(Image.alpha_composite(img.convert("RGBA"), glow).convert("RGB"), (0, 0))
d = ImageDraw.Draw(img, "RGBA")

segb = "C:/Windows/Fonts/segoeuib.ttf"
segr = "C:/Windows/Fonts/segoeui.ttf"
f_brand = ImageFont.truetype(segb, 120)
f_tag = ImageFont.truetype(segb, 46)
f_sub = ImageFont.truetype(segr, 33)
f_url = ImageFont.truetype(segb, 30)
f_badge = ImageFont.truetype(segb, 26)

# ---- logo tile (echoes the favicon) ----
ox, oy, size = 80, 70, 130
s = size / 64.0
d.rounded_rectangle([ox, oy, ox + size, oy + size], radius=int(14 * s), fill=blue)
def r(x, y, w, h, rad, fill):
    d.rounded_rectangle([ox + x * s, oy + y * s, ox + (x + w) * s, oy + (y + h) * s], radius=rad, fill=fill)
r(13, 25, 28, 6, 6, (255, 255, 255, 130))
r(13, 37, 22, 6, 6, (255, 255, 255, 130))
r(11, 31, 34, 8, 8, white)
d.ellipse([ox + 43 * s, oy + 14 * s, ox + 55 * s, oy + 26 * s], fill=amber)

# small kicker badge next to logo
bx = ox + size + 26
d.rounded_rectangle([bx, oy + 40, bx + 360, oy + 92, ], radius=26, fill=(37, 99, 235, 28))
d.text((bx + 22, oy + 52), "MARKDOWN ANNOTATION", font=f_badge, fill=blue_d)

# ---- wordmark: "Margin" + "alia" (blue) ----
wy = 250
t1 = "Margin"
t2 = "alia"
d.text((78, wy), t1, font=f_brand, fill=ink)
w1 = d.textlength(t1, font=f_brand)
d.text((78 + w1, wy), t2, font=f_brand, fill=blue)

# ---- tagline with a highlight behind one word ----
ty = 410
seg_a = "Annotate Markdown, export "
seg_b = "context"
seg_c = " for AI."
xa = 80
wa = d.textlength(seg_a, font=f_tag)
wb = d.textlength(seg_b, font=f_tag)
# highlight bar behind "context"
d.rounded_rectangle([xa + wa - 4, ty + 8, xa + wa + wb + 8, ty + 58], radius=10, fill=(37, 99, 235, 38))
d.text((xa, ty), seg_a, font=f_tag, fill=ink)
d.text((xa + wa, ty), seg_b, font=f_tag, fill=blue_d)
d.text((xa + wa + wb, ty), seg_c, font=f_tag, fill=ink)

# ---- sub line ----
d.text((80, ty + 76), "Highlight a passage, add a note, copy a clean bundle for AI assistants.",
       font=f_sub, fill=slate)

# ---- url pill bottom ----
url = "ductienuit.github.io/marginalia"
uw = d.textlength(url, font=f_url)
d.rounded_rectangle([80, 552, 80 + uw + 44, 552 + 52], radius=26, fill=blue)
d.text((80 + 22, 552 + 11), url, font=f_url, fill=white)

img.save("og-image.png", "PNG")
print("saved og-image.png", img.size)
