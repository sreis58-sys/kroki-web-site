"""kroki-crm.html: uygulama tanıtım sayfası, pafta.html ile aynı temel. Girişte karakalem stüdyo eskizi; kaydırınca masadaki
telefon kalkar ve ekranları sırayla gösterir. Ardından bilgisayar ve telefon ekranlarıyla özellikler, adımlar, bant, paketler,
SSS, pafta bandı ve kapanış. Ürün sayfalarının ortak stilleri pafta_v2.py'den alınır."""
import ortak as O
import pafta_v2 as P
import pafta_ekranlar as E
import crm_ekranlar as C
from ortak import ANA_CSS, ANA_MOBIL, magaza

# ürün sayfalarının ortak stilleri pafta_v2.py'den: ızgara zemini, telefon çerçevesi … nasıl çalışır, ekosistem … sonu
ORTAK_CSS = (O.kes(P.CSS, '.izgara{', '\n') + '\n' + O.kes(P.CSS, '/* ---------- telefon çerçevesi', '/* ---------- ekosistem bandı')
             + O.kes(P.CSS, '/* ---------- ekosistem bandı'))
ORTAK_MOBIL = O.kes(P.MOBIL, '  .cep{padding:7px;')
LOGO_ACIK = 'assets/kroki-crm-acik.png'

