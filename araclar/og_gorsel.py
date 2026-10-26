"""Paylaşım önizleme görselleri (1200×630): kâğıt zemin, solda logo ve başlık, sağda sayfanın karakalem eskizi."""
from PIL import Image, ImageDraw, ImageFont
A = 'C:/Users/msali/Desktop/kroki-web-site/assets/'
KAGIT, MUREKKEP, KURSUN, MAVI = (248, 245, 238), (19, 19, 19), (85, 85, 82), (28, 134, 238)

def yazi(boy, agirlik):
    f = ImageFont.truetype('font/Sora.ttf', boy); f.set_variation_by_axes([agirlik]); return f

def logo(yol, yukseklik):
    if yol.endswith('.svg'):
        return None
    im = Image.open(yol).convert('RGBA'); return im.resize((int(im.width * yukseklik / im.height), yukseklik), Image.LANCZOS)

def gorsel(ad, eskiz, logo_yolu, satirlar, alt, kirp, mavi=None):
    W, H = 1200, 630
    im = Image.new('RGB', (W, H), KAGIT)
    e = Image.open(A + eskiz).convert('RGBA').crop(kirp)
    olcek = H / e.height; e = e.resize((int(e.width * olcek), H), Image.LANCZOS)
    im.paste(e, (W - e.width + 10, 0), e)
    if mavi:                                                       # eskizdeki mavi düzlem, aynı ölçekte
        d = ImageDraw.Draw(im, 'RGBA'); ox = W - e.width + 10
        d.polygon([((x - kirp[0]) * olcek + ox, (y - kirp[1]) * olcek) for x, y in mavi], fill=MAVI + (215,))
    # yazının arkası temiz kalsın: soldan sağa açılan kâğıt
    perde = Image.new('RGBA', (W, H)); pd = ImageDraw.Draw(perde)
    for x in range(620):
        pd.line([(x, 0), (x, H)], fill=KAGIT + (int(255 * min(1, (620 - x) / 180)),))
    im.paste(perde, (0, 0), perde)
    d = ImageDraw.Draw(im)
    y = 92
    if logo_yolu.endswith('.svg'):                                 # pafta.: logo yazı ve mavi kare olarak çizilir
        f = yazi(62, 800); d.text((72, y + 56), 'pafta', font=f, fill=MUREKKEP, anchor='ls')
        w = f.getlength('pafta'); d.rectangle([72 + w + 6, y + 44, 72 + w + 20, y + 58], fill=MAVI)
    else:
        lg = logo(A + logo_yolu, 70); im.paste(lg, (72, y), lg)
    y = 250
    for s in satirlar:
        d.text((70, y), s, font=yazi(64, 650), fill=MUREKKEP, anchor='ls'); y += 76
    d.text((72, y + 24), alt, font=yazi(24, 400), fill=KURSUN, anchor='ls')
    im.save(A + f'og-{ad}.jpg', quality=86, optimize=True)
    print(ad)

gorsel('kroki', 'giris-eskiz.webp', 'kroki-firma.png', ['Aynı plan.', 'Farklı araçlar.'], 'Mimarlar için birbirine bağlı yazılımlar.', (180, 0, 1536, 1024),
       [(829, 575), (1036, 612), (1036, 798), (829, 798)])
gorsel('crm', 'crm-eskiz.webp', 'kroki-crm.png', ['Dağınık işler,', 'tek planda.'], 'Müşteri, şantiye, takvim ve tahsilat.', (300, 0, 1536, 1024),
       [(1232, 310), (1264, 310), (1264, 372), (1232, 372)])
gorsel('pafta', 'pafta-eskiz.webp', 'pafta-logo.svg', ['Ölçü sahada,', 'plan elinde.'], 'Röleveyi telefonla alın.', (380, 0, 1536, 1024),
       [(1392, 332), (1478, 318), (1478, 718), (1392, 693)])
