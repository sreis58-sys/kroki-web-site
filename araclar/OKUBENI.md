# Sayfa üreticileri

`pafta.html`, `kroki-crm.html`, `kvkk.html`, `hakkimizda.html` ve `404.html` bu betiklerle üretilir. Bu sayfaları elle düzenlemeyin; değişikliği betikte yapıp yeniden üretin. `kroki-web.html` (ana sayfa) ve `admin.html` ise elle yazılır.

`ortak.py` bütün sayfaların ortak parçalarını tutar:
- menü, alt bilgi ve temel stil (`kroki-web.html`'den alınır)
- sayfa iskeleti ve paylaşım önizlemesi etiketleri
- mağaza düğmeleri
- paket kartları (`assets/site-icerik.js`'den okunur, bunun için `node` gerekir)

Ana sayfanın menüsünü ya da alt bilgisini değiştirdikten sonra betikleri yeniden çalıştırın. Sıra önemli değildir; her betik yalnızca kendi sayfasını yazar:

```
python pafta_v2.py          # pafta.html
python crm_v5.py            # kroki-crm.html
python metin_sayfalari.py   # kvkk.html, hakkimizda.html, 404.html
python son_dokunus.py       # kroki-web.html'in paylaşım önizlemesi etiketleri
```

Sayfalardaki telefon ekranları `pafta_ekranlar.py` ve `crm_ekranlar.py` içinde SVG olarak çizilir. Ürün sayfalarının ortak stilleri `pafta_v2.py`'nin `CSS`/`MOBIL` bölümlerindedir; `crm_v5.py` de onları kullanır.

## Ek araçlar

Bu iki araç `font/` klasöründe yazı tipi dosyası ister. Klasör git'e girmez; dosyaları Google Fonts deposundan indirin.

- `og_gorsel.py`: `assets/og-*.jpg` paylaşım görsellerini üretir. `font/Sora.ttf` gerekir.
- `pc_temizle.py`: `referans/kroki-crm/pc/` altındaki ekran görüntülerinden `assets/crm-pc-*.webp` dosyalarını üretir. Gerçek müşteri adlarını örnek adlarla değiştirir. `font/Inter.ttf` gerekir.

Alan adı belli olunca `ortak.py` içindeki `SITE` değişkenine yazın ve dört betiği yeniden çalıştırın. Paylaşım görselleri o zaman tam adresle verilir.