CSS = r'''
main{position:relative}

/* ---------- giriş: ana sayfadaki gibi karakalem eskiz; mavi düzlemler paftalarda, telefon masanın üstünde ---------- */
.giris-c{position:relative;min-height:min(52vw,750px)}
.giris-c__eskiz{position:absolute;right:0;top:max(-2vw,-29px);width:min(79.9vw,1150px)}
.giris-c__eskiz img{width:100%;height:auto}
.giris-c__eskiz svg{position:absolute;inset:0;width:100%;height:100%}
.giris-c__eskiz .duzlem{fill:var(--mavi);mix-blend-mode:multiply;opacity:.88}
.giris-c__yer{position:absolute;left:38.5%;top:47%;width:15.5%;aspect-ratio:.47}  /* telefonun masadaki yeri: sahne buradan başlar */

/* ---------- giriş sahnesi: kaydırdıkça telefon masadan kalkar, karşıya döner, ekranları sırayla gösterir ---------- */
.sinema-c{position:relative;height:850vh}           /* her ekran yaklaşık iki ekran boyu kaydırma ister */
.sinema-c__sahne{position:sticky;top:0;height:100vh;height:100svh;overflow:hidden}
.sinema-c__cep{position:absolute;left:0;top:0;z-index:3;width:calc(min(78vh,760px) * .47);will-change:transform}
.js .sinema-c__cep{visibility:hidden}
.sinema-c__ekran{position:absolute;inset:0}
.sinema-c__ekran + .sinema-c__ekran{opacity:0}
.sinema-c__ekran .ekran{display:block;width:100%;height:100%}
.sinema-c__yazilar{position:absolute;left:var(--kenar);top:50%;z-index:2;width:min(36vw,500px);height:20em;margin-top:-10em;pointer-events:none}
.sinema-c__yazi{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;opacity:0}
.sinema-c__yazi i{margin-bottom:16px;font:500 min(1.05vw,15px)/1 var(--f);font-style:normal;color:var(--mavi)}
.sinema-c__yazi b{font:600 min(3.6vw,52px)/1.08 var(--f);letter-spacing:-0.028em}
.sinema-c__yazi > span{max-width:24em;margin-top:18px;font-size:min(1.3vw,19px);line-height:1.6;color:var(--kursun)}
.sinema-c__yazi .not{position:relative;left:auto;top:auto;margin-top:34px;font-size:min(1.15vw,16.5px)}
@media (prefers-reduced-motion:reduce){.sinema-c{height:auto}.sinema-c__sahne{position:relative;height:auto}.sinema-c__yazilar{display:none}}
.giris-c__eskiz .not{left:15%;top:7%}
.giris-c__metin{position:relative;z-index:2;padding-top:min(6vw,86px)}
.giris-c__metin > div{max-width:min(36vw,520px)}
.giris-c__logo{height:min(3.6vw,52px);width:auto}
.giris-c h1{margin:min(2.6vw,38px) 0 0;font-size:min(4.9vw,70px);font-weight:650;line-height:1.08;letter-spacing:-0.028em}
.giris-c__alt{margin-top:min(1.6vw,22px);max-width:25em;font-size:min(1.3vw,19px);line-height:1.6;color:var(--kursun)}
.giris-c__eylem{display:flex;flex-wrap:wrap;align-items:center;gap:14px 28px;margin-top:min(2.8vw,40px)}
.giris-c__not{margin-top:min(1.8vw,24px);font-size:min(.95vw,13.5px);color:#86837b}

/* ---------- özellikler: bilgisayar ekranı, önünde telefon; görsel sütunu daha geniş ---------- */
.ozellik--genis{grid-template-columns:minmax(0,4fr) minmax(0,7fr);gap:min(5vw,72px)}
.ozellik--genis.ozellik--ters{grid-template-columns:minmax(0,7fr) minmax(0,4fr)}
.cift{position:relative;width:100%;padding:0 0 min(3vw,40px)}
.cift--dar{width:82%}
.ekran-pc{overflow:hidden;border:1px solid #2A2E31;border-radius:min(1.2vw,16px);background:#0B0C0D;box-shadow:0 40px 80px -36px rgba(20,24,30,.5)}
.ekran-pc img{display:block;width:100%;height:auto}
.ozellik__gorsel .cift .cep{position:absolute;right:-3%;bottom:0;width:15%;padding:min(.5vw,7px);border-radius:min(2.2vw,30px)}
.cift .cep__ekran{border-radius:min(1.7vw,24px)}
.ozellik--ters .ozellik__gorsel .cift .cep{right:auto;left:-3%}
.ozellik__gorsel .not:has(+ .cift){left:0;top:auto;bottom:calc(100% + 18px)}
.ozellik--ters .ozellik__gorsel .not:has(+ .cift){left:auto;right:0}
.adim .hap{background:#111;font-family:var(--f)}
.adim .hap--cizgi{background:none;border:1.5px solid #111;color:#111}
.adim__ui{gap:10px;flex-wrap:wrap}

/* el yazısı kenar notları: telefonların yanında, mimarın paftaya düştüğü notlar gibi */
/* telefon sütunun dış kenarına yaslanır, not iç taraftaki boşlukta durur */
.ozellik__gorsel:has(> .not){justify-content:flex-end}
.ozellik--ters .ozellik__gorsel:has(> .not){justify-content:flex-start}
.ozellik__gorsel .not{left:6%;top:10%;font-size:min(1.15vw,16.5px)}
.ozellik--ters .ozellik__gorsel .not{left:auto;right:6%}

.metin-link{padding-bottom:4px;border-bottom:1.5px solid currentColor;font:500 min(1.1vw,16px)/1 var(--f);transition:color .2s}
.metin-link:hover{color:var(--mavi)}

/* ---------- paketler ---------- */
.paketler__izgara{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:min(1.4vw,20px);margin-top:min(4vw,56px)}
.paket{position:relative;display:flex;flex-direction:column;padding:min(2.4vw,34px);border:1px solid #d6d0c3;border-radius:18px;background:rgba(255,255,255,.4)}
.paket[data-onerilen]{border-color:var(--mavi);box-shadow:inset 0 0 0 1px var(--mavi)}
.paket h3{margin:0;font:600 min(1.6vw,23px)/1.2 var(--f)}
.paket__kim{margin-top:6px;font:400 min(1vw,14.5px)/1.5 var(--f);color:#77746c}
.paket__fiyat{margin-top:min(2vw,28px);font:600 min(2.6vw,38px)/1 var(--f);letter-spacing:-0.02em}
.paket__fiyat small{font-size:.4em;font-weight:400;letter-spacing:0;color:#77746c}
.paket ul{list-style:none;margin:min(2vw,28px) 0;padding:0;display:grid;gap:12px;font:400 min(1.02vw,14.5px)/1.45 var(--f);color:#2a2a2a}
.paket li{display:flex;gap:10px}
.paket li::before{content:"";flex:none;width:7px;height:7px;margin-top:.5em;background:#151515;opacity:.55}
.paket[data-onerilen] li::before{background:var(--mavi);opacity:1}
.paket__btn{display:inline-flex;align-items:center;justify-content:center;margin-top:auto;height:min(3.3vw,48px);border:1.5px solid #bdb7aa;border-radius:10px;font:500 min(1.05vw,15px)/1 var(--f);transition:border-color .2s,background-color .2s}
.paket__btn:hover{border-color:#151515}
.paket[data-onerilen] .paket__btn{background:#0B6FE8;border-color:#0B6FE8;color:#fff}
.paket[data-onerilen] .paket__btn:hover{background:#095BC0;border-color:#095BC0}
.paket__etiket{position:absolute;top:-11px;left:min(2.4vw,34px);padding:6px 10px;border-radius:6px;background:#0B6FE8;font:600 11px/1 var(--f);letter-spacing:.04em;color:#fff}
.paketler__not{margin-top:22px;font-size:min(.98vw,14px);color:#86837b}
'''
MOBIL = r'''
  .sinema-c{height:750vh}
  .sinema-c__cep{width:calc(min(60vh,540px) * .47)}
  .sinema-c__yazilar{left:20px;right:20px;top:auto;bottom:20px;width:auto;height:8em;margin-top:0}
  .sinema-c__yazi{justify-content:flex-end;align-items:center;text-align:center}
  .sinema-c__yazi i{margin-bottom:8px;font-size:13px}
  .sinema-c__yazi b{font-size:1.45rem}
  .sinema-c__yazi > span{margin-top:8px;font-size:.95rem}
  .sinema-c__yazi .not{display:none}
  .giris-c{min-height:0;display:flex;flex-direction:column;overflow:hidden;padding-bottom:48px}
  .giris-c__eskiz{position:relative;order:-1;top:0;width:150%;margin-left:-38%}
  .giris-c__eskiz .not{left:30%;top:4%;font-size:12px}
  .giris-c__metin{padding-top:8px}
  .giris-c__metin > div{max-width:none}
  .giris-c__logo{height:38px}
  .giris-c h1{margin-top:22px;font-size:clamp(2.3rem,9.5vw,3.4rem)}
  .giris-c__alt{font-size:1.05rem}
  .giris-c__not{font-size:13.5px}
  .not{font-size:12px}
  .ozellik__gorsel:has(> .not){justify-content:center}
  .ozellik__gorsel .not,.ozellik--ters .ozellik__gorsel .not{position:relative;left:auto;right:auto;top:auto;bottom:auto;align-self:flex-start;margin:0 0 18px;font-size:12px}
  .ozellik__gorsel:has(> .not){flex-direction:column;align-items:center}
  .ozellik--genis,.ozellik--genis.ozellik--ters{grid-template-columns:1fr}
  .cift,.cift--dar{width:100%;padding-bottom:34px}
  .ozellik__gorsel .cift .cep{right:0;width:22%;padding:4px;border-radius:18px}
  .cift .cep__ekran{border-radius:14px}
  .ozellik--ters .ozellik__gorsel .cift .cep{left:0}
  .metin-link{font-size:1rem}
  .paketler__izgara{grid-template-columns:1fr;gap:28px;margin-top:36px}
  .paket{padding:30px 26px}
  .paket h3{font-size:1.35rem}
  .paket__kim{font-size:14px}
  .paket__fiyat{font-size:2.2rem;margin-top:22px}
  .paket ul{font-size:15px;margin:22px 0}
  .paket__btn{height:48px;font-size:15px}
  .paket__etiket{left:26px}
  .paketler__not{font-size:14px}
'''

