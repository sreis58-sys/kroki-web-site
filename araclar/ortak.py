"""Sayfa üreticilerinin ortak parçaları. İçe aktarılınca hiçbir dosyaya yazmaz.

Menü, alt bilgi, temel stil ve el yazısı not/bant stilleri ana sayfadan (kroki-web.html) alınır; böylece ana sayfada
yapılan bir değişiklik, üreticiler yeniden çalıştırılınca bütün sayfalara geçer."""
import json
import subprocess
from pathlib import Path

kok = Path(__file__).resolve().parent.parent
ana = (kok / 'kroki-web.html').read_text(encoding='utf-8')


def kes(metin, bas, son=None, dahil=False):
    """metin içinde bas'tan son'a kadar olan parça; son verilmezse sona kadar, dahil=True ise son da dahil."""
    i = metin.index(bas)
    if son is None:
        return metin[i:]
    j = metin.index(son, i)
    return metin[i:j + (len(son) if dahil else 0)]


def satir_sonuna(metin, bas, son_satir):
    """bas'tan, son_satir ile başlayan satırın sonuna kadar."""
    i = metin.index(bas)
    return metin[i:metin.index('\n', metin.index(son_satir, i))]


# ---------- ana sayfadan alınan parçalar ----------
temel_css = kes(ana, ':root{', '.menu-btn svg{width:26px;height:26px}', dahil=True)
alt_css = kes(ana, '.alt{background:#121212;color:#fff}', '.alt__telif{color:#8d8d8d;margin-left:min(4.5vw,65px)}', dahil=True)
mobil_ust = kes(ana, '  .ust{height:76px;padding-top:0}', '  .ust.acik .ust__nav a{padding:14px 0;font-size:1.05rem;border-bottom:1px solid #dcd8cf}', dahil=True)
mobil_alt = kes(ana, '  .alt__ic{flex-wrap:wrap;', '  .alt__telif{margin-left:0;width:100%}', dahil=True)
ust_html = kes(ana, '<header class="kap ust" id="ust">', '</header>', dahil=True)
alt_html = kes(ana, '<footer class="alt">', '</footer>', dahil=True)
menu_js = kes(ana, '  // mobil menü', "menuBtn.setAttribute('aria-label', acik ? 'Menüyü kapat' : 'Menüyü aç');\n  });", dahil=True)
# el yazısı kesik çizgili not ve karakalem bant (koyu panel kuralı ana sayfaya özgü, alınmaz)
ANA_CSS = satir_sonuna(ana, '.not{position:absolute;', '.not span:last-child::before') + '\n' + kes(ana, '.bant{position:relative;', '\n.bant__eskiz .koyu')
ANA_MOBIL = kes(ana, '  .bant{height:auto}', '\n  .bant__eskiz{') + satir_sonuna(ana, '  .bant__eskiz{position:relative;', '  .bant__eskiz{position:relative;')


# ---------- içerik: sitenin başlangıç içeriği tek kaynaktan, assets/site-icerik.js ----------
def site_icerik():
    """site-icerik.js'deki window.SITE_VARSAYILAN; dosya JavaScript olduğu için node ile okunur."""
    betik = 'global.window = {}; require(process.argv[1]); process.stdout.write(JSON.stringify(window.SITE_VARSAYILAN));'
    cikti = subprocess.run(['node', '-e', betik, str(kok / 'assets' / 'site-icerik.js')],
                           capture_output=True, text=True, encoding='utf-8', check=True)
    return json.loads(cikti.stdout)


def paketler_html(hedef):
    """paket kartları; site-veri.js'deki paketleriYaz ile aynı yapı (sayfa Firebase'den okumadan önce de doğru görünür)."""
    kartlar = []
    for p in site_icerik()['paketler']:
        onerilen = p.get('onerilen')
        kartlar.append(f'''      <article class="paket"{' data-onerilen' if onerilen else ''}>
        {'<span class="paket__etiket">Önerilen</span>' if onerilen else ''}<h3>{p['ad']}</h3>
        <p class="paket__kim">{p['kim']}</p>
        <p class="paket__fiyat">{p['fiyat']} TL <small>/ ay</small></p>
        <ul>{''.join(f'<li>{o}</li>' for o in p['ozellikler'])}</ul>
        <a class="paket__btn" href="{hedef}">Ücretsiz dene</a>
      </article>''')
    return '\n'.join(kartlar)


