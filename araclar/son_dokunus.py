"""Elle yazılan ana sayfaya (kroki-web.html) paylaşım önizlemesi (Open Graph) etiketlerini yazar; tekrar çalıştırılabilir.
Üretilen sayfalar bu etiketleri ortak.py'deki sayfa iskeletinden zaten alır. Etiketlerin metni: ortak.ONIZLEME."""
import re
import ortak as O

yol = O.kok / 'kroki-web.html'
s = yol.read_text(encoding='utf-8')
s = re.sub(r'<!-- paylaşım önizlemesi -->.*?<!-- /paylaşım önizlemesi -->\n', '', s, flags=re.S)
i = s.index('<link rel="icon"')
yol.write_text(s[:i] + O.onizleme('kroki-web.html') + s[i:], encoding='utf-8')
print('kroki-web.html: önizleme etiketleri yazıldı')