YAZILAR = [('Panel', 'Güne sıradaki işle başlayın.', 'Panel, sıradaki işi ve günün listesini öne çıkarır. Yeni müşteri ya da randevu tek dokunuşta.', ('Sıradaki iş', 'hep', 'önde.')),
           ('Müşteriler', 'Her müşteri tek kartta.', 'Aşamasına göre süzün, adıyla arayın; tek dokunuşla arayın ya da WhatsApp’tan yazın.', ('Tek dokunuşla', 'WhatsApp.')),
           ('Takvim', 'Randevular tek takvimde.', 'Ölçü, sunum ve şantiye ziyaretleri gün, hafta ve ay görünümünde. Biten işlerin üstü çizilir.', ('Biten işin', 'üstü', 'çizilir.')),
           ('Muhasebe', 'Gelen, giden, kalan.', 'Ayın tahsilatları, ödemeleri ve kalan net tek ekranda.', ('Ay sonu', 'sürpriz', 'yok.'))]
yazilar_html = '\n'.join(f'''        <div class="sinema-c__yazi"><i>{ad}</i><b>{bas}</b><span>{alt}</span><p class="not">{''.join(f'<span>{t}</span>' for t in not_)}</p></div>''' for ad, bas, alt, not_ in YAZILAR)
sinema_cep = ('<div class="cep"><div class="cep__ekran">'
              + ''.join(f'<div class="sinema-c__ekran">{ekran}</div>' for ekran in (C.panel('s1', LOGO_ACIK), C.musteriler('s2', LOGO_ACIK), C.takvim('s3', LOGO_ACIK), C.muhasebe('s4', LOGO_ACIK)))
              + '<span class="cep__ada" aria-hidden="true"></span></div></div>')