# ---------- mağaza düğmeleri ----------
APPLE = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16.37 12.6c-.02-2.3 1.88-3.4 1.96-3.46-1.07-1.56-2.73-1.78-3.32-1.8-1.41-.14-2.76.83-3.48.83-.72 0-1.82-.81-3-.79-1.54.02-2.97.9-3.76 2.28-1.61 2.79-.41 6.91 1.15 9.17.77 1.1 1.68 2.34 2.87 2.3 1.15-.05 1.59-.74 2.98-.74 1.39 0 1.78.74 3 .72 1.24-.02 2.03-1.12 2.78-2.23.88-1.28 1.24-2.52 1.26-2.59-.03-.01-2.41-.92-2.44-3.69zM14.1 5.86c.63-.77 1.06-1.83.94-2.89-.91.04-2.02.61-2.67 1.37-.58.67-1.1 1.76-.96 2.8 1.02.08 2.06-.52 2.69-1.28z"/></svg>'
PLAY = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#32BBFF" d="M3.6 2.3 13 12l-9.4 9.7c-.3-.3-.4-.8-.4-1.3V3.6c0-.5.1-1 .4-1.3z"/>'
        '<path fill="#00F076" d="M3.6 2.3c.4-.4 1-.4 1.7 0l11.1 6.3L13 12z"/><path fill="#FF3A44" d="M3.6 21.7 13 12l3.4 3.4-11.1 6.3c-.7.4-1.3.4-1.7 0z"/>'
        '<path fill="#FFD500" d="m16.4 8.6 3.6 2c1.1.6 1.1 2.2 0 2.8l-3.6 2L13 12z"/></svg>')


def magaza(kod='pafta', ad='pafta.', ek=''):
    """App Store ve Google Play düğmeleri; adresler admin panelinden gelir (data-bag="<kod>AppStore" …)."""
    return f'''<!-- MAĞAZA BAĞLANTILARI: adresler admin panelinden girilir; boşken düğmede "Yakında" yazar -->
        <div class="magaza{ek}">
          <a href="#" data-bag="{kod}AppStore" aria-label="{ad} uygulamasını App Store'dan indirin">{APPLE}<span><small>Şuradan indirin</small><b>App Store</b></span></a>
          <a href="#" data-bag="{kod}GooglePlay" aria-label="{ad} uygulamasını Google Play'den indirin">{PLAY}<span><small>Şuradan alın</small><b>Google Play</b></span></a>
        </div>'''


# kaydırma sahnelerinin ortak yardımcıları (ürün sayfalarının betiklerine eklenir)
ARA_JS = '''    const sinir = v => Math.max(0, Math.min(1, v));
    const yumusak = t => t * t * (3 - 2 * t);
    const ara = (a, b, p) => yumusak(sinir((p - a) / (b - a)));
    const kar = (a, b, t) => a + (b - a) * t;
'''


# ---------- paylaşım önizlemesi (Open Graph) ----------
SITE = 'https://kroki-site.web.app/'   # alan adı alınınca yalnızca burası değişir, ör. 'https://kroki.com.tr/'
ONIZLEME = {
    'kroki-web.html': ('Kroki — Mimari yazılımlar', 'Mimarların ihtiyaçları için tasarlanmış, birbirine bağlı yazılımlar: kroki crm ve pafta.', 'og-kroki.jpg'),
    'kroki-crm.html': ('kroki crm — Dağınık işler, tek planda', 'İç mimarlık stüdyoları için müşteri, şantiye, takvim, sözleşme ve tahsilat yönetimi.', 'og-crm.jpg'),
    'pafta.html': ('pafta. — Ölçü sahada, plan elinde', 'Röleveyi telefonla alın: duvarlar, kirişler, kapılar ve ölçüler plana kendiliğinden yazılsın. Ücretsiz.', 'og-pafta.jpg'),
    'hakkimizda.html': ('Hakkımızda — Kroki', 'Kroki, iç mimarlık ve mimarlık stüdyoları için yazılım geliştirir.', 'og-kroki.jpg'),
    'kvkk.html': ('KVKK ve gizlilik — Kroki', 'Kroki web sitesinde kişisel verilerin işlenmesine ilişkin aydınlatma metni.', 'og-kroki.jpg'),
    '404.html': ('Sayfa bulunamadı — Kroki', 'Aradığınız sayfa bulunamadı.', 'og-kroki.jpg'),
}


def onizleme(dosya):
    baslik, aciklama, gorsel = ONIZLEME[dosya]
    return f'''<!-- paylaşım önizlemesi -->
<meta property="og:type" content="website">
<meta property="og:site_name" content="Kroki">
<meta property="og:locale" content="tr_TR">
<meta property="og:title" content="{baslik}">
<meta property="og:description" content="{aciklama}">
<meta property="og:image" content="{SITE}assets/{gorsel}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#F8F5EE">
<!-- /paylaşım önizlemesi -->
'''


# ---------- arama motorları: asıl adres ve yapılandırılmış veri ----------
SAYFA_HARITASI = ['kroki-web.html', 'kroki-crm.html', 'pafta.html', 'hakkimizda.html', 'kvkk.html']


