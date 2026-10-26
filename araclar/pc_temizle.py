"""kroki crm bilgisayar ekran görüntülerini siteye hazırlar: tarayıcı çubuğu, görev çubuğu ve bildirim kesilir;
gerçek müşteri adları, telefon, adres ve notlar örnek bilgilerle değiştirilir (Inter ile, aynı yerde ve boyda)."""
from collections import Counter
from PIL import Image, ImageDraw, ImageFont

KAYNAK = 'C:/Users/msali/Desktop/kroki-web-site/referans/kroki-crm/pc/Screenshot 2026-10-26 '
HEDEF = 'C:/Users/msali/Desktop/kroki-web-site/assets/'
INTER = 'font/Inter.ttf'

def yazi_tipi(boy, agirlik):
    f = ImageFont.truetype(INTER, boy)
    f.set_variation_by_axes([min(32, max(14, boy)), agirlik])
    return f

def zemin_rengi(im, kutu):
    """kutunun çevresindeki en sık renk: yazının altındaki zemin"""
    x0, y0, x1, y1 = kutu
    px = [im.getpixel((x, y)) for x in range(x0, x1 + 1) for y in (y0, y1)] + [im.getpixel((x, y)) for y in range(y0, y1 + 1) for x in (x0, x1)]
    return Counter(px).most_common(1)[0][0]

def yazi_rengi(im, kutu):
    """kutudaki en parlak ya da zeminden en uzak piksel: eski yazının rengi"""
    z = zemin_rengi(im, kutu)
    x0, y0, x1, y1 = kutu
    return max((im.getpixel((x, y)) for x in range(x0, x1) for y in range(y0, y1)), key=lambda c: sum(abs(a - b) for a, b in zip(c, z)))

def degistir(im, kutu, x, taban, metin, boy, agirlik, renk=None, ortala=False):
    renk = renk or yazi_rengi(im, kutu)
    d = ImageDraw.Draw(im)
    d.rectangle(kutu, fill=zemin_rengi(im, kutu))
    d.text((x, taban), metin, font=yazi_tipi(boy, agirlik), fill=renk, anchor='ms' if ortala else 'ls')
    return yazi_tipi(boy, agirlik).getlength(metin)

def hazirla(saat, kirp, degisiklikler, ad):
    im = Image.open(KAYNAK + saat + '.png').convert('RGB')
    for d in degisiklikler:
        degistir(im, *d)
    im = im.crop(kirp)
    im.save(HEDEF + f'crm-pc-{ad}.webp', quality=90, method=6)
    print(ad, im.size)

GRI, BEYAZ = None, None  # renkler eski yazıdan okunur

# Panel: sıradaki iş ve bugünkü işler satırındaki müşteri
hazirla('210032', (0, 122, 1919, 990), [
    ((509, 524, 712, 543), 512, 537, 'Ece Yıldız · Moda daire', 13, 450),
    ((509, 777, 715, 794), 512, 789, 'Tasarım & Proje · Moda daire', 13, 450),
], 'panel')

# Müşteriler: ilk beş kişi
kisiler = [(418, 434, 'Ece Yıldız', 'EY', None), (511, 528, 'Deniz Arslan', 'DA', (554, 'Salon yenileme')),
           (603, 622, 'Selin Kaya', 'SK', None), (697, 714, 'Bora Demir', 'BD', (740, 'Ofis')), (790, 807, 'Merve Aksoy', 'MA', None)]
d = []
for taban, harf_y, ad, bas, is_ in kisiler:
    d.append(((543, taban - 15, 660, taban + 5), 545, taban, ad, 16, 700))
    d.append(((506, harf_y - 9, 531, harf_y + 8), 518, harf_y + 5, bas, 13, 600, None, True))
    if is_:
        d.append(((543, is_[0] - 13, 650, is_[0] + 6), 545, is_[0], is_[1], 13, 400))
hazirla('210125', (0, 122, 1919, 865), d, 'musteriler')

# Takvim (ay): sağdaki gün listesinde şantiye adı
hazirla('210248', (0, 122, 1919, 1100), [
    ((1258, 482, 1530, 500), 1260, 496, '· Moda daire · Elektrikçi ile iş başlatılacak', 12, 500),
], 'takvim')

# Muhasebe: hareketler
hazirla('210328', (0, 122, 1919, 1010), [
    ((559, 845, 660, 865), 561, 861, 'Ece Yıldız', 16, 700),
    ((559, 870, 795, 886), 561, 881, '17.10.2026 · 2. hakediş', 12, 400),
    ((559, 924, 650, 944), 561, 940, 'Bora Demir', 16, 700),
], 'muhasebe')

# Şantiye detayı: başlık, müşteri, telefon, adres, ad alanı, not
im_kirp = (1001, 122, 1919, 1150)
hazirla('210358', im_kirp, [
    ((1030, 150, 1400, 193), 1033, 183, 'Moda Daire Şantiyesi', 36, 800),
    ((1030, 196, 1112, 213), 1033, 208, 'Ece Yıldız', 14, 400),
    ((1030, 223, 1176, 241), 1033, 235, '0532 000 00 00', 13, 700),
    ((1068, 322, 1245, 344), 1071, 338, 'Moda Daire Şantiyesi', 15, 400),
    ((1572, 521, 1815, 539), 1574, 533, 'Usta ile görüşme yapıldı.', 12, 600),
], 'santiye')
# adres telefonun yanına (aynı mavi)
im = Image.open(HEDEF + 'crm-pc-santiye.webp').convert('RGB')
mavi = (59, 130, 246)
ImageDraw.Draw(im).text((1033 - 1001 + yazi_tipi(13, 700).getlength('0532 000 00 00') + 14, 235 - 122), 'Moda', font=yazi_tipi(13, 700), fill=mavi, anchor='ls')
im.save(HEDEF + 'crm-pc-santiye.webp', quality=90, method=6)

# Sözleşme: müşteri ve iç mimar
hazirla('210441', im_kirp, [
    ((1044, 186, 1079, 208), 1061, 203, 'DA', 19, 500, None, True),
    ((1100, 150, 1335, 193), 1104, 183, 'Deniz Arslan', 36, 800),
    ((1068, 829, 1160, 851), 1071, 845, 'Ada Yılmaz', 15, 400),
    ((1566, 469, 1700, 493), 1570, 487, 'Deniz Arslan', 20, 800),
    ((1648, 597, 1725, 615), 1650, 609, 'Ada Yılmaz', 12, 600),
], 'sozlesme')