GOVDE = f'''  <section class="sinema-c" aria-labelledby="giris-baslik">
  <div class="sinema-c__sahne">
  <div class="giris-c">
    <div class="giris-c__eskiz">
      <img src="assets/crm-eskiz.webp" width="1536" height="1024" alt="Kalemle çizilmiş bir iç mimarlık stüdyosu: çizim masası, malzeme örnekleri, raf ve duvarda iki pafta">
      <!-- mavi düzlemler görselin piksel koordinatlarında: duvardaki iki paftada ve masadaki planda birer oda -->
      <svg viewBox="0 0 1536 1024" aria-hidden="true">
          <polygon class="duzlem" points="1232,310 1264,310 1264,372 1232,372"/>
          <polygon class="duzlem" points="1384,230 1414,230 1414,282 1384,282"/>
          <polygon class="duzlem" points="1128,602 1185,592 1195,610 1135,620"/>
      </svg>
      <p class="not" aria-hidden="true"><span>Paftalar</span><span>duvarda,</span><span>işler cebinde.</span></p>
      <span class="giris-c__yer" aria-hidden="true"></span>
    </div>
    <div class="kap giris-c__metin">
      <div>
        <img class="giris-c__logo" src="assets/kroki-crm.png" alt="kroki crm" width="900" height="278">
        <h1 id="giris-baslik">Dağınık işler, tek planda.</h1>
        <p class="giris-c__alt">Müşteri, şantiye, takvim ve tahsilat. İç mimarlık stüdyoları için tek uygulamada.</p>
        <div class="giris-c__eylem">
          {magaza('crm', 'kroki crm')}
          <a class="metin-link" href="#paketler">Paketleri gör</a>
        </div>
        <p class="giris-c__not">14 gün boyunca Stüdyo paketinin tamamı ücretsiz.</p>
      </div>
    </div>
  </div>
    <div class="sinema-c__cep">{sinema_cep}</div>
    <div class="sinema-c__yazilar" aria-hidden="true">
{yazilar_html}
    </div>
  </div>
  </section>

  <section class="kap" aria-label="Kısaca kroki crm">
    <div class="bilgiler">
      <div><h3>Müşteri kartı</h3><p>İletişim, projeler, teklifler ve notlar tek yerde.</p></div>
      <div><h3>Satış hattı</h3><p>Randevudan anlaşmaya, her müşteri hangi aşamada.</p></div>
      <div><h3>Şantiye ve takvim</h3><p>Aşamalar, ustalar ve randevular aynı planda.</p></div>
      <div><h3>Teklif ve tahsilat</h3><p>Teklif ve sözleşme PDF, ödemeler ve makbuz.</p></div>
    </div>
  </section>

  <section class="kap bolum" aria-labelledby="ozellik-baslik">
    <div class="bolum__bas">
      <h2 id="ozellik-baslik">Stüdyonun bütün işi, tek ekranda.</h2>
      <p>Ofiste bilgisayarda, şantiyede telefonda: aynı müşteriler, aynı takvim, aynı hesap.</p>
    </div>

    <div class="ozellik ozellik--genis">
      <div>
        <p class="ozellik__ad">Panel</p>
        <h3>Güne sıradaki işle başlayın.</h3>
        <p>Sıradaki iş, günün listesi, müşteri ve şantiye sayıları, satış hattı; ofiste bilgisayarda, şantiyede telefonda aynı panel.</p>
        <ul><li>Sıradaki iş ve bugünkü işler</li><li>Bir bakışta müşteri, satış ve şantiye</li><li>Tek tıkla yeni müşteri ve randevu</li></ul>
      </div>
      <div class="ozellik__gorsel"><p class="not" aria-hidden="true"><span>Sıradaki iş</span><span>hep önde.</span></p><div class="cift"><div class="ekran-pc"><img src="assets/crm-pc-panel.webp" alt="kroki crm Panel ekranı bilgisayarda: sıradaki iş, bugünkü işler, bir bakışta sayılar ve satış hattı" width="1919" height="868" loading="lazy"></div>{E.telefon(C.panel('o1', LOGO_ACIK))}</div></div>
    </div>
    <div class="ozellik ozellik--genis ozellik--ters">
      <div>
        <p class="ozellik__ad">Müşteriler</p>
        <h3>Her müşteri tek kartta.</h3>
        <p>Müşterileri aşamasına göre süzün, adına ya da proje tipine göre arayın; telefonla veya WhatsApp’tan tek dokunuşla ulaşın. Ustalarınız da ayrı bir listede.</p>
        <ul><li>Aşamaya göre süzme ve arama</li><li>Arama ve WhatsApp kısayolu</li><li>Ustalar listesi</li></ul>
      </div>
      <div class="ozellik__gorsel"><p class="not" aria-hidden="true"><span>Tek dokunuşla</span><span>WhatsApp.</span></p><div class="cift"><div class="ekran-pc"><img src="assets/crm-pc-musteriler.webp" alt="kroki crm Müşteriler ekranı bilgisayarda: aşamalarıyla müşteri listesi, arama ve WhatsApp düğmeleri" width="1919" height="743" loading="lazy"></div>{E.telefon(C.musteriler('o2', LOGO_ACIK))}</div></div>
    </div>
    <div class="ozellik ozellik--genis">
      <div>
        <p class="ozellik__ad">Şantiye</p>
        <h3>Şantiyeler aşama aşama.</h3>
        <p>Tasarımdan uygulamaya, son rötuşlardan teslime; her şantiyenin süreci, kontrol listesi, notları ve parası kendi kartında.</p>
        <ul><li>Tasarım & Proje, Uygulama, Son Rötuşlar, Teslim</li><li>Kontrol listesi ve şantiye notları</li><li>Tahsil edilen, ustalara ödenen, kalan</li></ul>
      </div>
      <div class="ozellik__gorsel"><p class="not" aria-hidden="true"><span>Kontrol listesi</span><span>hep elinde.</span></p><div class="cift cift--dar"><div class="ekran-pc"><img src="assets/crm-pc-santiye.webp" alt="kroki crm şantiye kartı: şantiye süreci, kontrol listesi, tahsil edilen ve ustalara ödenen tutarlar, şantiye notları" width="918" height="1028" loading="lazy"></div></div></div>
    </div>
    <div class="ozellik ozellik--genis ozellik--ters">
      <div>
        <p class="ozellik__ad">Takvim</p>
        <h3>Randevular tek takvimde.</h3>
        <p>Ölçü, sunum, teklif ve şantiye ziyaretleri gün, hafta ve ay görünümünde. Biten işlerin üstü çizilir; randevu, şantiye ve ödeme kendi renginde.</p>
        <ul><li>Gün, hafta ve ay görünümü</li><li>Randevu, şantiye ve ödeme renkleri</li><li>Seçili günün işleri yanda</li></ul>
      </div>
      <div class="ozellik__gorsel"><p class="not" aria-hidden="true"><span>Biten işin</span><span>üstü çizilir.</span></p><div class="cift"><div class="ekran-pc"><img src="assets/crm-pc-takvim.webp" alt="kroki crm Takvim ekranı bilgisayarda: ekim ayı, renkli işler ve seçili günün listesi" width="1919" height="978" loading="lazy"></div>{E.telefon(C.takvim('o3', LOGO_ACIK))}</div></div>
    </div>
    <div class="ozellik ozellik--genis">
      <div>
        <p class="ozellik__ad">Sözleşme</p>
        <h3>Teklif ve sözleşme tek formda.</h3>
        <p>Anahtar teslim ya da tasarım teklifi seçin, iş kalemlerini ve ödeme planını girin. Belge özeti siz yazdıkça hazırlanır, sözleşme metni tek tuşla oluşur.</p>
        <ul><li>Anahtar teslim ve tasarım teklifi</li><li>İş kalemleri ve ödeme planı</li><li>Sözleşme metni tek tuşla</li></ul>
      </div>
      <div class="ozellik__gorsel"><p class="not" aria-hidden="true"><span>Tek tuşla</span><span>sözleşme.</span></p><div class="cift cift--dar"><div class="ekran-pc"><img src="assets/crm-pc-sozlesme.webp" alt="kroki crm sözleşme formu: anahtar teslim teklif, ödeme planı, iç mimar ve belge özeti" width="918" height="1028" loading="lazy"></div></div></div>
    </div>
    <div class="ozellik ozellik--genis ozellik--ters">
      <div>
        <p class="ozellik__ad">Muhasebe</p>
        <h3>Gelen, giden, kalan.</h3>
        <p>Müşterilerden beklenen ve ustalara kalan borç en üstte; ay ay gelen, giden ve net. Bütün hareketler tek listede, tek tıkla Excel’e.</p>
        <ul><li>Müşterilerden beklenen, ustalara kalan borç</li><li>Aylık gelen, giden ve net</li><li>Excel’e aktarma</li></ul>
      </div>
      <div class="ozellik__gorsel"><p class="not" aria-hidden="true"><span>Ay sonu</span><span>sürpriz yok.</span></p><div class="cift"><div class="ekran-pc"><img src="assets/crm-pc-muhasebe.webp" alt="kroki crm Muhasebe ekranı bilgisayarda: genel durum, aylık gelen, giden ve net, hareketler" width="1919" height="888" loading="lazy"></div>{E.telefon(C.muhasebe('o4', LOGO_ACIK))}</div></div>
    </div>
  </section>

  <section class="kap bolum" id="nasil" aria-labelledby="nasil-baslik">
    <div class="bolum__bas">
      <h2 id="nasil-baslik">Üç adımda düzen.</h2>
      <p>Müşteri geldiği andan tahsilata kadar her iş aynı yerde ilerler.</p>
    </div>
    <ol class="adimlar">
      <li class="adim">
        <span class="adim__sira">1. adım</span>
        <h3>Müşteriyi ekleyin.</h3>
        <p>Adı, telefonu ve proje tipi yeter; müşteri satış hattına girer.</p>
        <div class="adim__ui" aria-hidden="true"><span class="hap">+ Yeni Müşteri</span></div>
      </li>
      <li class="adim">
        <span class="adim__sira">2. adım</span>
        <h3>Randevuyu takvime koyun.</h3>
        <p>Ölçü, sunum ya da şantiye ziyareti; günü gelince Panel’de sıradaki iş olur.</p>
        <div class="adim__ui" aria-hidden="true"><span class="hap">+ Randevu Ekle</span></div>
      </li>
      <li class="adim">
        <span class="adim__sira">3. adım</span>
        <h3>Sözleşmeyi yapın, tahsil edin.</h3>
        <p>Sözleşme metni tek tuşla oluşur; ödemeler geldikçe muhasebeye işlenir.</p>
        <div class="adim__ui" aria-hidden="true"><span class="hap hap--cizgi">Sözleşme Metnini Oluştur</span><span class="hap">+ Ödeme</span></div>
      </li>
    </ol>
  </section>

  <section class="bant" aria-label="kroki crm'in yaklaşımı">
    <div class="bant__ic">
      <p class="bant__metin">Her iş<br>yerli<br>yerinde.</p>
      <div class="bant__eskiz" aria-hidden="true">
        <img src="assets/crm-bant.webp" alt="" width="1536" height="350" loading="lazy">
        <svg viewBox="0 0 1536 350"><polygon class="mavi" points="1237,78 1287,68 1287,263 1237,255"/><polygon class="mavi" points="1296,66 1354,54 1354,274 1296,264"/></svg>
      </div>
    </div>
  </section>

  <section class="kap bolum" id="paketler" aria-labelledby="paketler-baslik">
    <div class="bolum__bas">
      <h2 id="paketler-baslik">Stüdyonuza uygun paketi seçin.</h2>
      <p>Paket değiştirdiğinizde verileriniz silinmez; yalnızca açık bölümler değişir.</p>
    </div>
    <!-- paketler admin panelinden yönetilir; bu hâl başlangıç içeriğidir: assets/site-icerik.js -->
    <div class="paketler__izgara" data-paketler data-hedef="#indir">
{O.paketler_html('#indir')}
    </div>
    <p class="paketler__not">Fiyatlar aylıktır. 14 gün boyunca Stüdyo paketi ücretsiz. Abonelik App Store ve Google Play üzerinden.</p>
  </section>

  <section class="kap bolum sss" id="sss" aria-labelledby="sss-baslik">
    <div class="bolum__bas"><h2 id="sss-baslik">Sık sorulan sorular</h2></div>
    <div class="sss__liste">
      <details><summary>Deneme süresinde neler açık?</summary><p>14 gün boyunca Stüdyo paketinin tamamı açık. Siz ve üç çalışanınız, dört kişiye kadar birlikte deneyebilirsiniz.</p></details>
      <details><summary>Paket değiştirince verilerim silinir mi?</summary><p>Hayır. Paket ya da yetki değişikliği veriyi silmez; yalnızca açık bölümler değişir.</p></details>
      <details><summary>Ekibimi nasıl eklerim?</summary><p>Stüdyo paketinde 3, Ofis paketinde 10 çalışan davet edebilirsiniz. Muhasebe izni kapalı çalışan sözleşmeleri görür, diğer finans verilerini görmez.</p></details>
      <details><summary>Bilgisayarda da kullanabilir miyim?</summary><p>Evet. Aynı hesapla telefonda uygulamadan, bilgisayarda tarayıcıdan girersiniz; müşteriler, takvim ve muhasebe ikisinde de aynıdır.</p></details>
      <details><summary>Verilerim güvende mi?</summary><p>Veriler Google’ın Firebase altyapısında saklanır. Her stüdyo yalnızca kendi verisini görür; başka bir stüdyonun bilgisine erişemez.</p></details>
      <details><summary>Ödeme nasıl yapılır?</summary><p>Abonelik aylıktır ve App Store ya da Google Play üzerinden alınır.</p></details>
    </div>
  </section>

  <section class="kap">
    <div class="ekosistem">
      <img src="assets/pafta-logo.svg" alt="pafta." width="640" height="206" loading="lazy">
      <p>Sahadaki ölçü ve röleve için pafta. Aynı ekosistemin öteki parçası.</p>
      <a class="metin-link" href="pafta.html">pafta.’yı tanıyın</a>
    </div>
  </section>

  <section class="kapanis" id="indir" aria-labelledby="indir-baslik">
    <div class="izgara" aria-hidden="true"></div>
    <div class="kap">
      <div>
        <h2 id="indir-baslik">kroki crm’i indirin.</h2>
        <p>14 gün boyunca Stüdyo paketinin tamamı ücretsiz.</p>
        <div class="kapanis__eylem">
          {magaza('crm', 'kroki crm', ' magaza--acik')}
          <a class="metin-link" data-bag="crmWeb" href="https://studyo-crm.web.app/">Web’den giriş yap</a>
        </div>
      </div>
      {E.telefon(C.panel('k1', LOGO_ACIK))}
    </div>
  </section>'''



