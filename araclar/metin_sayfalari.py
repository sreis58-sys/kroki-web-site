"""kvkk.html (aydınlatma metni, gizlilik ve çerezler), hakkimizda.html ve 404.html. Menü, alt bilgi ve temel stil
ana sayfadan gelir (ortak.py)."""
import ortak as O

CSS = r'''
.metin-sayfa{padding:min(5vw,72px) 0 min(8vw,116px)}
.metin-sayfa .kap{max-width:920px}
.ust-not{font:500 min(1.05vw,15px)/1 var(--f);color:var(--mavi)}
.metin-sayfa h1{margin:16px 0 0;font-size:min(4.4vw,60px);font-weight:650;line-height:1.08;letter-spacing:-0.025em}
.metin-sayfa .giris-metni{margin-top:20px;max-width:36em;font-size:min(1.35vw,19.5px);line-height:1.6;color:var(--kursun)}
.metin-sayfa h2{margin:min(4vw,52px) 0 12px;font:600 min(1.9vw,26px)/1.25 var(--f);letter-spacing:-0.01em}
.metin-sayfa p,.metin-sayfa li{font-size:min(1.15vw,16.5px);line-height:1.7;color:#2c2b28}
.metin-sayfa p{margin:0 0 12px;max-width:44em}
.metin-sayfa ul{margin:0 0 12px;padding-left:1.2em;max-width:44em}
.metin-sayfa li{margin-bottom:6px}
.metin-sayfa a{color:var(--mavi-koyu,#0B6FE8);text-decoration:underline;text-underline-offset:3px}
.kunye{display:grid;grid-template-columns:auto 1fr;gap:8px 24px;margin:0 0 12px;padding:20px 22px;border:1px solid #dcd7cc;border-radius:14px;background:rgba(255,255,255,.5);font-size:min(1.1vw,16px)}
.kunye dt{color:var(--kursun)}
.kunye dd{margin:0;font-weight:500}
.metin-sayfa .tarih{margin-top:min(4vw,52px);font-size:14px;color:var(--kursun)}
.urun-satir{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;margin:min(3vw,40px) 0}
.urun-satir a{display:flex;flex-direction:column;gap:14px;min-height:170px;padding:24px;border:1px solid #dcd7cc;border-radius:18px;background:rgba(255,255,255,.55);text-decoration:none;color:inherit;transition:border-color .2s}
.urun-satir a:hover{border-color:#111}
.urun-satir img{height:34px;width:auto;align-self:flex-start}
.urun-satir span{font-size:15px;line-height:1.55;color:var(--kursun)}
.urun-satir b{font:700 30px/1 var(--f);letter-spacing:-.03em}
.urun-satir .yakinda{opacity:.6;pointer-events:none}
.metin-eskiz{margin:min(4vw,52px) 0;border-radius:18px;overflow:hidden;background:#E5E0D8}
.metin-eskiz img{display:block;width:100%;height:auto;mix-blend-mode:multiply}
.metin-sayfa .btn{height:56px;padding:0 28px;margin-top:10px;color:#fff;text-decoration:none}
'''
MOBIL = '''  .metin-sayfa{padding:40px 0 64px}
  .metin-sayfa h1{font-size:clamp(2.1rem,9vw,3rem)}
  .metin-sayfa .giris-metni{font-size:1.05rem}
  .metin-sayfa h2{font-size:1.3rem;margin-top:40px}
  .metin-sayfa p,.metin-sayfa li{font-size:1rem}
  .kunye{grid-template-columns:1fr;gap:2px;font-size:15px}
  .kunye dd{margin-bottom:10px}
  .urun-satir{grid-template-columns:1fr}
'''

def metin_sayfasi(dosya, baslik, aciklama, govde, taban=None, veriler=()):
    O.sayfa(dosya, baslik, aciklama, css=CSS.strip(), mobil=MOBIL.rstrip(),
            govde=f'<main class="metin-sayfa">\n  <div class="kap">\n{govde}\n  </div>\n</main>', yazi_tipi='metin',
            taban=taban, veriler=veriler, dizinle=taban is None)