def adres(dosya):
    """sayfanın asıl adresi; ana sayfa kök adreste yayınlanır"""
    return SITE if dosya == 'kroki-web.html' else SITE + dosya


def kurulus():
    return {'@context': 'https://schema.org', '@type': 'Organization', 'name': 'Kroki', 'url': SITE,
            'logo': SITE + 'assets/kroki-firma.png', 'description': 'İç mimarlık ve mimarlık stüdyoları için yazılım.'}


def uygulama(ad, aciklama, dosya, sistem, teklif):
    return {'@context': 'https://schema.org', '@type': 'SoftwareApplication', 'name': ad, 'description': aciklama,
            'url': adres(dosya), 'applicationCategory': 'BusinessApplication', 'operatingSystem': sistem, 'inLanguage': 'tr',
            'offers': teklif, 'publisher': {'@type': 'Organization', 'name': 'Kroki', 'url': SITE}}


def paket_teklifi():
    """kroki crm paketlerinin fiyat aralığı (site-icerik.js'den)"""
    fiyatlar = [int(p['fiyat'].replace('.', '')) for p in site_icerik()['paketler'] if p['fiyat'].replace('.', '').isdigit()]
    return {'@type': 'AggregateOffer', 'priceCurrency': 'TRY', 'lowPrice': min(fiyatlar), 'highPrice': max(fiyatlar), 'offerCount': len(fiyatlar)}


def sss(govde):
    """sayfadaki sık sorulan sorular (<details><summary>soru</summary><p>yanıt</p>) → FAQPage"""
    import re
    sorular = re.findall(r'<details><summary>(.*?)</summary><p>(.*?)</p></details>', govde)
    return {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': s, 'acceptedAnswer': {'@type': 'Answer', 'text': c}} for s, c in sorular]}


def arama(dosya, veriler=()):
    """asıl adres etiketi ve JSON-LD blokları"""
    ld = ''.join(f'<script type="application/ld+json">{json.dumps(v, ensure_ascii=False)}</script>\n' for v in veriler)
    return f'<!-- arama motorları -->\n<link rel="canonical" href="{adres(dosya)}">\n{ld}<!-- /arama motorları -->\n'


def site_haritasi():
    from datetime import date
    gun = date.today().isoformat()
    satirlar = ''.join(f'  <url><loc>{adres(d)}</loc><lastmod>{gun}</lastmod></url>\n' for d in SAYFA_HARITASI)
    (kok / 'sitemap.xml').write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{satirlar}</urlset>\n', encoding='utf-8')
    (kok / 'robots.txt').write_text(f'User-agent: *\nDisallow: /admin.html\n\nSitemap: {SITE}sitemap.xml\n', encoding='utf-8')


# ---------- sayfa iskeleti ----------
YAZI_TIPLERI = {
    'urun': 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Patrick+Hand&family=Sora:wght@400;500;600;700&display=swap',
    'metin': 'https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700&display=swap',
}
ORTAK_NOT = 'Menü, alt bilgi ve temel stil ana sayfayla (kroki-web.html) ortaktır.'


def sayfa(dosya, baslik, aciklama, css, mobil, govde, js='', ikon='assets/kroki-crm-ikon.svg',
          yazi_tipi='urun', css_notu=ORTAK_NOT, taban=None, veriler=(), dizinle=True):
    """Sayfayı yazar. css/mobil: temel stil ile alt bilgi stili arasına girenler; govde: menü ile alt bilgi arası;
    js: mobil menüden önce çalışan betik; taban: <base href> (404 gibi her adreste açılan sayfalar için);
    veriler: JSON-LD nesneleri; dizinle=False: asıl adres verilmez (404)."""
    metin = f'''<!doctype html>
<html lang="tr">
<head>
{f'<base href="{taban}">' + chr(10) if taban else ''}<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{baslik}</title>
<meta name="description" content="{aciklama}">
{onizleme(dosya)}{arama(dosya, veriler) if dizinle else ""}<link rel="icon" href="{ikon}">
<script>document.documentElement.classList.add('js')</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://firestore.googleapis.com" crossorigin>
<link href="{YAZI_TIPLERI[yazi_tipi]}" rel="stylesheet">
<style>
/* {css_notu} */
{temel_css}
{css}

{alt_css}

@media (max-width:900px){{
{mobil_ust}
{mobil}
{mobil_alt}
}}
</style>
</head>
<body>
{ust_html}

{govde}

{alt_html}

<script src="assets/firebase-ayar.js"></script>
<script src="assets/site-icerik.js"></script>
<script src="assets/site-veri.js"></script>
<script>
{js}{menu_js}
</script>
</body>
</html>
'''
    (kok / dosya).write_text(metin, encoding='utf-8')
    print(f'{dosya} yazıldı', len(metin))
