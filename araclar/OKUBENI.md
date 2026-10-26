# Sayfa üreticileri

`pafta.html`, `kroki-crm.html`, `kvkk.html`, `hakkimizda.html` ve `404.html` bu betiklerle üretilir. Menü, alt bilgi ve temel stil her seferinde `kroki-web.html`'den alınır. Bu yüzden ana sayfanın menüsünü ya da alt bilgisini değiştirdikten sonra betikleri yeniden çalıştırın.

Bu klasörün içinden, şu sırayla çalıştırın:

```
python pafta_v2.py          # pafta.html
python crm_v5.py            # kroki-crm.html
python metin_sayfalari.py   # kvkk.html, hakkimizda.html, 404.html
python son_dokunus.py       # bütün sayfalara paylaşım önizlemesi etiketleri
```

Sayfalardaki telefon ekranları `pafta_ekranlar.py` ve `crm_ekranlar.py` içinde SVG olarak çizilir.

## Ek araçlar

Bu iki araç `font/` klasöründe yazı tipi dosyası ister. Klasör git'e girmez; dosyaları Google Fonts deposundan indirin.

- `og_gorsel.py`: `assets/og-*.jpg` paylaşım görsellerini üretir. `font/Sora.ttf` gerekir.
- `pc_temizle.py`: `referans/kroki-crm/pc/` altındaki ekran görüntülerinden `assets/crm-pc-*.webp` dosyalarını üretir. Gerçek müşteri adlarını örnek adlarla değiştirir. `font/Inter.ttf` gerekir.

Alan adı belli olunca `son_dokunus.py` içindeki `SITE` değişkenine yazın ve betiği yeniden çalıştırın. Paylaşım görselleri o zaman tam adresle verilir.