YER = lambda ad, metin: f'<span data-bag-metin="{ad}">{metin}</span>'
KVKK = f'''    <p class="ust-not">KVKK ve gizlilik</p>
    <h1>Kişisel verileriniz hakkında</h1>
    <p class="giris-metni">Bu sayfa, kroki web sitesini ve sitedeki “Bize yazın” formunu kullandığınızda hangi bilgilerinizin, neden ve nasıl işlendiğini anlatır.</p>

    <h2>Veri sorumlusu</h2>
    <p>Bu aydınlatma metni, 6698 sayılı Kişisel Verilerin Korunması Kanunu’nun (KVKK) 10. maddesi uyarınca veri sorumlusu sıfatıyla aşağıdaki şirket tarafından hazırlanmıştır.</p>
    <dl class="kunye">
      <dt>Unvan</dt><dd>{YER('sirketUnvan', '[Şirket unvanı]')}</dd>
      <dt>Adres</dt><dd>{YER('sirketAdres', '[Adres]')}</dd>
      <dt>MERSİS no</dt><dd>{YER('mersis', '[MERSİS numarası]')}</dd>
      <dt>E-posta</dt><dd>{YER('eposta', '[E-posta]')}</dd>
      <dt>KEP</dt><dd>{YER('kep', '[KEP adresi]')}</dd>
    </dl>

    <h2>Hangi bilgileri işliyoruz?</h2>
    <p>Yalnızca “Bize yazın” formunu doldurduğunuzda, formda yazdıklarınızı işleriz:</p>
    <ul>
      <li><b>Kimlik:</b> ad ve soyad.</li>
      <li><b>İletişim:</b> telefon numarası ya da e-posta adresi.</li>
      <li><b>Talep:</b> stüdyo adı, ilgilendiğiniz ürün ve mesajınız.</li>
      <li><b>İşlem güvenliği:</b> formun gönderildiği tarih ve saat.</li>
    </ul>
    <p>Siteyi yalnızca gezmeniz için sizden bilgi istemeyiz ve siteye üyelik yoktur.</p>

    <h2>Neden işliyoruz?</h2>
    <ul>
      <li>Başvurunuza dönüş yapmak; demo, paket ve fiyat sorularınızı yanıtlamak,</li>
      <li>İstediğiniz ürün için size teklif hazırlamak,</li>
      <li>Formun kötüye kullanılmasını önlemek.</li>
    </ul>
    <p>Bu bilgiler, KVKK’nın 5/2-c maddesi (bir sözleşmenin kurulmasıyla doğrudan ilgili olması) ve 5/2-f maddesi (temel hak ve özgürlüklerinize zarar vermemek kaydıyla meşru menfaatimiz) kapsamında işlenir. Size kampanya ya da bülten göndermeyiz; bunun için ayrıca onayınızı isteriz.</p>

    <h2>Kimlerle paylaşıyoruz?</h2>
    <ul>
      <li><b>Barındırma:</b> site ve form başvuruları Google LLC’nin Firebase hizmetinde saklanır. Sunucular yurt dışında olabileceğinden bu, KVKK’nın 9. maddesi kapsamında yurt dışına aktarım sayılır ve kanunda öngörülen güvenceler çerçevesinde yapılır.</li>
      <li><b>Yazı tipleri:</b> sayfadaki yazı tipleri Google Fonts’tan yüklenir. Bu sırada tarayıcınızın IP adresi Google’a iletilir.</li>
      <li><b>Yetkili kurumlar:</b> yalnızca kanunen zorunlu olduğunda.</li>
    </ul>

    <h2>Ne kadar süre saklıyoruz?</h2>
    <p>Başvurunuz sonuçlandıktan sonra en fazla bir yıl saklar, sonra sileriz. Daha önce silinmesini isterseniz yukarıdaki e-posta adresine yazmanız yeterli.</p>

    <h2>Haklarınız</h2>
    <p>KVKK’nın 11. maddesi uyarınca; verilerinizin işlenip işlenmediğini öğrenme, işlenmişse bilgi isteme, işleme amacını ve amacına uygun kullanılıp kullanılmadığını öğrenme, aktarıldığı kişileri bilme, eksik ya da yanlışsa düzeltilmesini, silinmesini ya da yok edilmesini isteme, bu işlemlerin aktarılan kişilere bildirilmesini isteme, otomatik sistemlerle analiz sonucu aleyhinize bir sonuca itiraz etme ve kanuna aykırı işleme nedeniyle zararın giderilmesini isteme haklarına sahipsiniz.</p>
    <p>Başvurunuzu yukarıdaki e-posta ya da KEP adresine yazılı olarak iletebilirsiniz. Başvurunuzu en geç 30 gün içinde sonuçlandırırız.</p>

    <h2>Çerezler</h2>
    <p>Bu site çerez kullanmaz ve sizi izleyen bir analiz ya da reklam aracı içermez. Tarayıcınızda yalnızca sitenin çalışması için gereken küçük ayarlar tutulur; bunlar kimseyle paylaşılmaz.</p>

    <h2>Uygulamalar</h2>
    <p>kroki crm ve pafta. uygulamalarını kullandığınızda işlenen veriler, uygulamaların kendi aydınlatma metinlerinde ve kullanım sözleşmelerinde anlatılır.</p>

    <p class="tarih">Son güncelleme: 27 Ekim 2026</p>'''

