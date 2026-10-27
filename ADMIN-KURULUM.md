# Admin panelini Firebase'e bağlama

Admin paneli (`admin.html`) Firebase'e bağlanana kadar **deneme modunda** çalışır. Bu modda yapılan değişiklikler ve gelen başvurular yalnızca o tarayıcıda saklanır. Aşağıdaki adımlar bir kez yapılır; sonunda panel gerçek veritabanıyla çalışır ve site yayına çıkar.

Bu proje kroki crm'in Firebase projesinden (`studyo-crm`) **ayrıdır**. Müşteri verisine dokunmaz ve ücretsiz Spark planında kalır.

## 1. Firebase projesini açın

1. https://console.firebase.google.com adresinde **Proje ekle**'ye tıklayın.
2. Ad olarak örneğin `kroki-site` yazın. Google Analytics gerekmez.
3. Proje açılınca sol üstteki dişli → **Proje ayarları**'ndaki **Proje kimliği**'ni not edin (ör. `kroki-site-1a2b3`).

## 2. Firestore ve giriş yöntemini açın

1. **Build → Firestore Database → Veritabanı oluştur**. Konum: `eur3 (europe-west)`. **Üretim modunda başlat**'ı seçin.
2. **Build → Authentication → Başlayın → E-posta/Şifre**'yi etkinleştirin.
3. **Authentication → Users → Kullanıcı ekle**: kendi e-postanız ve güçlü bir şifre. Eklenen satırdaki **Kullanıcı UID**'yi kopyalayın.

## 3. Web uygulaması ayarlarını siteye yazın

1. **Proje ayarları → Genel → Uygulamalarınız → `</>` (Web)**. Takma ad olarak `site` yazın. Hosting kutusunu işaretlemeyin.
2. Çıkan `firebaseConfig` içindeki dört değeri `assets/firebase-ayar.js` dosyasına yazın:

   ```js
   window.FIREBASE_AYAR = { apiKey: '…', authDomain: '….firebaseapp.com', projectId: '…', appId: '…' };
   ```

   Bu değerler gizli değildir. Veriyi `firestore.rules` korur.

3. `.firebaserc` dosyasındaki `PROJE-KIMLIGI` yerine 1. adımdaki proje kimliğini yazın.

## 4. Kuralları ve siteyi yayınlayın

Proje klasöründe bir kez:

```
npm install -g firebase-tools
firebase login
firebase deploy
```

`firebase deploy` iki şey yayınlar:
- **Firestore kuralları:** içeriği herkes okur, yalnızca yöneticiler değiştirir. Başvuruyu herkes gönderir, yalnızca yöneticiler okur.
- **Site:** `https://<proje-kimliği>.web.app` adresinde açılır. Kendi alan adınız **Hosting → Özel alan adı ekle**'den bağlanır.

## 5. Kendinizi yönetici yapın

1. **Firestore Database → Koleksiyon başlat**. Koleksiyon kimliği: `yoneticiler`.
2. **Belge kimliği:** 2. adımda kopyaladığınız UID. Alan eklemeniz gerekmez; boş bırakıp kaydedin. Konsol bir alan isterse `ad` = adınız yazın.
3. `https://<proje-kimliği>.web.app/admin.html` adresine gidip e-posta ve şifrenizle girin.

Sonra panelde **Bağlantılar ve şirket** sekmesinden şirket unvanını, adresi, MERSİS numarasını, KEP adresini ve iletişim e-postasını girin. Bunlar KVKK sayfasında görünür; boş kaldıkça sayfada köşeli parantezli yer tutucu çıkar.

Panelde ilk **Kaydet**'e basıldığında paketler, yorumlar ve bağlantılar Firebase'e yazılır. O andan sonra site içeriği oradan okur.

## Alan adı bağlandıktan sonra

`araclar/ortak.py` içindeki `SITE` değişkenine alan adını yazın (ör. `https://kroki.com.tr/`) ve `araclar/OKUBENI.md`'deki betiklerle sayfaları yeniden üretin. Böylece paylaşım görselleri tam adresle verilir. İsterseniz bir site haritası (`sitemap.xml`) da eklenir.

## Bilmeniz gerekenler

- Panelin adresi hiçbir yerde bağlantı olarak geçmez ve arama motorlarına kapalıdır (`noindex`). Panelin asıl koruması ise giriş ve Firestore kurallarıdır.
- Başka birini yönetici yapmak için ona Authentication'dan hesap açın ve `yoneticiler` koleksiyonuna onun UID'siyle bir belge ekleyin.
- Form spam alırsa Firebase **App Check** (reCAPTCHA) eklenebilir. Şu an formda yalnızca gizli bir tuzak alanı var.
- Ücretsiz Spark planının sınırları (günde 50.000 okuma, 20.000 yazma) bu site için fazlasıyla yeterlidir.
