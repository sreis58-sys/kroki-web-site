"""Bütün sayfalara paylaşım önizlemesi (Open Graph) etiketleri; tekrar çalıştırılabilir. Sayfa üreticilerinden sonra çalıştırılır.
Alan adı belli olunca SITE değişkenine yazılır; önizleme görselleri tam adresle verilir (bazı uygulamalar göreli adres okumaz)."""
import re
kok = 'C:/Users/msali/Desktop/kroki-web-site/'
SITE = ''          # ör. 'https://kroki.com.tr/' — boşken göreli adres kullanılır
SAYFALAR = {
    'kroki-web.html': ('Kroki — Mimari yazılımlar', 'Mimarların ihtiyaçları için tasarlanmış, birbirine bağlı yazılımlar: kroki crm ve pafta.', 'og-kroki.jpg'),
    'kroki-crm.html': ('kroki crm — Dağınık işler, tek planda', 'İç mimarlık stüdyoları için müşteri, şantiye, takvim, sözleşme ve tahsilat yönetimi.', 'og-crm.jpg'),
    'pafta.html': ('pafta. — Ölçü sahada, plan elinde', 'Röleveyi telefonla alın: duvarlar, kirişler, kapılar ve ölçüler plana kendiliğinden yazılsın. Şimdilik ücretsiz.', 'og-pafta.jpg'),
    'hakkimizda.html': ('Hakkımızda — Kroki', 'Kroki, iç mimarlık ve mimarlık stüdyoları için yazılım geliştirir.', 'og-kroki.jpg'),
    'kvkk.html': ('KVKK ve gizlilik — Kroki', 'Kroki web sitesinde kişisel verilerin işlenmesine ilişkin aydınlatma metni.', 'og-kroki.jpg'),
    '404.html': ('Sayfa bulunamadı — Kroki', 'Aradığınız sayfa bulunamadı.', 'og-kroki.jpg'),
}
for dosya, (baslik, aciklama, gorsel) in SAYFALAR.items():
    p = kok + dosya; s = open(p, encoding='utf-8').read()
    s = re.sub(r'<!-- paylaşım önizlemesi -->.*?<!-- /paylaşım önizlemesi -->\n', '', s, flags=re.S)
    etiketler = f'''<!-- paylaşım önizlemesi -->
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
    i = s.index('<link rel="icon"')
    s = s[:i] + etiketler + s[i:]
    open(p, 'w', encoding='utf-8').write(s)
print('önizleme etiketleri eklendi')
