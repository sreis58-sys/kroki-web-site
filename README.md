# Kroki web sitesi

Kroki'nin tanıtım sitesi: ana sayfa, **kroki crm** ve **pafta.** ürün sayfaları, Hakkımızda, KVKK ve bir yönetim paneli.
Yayındaki adres: https://kroki-site.web.app

## Dosya düzeni

```
index.html          ana sayfa (elle yazılır)
kroki-crm.html      kroki crm ürün sayfası        ┐
pafta.html          pafta. ürün sayfası           │ araclar/ içindeki betiklerle üretilir,
hakkimizda.html     Hakkımızda                    │ elle düzenlenmez
kvkk.html           KVKK ve gizlilik              │
404.html            bulunamayan sayfalar          ┘
admin.html          yönetim paneli (başvurular, paketler, yorumlar, bağlantılar)
robots.txt          arama motorları için ┐ araclar/ana_sayfa_etiketleri.py üretir
sitemap.xml         site haritası        ┘

assets/
  logolar/          Kroki, kroki crm ve pafta. logoları
  gorseller/        eskizler, uygulama ekran görüntüleri, paylaşım görselleri
  js/               firebase-ayar.js (Firebase bağlantısı), site-icerik.js (başlangıç içeriği ve ortak yardımcılar),
                    site-veri.js (içeriği sayfaya uygular, iletişim formunu gönderir)

araclar/            sayfa üreticileri ve görsel araçları (nasıl çalıştırılacağı: araclar/OKUBENI.md)
kaynak/             eskizlerin Figma'dan gelen özgün hâlleri (yayınlanmaz)

firebase.json       barındırma ayarları   ┐ Firebase
firestore.rules     veritabanı kuralları  ┘
ADMIN-KURULUM.md    Firebase ve yönetim paneli kurulumu
```

`referans/` (ham ekran görüntüleri, videolar) ve `inceleme/` (kod inceleme raporları) bilgisayarda durur, depoya girmez.

## Yayınlama

```
npx -y firebase-tools deploy --only hosting --project kroki-site
```

Paketler, yorumlar, mağaza ve sosyal medya bağlantıları ile şirket bilgileri yönetim panelinden değiştirilir; bunlar için yeniden yayınlamak gerekmez.
