"""Elle yazılan ana sayfaya (index.html) paylaşım önizlemesi, asıl adres ve yapılandırılmış veri etiketlerini yazar;
site haritasını (sitemap.xml) ve robots.txt'yi üretir. Tekrar çalıştırılabilir. Üretilen sayfalar bu etiketleri
ortak.py'deki sayfa iskeletinden zaten alır."""
import re
import ortak as O

yol = O.kok / 'index.html'
s = yol.read_text(encoding='utf-8')
for blok in ('paylaşım önizlemesi', 'arama motorları'):
    s = re.sub(rf'<!-- {blok} -->.*?<!-- /{blok} -->\n', '', s, flags=re.S)
site = {'@context': 'https://schema.org', '@type': 'WebSite', 'name': 'Kroki', 'url': O.SITE, 'inLanguage': 'tr'}
i = s.index('<link rel="icon"')
yol.write_text(s[:i] + O.onizleme('index.html') + O.arama('index.html', [O.kurulus(), site]) + s[i:], encoding='utf-8')
O.site_haritasi()
print('index.html etiketleri, sitemap.xml ve robots.txt yazıldı')