SINEMA_JS = r'''
  // giriş sahnesi: kaydırma ilerlemesine göre telefonun yeri, duruşu ve ekranı
  (function () {
    const bolum = document.querySelector('.sinema-c'), sahne = bolum.querySelector('.sinema-c__sahne');
    const eskiz = bolum.querySelector('.giris-c__eskiz'), metin = bolum.querySelector('.giris-c__metin'), yer = bolum.querySelector('.giris-c__yer');
    const cep = bolum.querySelector('.sinema-c__cep'), ekranlar = [...cep.querySelectorAll('.sinema-c__ekran')];
    const yazilar = [...bolum.querySelectorAll('.sinema-c__yazi')];
    const hareket = matchMedia('(prefers-reduced-motion: reduce)');
''' + O.ARA_JS + r'''    const EKRAN_BAS = .24, EKRAN_UZ = .19;                        // telefon yerine oturunca dört ekran sırayla, her biri uzun süre kalır
    let raf = 0, gorunen = -1, sonCizim = '';

    function ciz() {
      raf = 0;
      const W = sahne.clientWidth, H = sahne.clientHeight, dar = W < 900;
      const r = bolum.getBoundingClientRect();
      const hedef = hareket.matches ? 0 : sinir(-r.top / (r.height - H));
      // ilerleme yumuşatılır: tekerlek sıçrasa da telefon ağır ağır yürür
      gorunen = gorunen < 0 || hareket.matches ? hedef : gorunen + (hedef - gorunen) * .14;
      const p = gorunen;
      const sr = sahne.getBoundingClientRect(), yr = yer.getBoundingClientRect();
      const cw = cep.offsetWidth, ch = cep.offsetHeight;
      // değerler değişmediyse (sahne geçildi, telefon yerine oturdu) yeniden yazılmaz; eskiz yüklenip yer değişirse çizilir
      const imza = `${p}|${W}|${H}|${yr.left - sr.left}|${yr.top - sr.top}|${yr.width}|${cw}`;
      if (imza === sonCizim) { if (Math.abs(hedef - gorunen) > .0004) iste(); return; }
      sonCizim = imza;
      // masadaki yerden ekranın sağ yarısının ortasına (telefonda: ortaya, yazıların üstüne)
      const x0 = yr.left - sr.left + yr.width / 2, y0 = yr.top - sr.top + yr.height / 2, o0 = yr.width / cw;
      const x1 = dar ? W / 2 : W * .66, y1 = dar ? H * .42 : H / 2;
      const k = ara(.05, .22, p), egim = Math.sin(k * Math.PI);    // yolun ortasında öne eğilip döner
      // ekran geçişlerinde telefon hafifçe bir sağa bir sola döner
      let don = 0;
      for (let i = 1; i < 4; i++) don += (i % 2 ? 1 : -1) * 16 * Math.exp(-(((p - (EKRAN_BAS + i * EKRAN_UZ)) / .035) ** 2));
      cep.style.transform = `translate(${kar(x0, x1, k) - cw / 2}px,${kar(y0, y1, k) - ch / 2}px) perspective(1500px) ` +
        `rotateX(${egim * 16}deg) rotateY(${-egim * 24 + don}deg) rotateZ(${kar(-8, 0, k)}deg) scale(${kar(o0, 1, k)})`;
      cep.style.visibility = 'visible';
      // yazılar tamamen çekilir, eskiz soluk bir zemin olarak kalır
      const c = ara(.04, .13, p);
      metin.style.opacity = 1 - c; metin.style.visibility = c > .99 ? 'hidden' : '';
      eskiz.style.opacity = 1 - .84 * c;
      ekranlar.forEach((e, i) => { if (i) e.style.opacity = ara(EKRAN_BAS + i * EKRAN_UZ - .035, EKRAN_BAS + i * EKRAN_UZ + .025, p); });
      yazilar.forEach((e, i) => {
        const bas = EKRAN_BAS + i * EKRAN_UZ, son = bas + EKRAN_UZ;
        const g = Math.min(ara(bas - .01, bas + .035, p), i < 3 ? 1 - ara(son - .045, son - .012, p) : 1);
        e.style.opacity = g; e.style.transform = `translateY(${(1 - g) * 18}px)`;
      });
      if (Math.abs(hedef - gorunen) > .0004) iste();
    }
    const iste = () => { if (!raf) raf = requestAnimationFrame(ciz); };
    addEventListener('scroll', iste, { passive: true });
    addEventListener('resize', iste);
    hareket.addEventListener('change', iste);
    addEventListener('load', iste);
    ciz();
  })();
'''

if __name__ == '__main__':
    O.sayfa('kroki-crm.html', 'kroki crm — Kroki', 'İç mimarlık stüdyoları için müşteri, satış hattı, şantiye, takvim ve tahsilat yönetimi.',
            css=CSS.strip() + '\n' + ORTAK_CSS.strip() + '\n' + ANA_CSS.strip(),
            mobil=MOBIL.strip('\n') + '\n' + ORTAK_MOBIL.rstrip() + '\n' + ANA_MOBIL.rstrip(),
            govde=f'<main>\n{GOVDE}\n</main>', js=SINEMA_JS + '\n')