HAKKIMIZDA = '''    <p class="ust-not">Hakkımızda</p>
    <h1>Mimarlar için yazılım.</h1>
    <p class="giris-metni">Kroki, iç mimarlık ve mimarlık stüdyoları için yazılım geliştirir. Sahada alınan ölçüden ofisteki teklife, şantiyeden tahsilata kadar her gün yapılan işleri aynı planda topluyoruz.</p>

    <div class="urun-satir">
      <a href="kroki-crm.html"><img src="assets/kroki-crm.png" alt="kroki crm" width="900" height="278"><span>Müşteriler, şantiyeler, takvim ve tahsilat. Stüdyonun bütün işi tek uygulamada.</span></a>
      <a href="pafta.html"><img src="assets/pafta-logo.svg" alt="pafta." width="640" height="206"><span>Röleveyi telefonla alın; duvarlar, kirişler ve ölçüler plana kendiliğinden yazılsın.</span></a>
      <a class="yakinda" aria-disabled="true"><b>scroll.</b><span>Yakında. Ekosistemin üçüncü parçası üzerinde çalışıyoruz.</span></a>
    </div>

    <h2>Aynı plan, farklı araçlar</h2>
    <p>Bir projede müşteri, ölçü, çizim, şantiye ve para ayrı ayrı yerlerde tutulunca işler dağılır. Kroki’nin her ürünü bu işin bir parçasını üstlenir; hepsi aynı mantıkla, aynı dille çalışır.</p>

    <figure class="metin-eskiz"><img src="assets/bant-eskiz.webp" alt="Kalemle çizilmiş modern bir bina eskizi" width="1536" height="360" loading="lazy"></figure>

    <h2>Nasıl çalışıyoruz</h2>
    <p>Ürünlerimizi stüdyoların gündelik işinden yola çıkarak tasarlıyoruz: önce sahada ve ofiste ne yapıldığına bakıyor, sonra o işi kısaltan en sade aracı yapıyoruz. Her yeni özellik, onu kullanacak iç mimarlarla birlikte deneniyor.</p>

    <h2>Bize ulaşın</h2>
    <p>Demo, işbirliği ya da sorularınız için yazın; en kısa sürede dönüş yapalım.</p>
    <a class="btn" href="kroki-web.html#iletisim">Bize yazın</a>'''

metin_sayfasi('kvkk.html', 'KVKK ve gizlilik — Kroki', 'Kroki web sitesinde ve iletişim formunda kişisel verilerin işlenmesine ilişkin aydınlatma metni, gizlilik ve çerezler.', KVKK)
metin_sayfasi('hakkimizda.html', 'Hakkımızda — Kroki', 'Kroki, iç mimarlık ve mimarlık stüdyoları için yazılım geliştirir: kroki crm, pafta. ve yakında scroll.', HAKKIMIZDA, veriler=[O.kurulus()])
YOK = """    <p class="ust-not">404</p>
    <h1>Bu sayfa henüz çizilmedi.</h1>
    <p class="giris-metni">Aradığınız sayfa taşınmış ya da hiç var olmamış olabilir. Buradan devam edebilirsiniz:</p>
    <div class="urun-satir">
      <a href="kroki-web.html"><b>Kroki</b><span>Ana sayfa</span></a>
      <a href="kroki-crm.html"><img src="assets/kroki-crm.png" alt="kroki crm" width="900" height="278"><span>Stüdyo yönetimi</span></a>
      <a href="pafta.html"><img src="assets/pafta-logo.svg" alt="pafta." width="640" height="206"><span>Röleve ve ölçü</span></a>
    </div>"""
# Firebase Hosting bilinmeyen adreslerde 404.html'i gösterir; adres derinse göreli bağlantılar bozulmasın diye kök adres
metin_sayfasi('404.html', 'Sayfa bulunamadı — Kroki', 'Aradığınız sayfa bulunamadı.', YOK, taban='/')
