"""pafta.html: uygulama tanıtım sayfası. Menü, alt bilgi ve temel stil ana sayfadan gelir (ortak.py); ekranlar
pafta_ekranlar.py'de uygulamanın ekran görüntülerinden vektör olarak çizilir. Ürün sayfalarının ortak stilleri (telefon,
mağaza, bilgiler, özellikler, adımlar, SSS, ekosistem, kapanış) bu dosyanın CSS/MOBIL bölümlerindedir; crm_sayfasi.py de alır."""
import ortak as O
import pafta_ekranlar as E
from ortak import ANA_CSS, ANA_MOBIL, magaza

CSS = r'''
main{position:relative}
/* uygulamanın kareli zemini: girişte ve kapanışta, kenarlara doğru söner */
.izgara{position:absolute;inset:0;pointer-events:none;background-image:linear-gradient(#dde8f4 1px,transparent 1px),linear-gradient(90deg,#dde8f4 1px,transparent 1px);background-size:26px 26px;-webkit-mask-image:radial-gradient(ellipse 70% 75% at 72% 45%,#000 30%,transparent 75%);mask-image:radial-gradient(ellipse 70% 75% at 72% 45%,#000 30%,transparent 75%)}

/* ---------- giriş: kaydırdıkça büyük telefon döner, karşıya gelir, ekranın içine girilir ---------- */
.sinema{position:relative;height:430vh;margin-top:calc(min(9.8vw,141px) * -1)}
.sinema__sahne{position:sticky;top:0;height:100vh;height:100svh;overflow:hidden;perspective:1500px;background:var(--kagit)}
.sinema__karanlik{position:absolute;inset:0;background:#0B0C0E;opacity:0}
.sinema__metin{position:absolute;inset:0;z-index:2;display:flex;flex-direction:column;justify-content:center;padding-top:min(9.8vw,141px);pointer-events:none}
.sinema__metin > div{max-width:min(40vw,560px);pointer-events:auto}
.urun-logo{height:min(3.9vw,56px);width:auto}
.sinema h1{margin:min(2.6vw,38px) 0 0;font-size:min(4.7vw,68px);font-weight:650;line-height:1.1;letter-spacing:-0.025em}
.giris-p__alt{margin-top:min(1.6vw,22px);max-width:25em;font-size:min(1.3vw,19px);line-height:1.6;color:var(--kursun)}
.giris-p__eylem{display:flex;flex-wrap:wrap;align-items:center;gap:min(1.6vw,22px) min(2.4vw,34px);margin-top:min(2.8vw,40px)}
.giris-p__not{margin-top:min(1.8vw,24px);font-size:min(1vw,14.5px);color:var(--kursun)}
.giris-p__not b{font-weight:600;color:var(--mavi)}
.metin-link{padding-bottom:4px;border-bottom:1.5px solid currentColor;font:500 min(1.1vw,16px)/1 var(--f);transition:color .2s}
.metin-link:hover{color:var(--mavi)}
.sinema__cep{position:absolute;left:50%;top:50%;z-index:1;width:min(23vw,330px);transform:translate(-50%,-50%) translate3d(22vw,4vh,0) rotateX(14deg) rotateY(-32deg) rotateZ(6deg);transform-style:preserve-3d;will-change:transform}
.sinema__ekran{position:absolute;inset:0}
.sinema__ekran + .sinema__ekran{opacity:0}
.sinema__ekran .ekran{display:block;width:100%;height:100%}
.cep__parilti{position:absolute;inset:0;z-index:2;background:linear-gradient(115deg,rgba(255,255,255,.4),rgba(255,255,255,0) 42%);opacity:var(--parilti,.6);pointer-events:none}
.sinema__etiket{position:absolute;left:0;top:0;z-index:3;padding:9px 13px;border-radius:10px;background:#fff;font:500 min(1.05vw,15px)/1.3 var(--f);color:#151515;white-space:nowrap;box-shadow:0 10px 24px -10px rgba(0,0,0,.5);opacity:0;pointer-events:none}
.sinema__etiket b{font-weight:600}
/* son hâlde başlık planın solundaki boş koyu alanda */
.sinema__alt{position:absolute;left:var(--kenar);top:50%;z-index:3;max-width:min(30vw,430px);color:#fff;opacity:0;transform:translateY(-50%);pointer-events:none}
.sinema__alt p{font:600 min(3vw,42px)/1.2 var(--f);letter-spacing:-0.02em}
.sinema__alt span{display:block;margin-top:10px;font:400 min(1.25vw,18px)/1.5 var(--f);color:#a9adb3}
@media (prefers-reduced-motion:reduce){.sinema{height:auto}.sinema__sahne{position:relative}}

/* girişte ölçülen oda eskizi: telefonun arkasında, kaydırınca söner */
.sinema__eskiz{position:absolute;right:0;top:calc(min(9.8vw,141px) + 4px);width:min(76vw,1100px);pointer-events:none}
.sinema__eskiz img{display:block;width:100%;height:auto}
.sinema__eskiz svg{position:absolute;inset:0;width:100%;height:100%}
.sinema__eskiz .duzlem{fill:var(--mavi);mix-blend-mode:multiply;opacity:.85}
.sinema__eskiz .not{left:12%;top:4%}
.ozellik__gorsel .not{left:0;top:4%;font-size:min(1.15vw,16.5px)}
.ozellik--ters .ozellik__gorsel .not{left:auto;right:0}
.yakin-alan .not{top:auto;bottom:calc(100% + 16px)}

/* ---------- telefon çerçevesi ---------- */
.cep{padding:min(.75vw,10px);border-radius:min(3.6vw,52px);background:#121315;box-shadow:0 0 0 1.5px #2b2d31 inset,0 30px 60px -20px rgba(20,24,30,.35),0 12px 24px -12px rgba(20,24,30,.25)}
.cep__ekran{position:relative;overflow:hidden;border-radius:min(2.9vw,42px);aspect-ratio:924/2000;background:#0B0C0E}
.cep__ekran .ekran{display:block;width:100%;height:100%}
.cep__ada{position:absolute;top:2.2%;left:50%;width:31%;height:3.6%;border-radius:99px;background:#000;transform:translateX(-50%)}

/* ---------- mağaza düğmeleri ---------- */
.magaza{display:flex;flex-wrap:wrap;gap:12px}
.magaza a{display:inline-flex;align-items:center;gap:10px;height:min(4vw,58px);min-height:50px;padding:0 20px 0 15px;border-radius:12px;background:#111;color:#fff;transition:background-color .2s}
.magaza a:hover{background:#000}
.magaza svg{width:26px;height:26px;flex:none}
.magaza span{display:flex;flex-direction:column;gap:3px}
.magaza small{font:400 11px/1 var(--f);color:#c9c9c9}
.magaza b{font:600 17px/1 var(--f)}
.magaza--acik a{background:#fff;color:#111}
.magaza--acik a:hover{background:#e9e9e9}
.magaza--acik small{color:#6a6a6a}
.magaza a[data-yakinda]{position:relative;cursor:default;opacity:.6}
.magaza a[data-yakinda]:hover{background:#111}
.magaza--acik a[data-yakinda]:hover{background:#fff}
.magaza a[data-yakinda]::after{content:"Yakında";position:absolute;top:-9px;right:-8px;padding:4px 8px;border-radius:99px;background:var(--mavi);font:600 10.5px/1 var(--f);color:#fff}

/* ---------- kısa bilgiler: mavi kare pafta.'nın noktası ---------- */
.bilgiler{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:min(2.6vw,38px);padding:min(3.4vw,48px) 0;border-top:1px solid #dcd7cc;border-bottom:1px solid #dcd7cc}
.bilgiler h3{display:flex;align-items:center;gap:10px;margin:0;font:600 min(1.15vw,16.5px)/1.3 var(--f)}
.bilgiler h3::before{content:"";flex:none;width:9px;height:9px;background:var(--mavi)}
.bilgiler p{margin-top:8px;padding-left:19px;font-size:min(1vw,14.5px);line-height:1.55;color:var(--kursun)}

/* ---------- özellikler: bir yazı, bir görsel; sıra bir sağa bir sola ---------- */
.bolum{padding-top:min(8vw,116px);padding-bottom:min(8vw,116px)}
.bolum__bas h2{margin:0;max-width:17em;font:600 min(3.05vw,44px)/1.15 var(--f);letter-spacing:-0.02em}
.bolum__bas p{margin-top:16px;max-width:34em;font-size:min(1.25vw,18px);line-height:1.6;color:var(--kursun)}
.ozellik{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);align-items:center;gap:min(6vw,86px);margin-top:min(7vw,100px)}
.ozellik--ters .ozellik__gorsel{order:-1}
.ozellik__ad{margin-bottom:14px;font:500 min(1.05vw,15px)/1 var(--f);color:var(--mavi)}
.ozellik h3{margin:0;font:600 min(2.5vw,36px)/1.15 var(--f);letter-spacing:-0.02em}
.ozellik p{margin-top:16px;max-width:27em;font-size:min(1.25vw,18px);line-height:1.6;color:var(--kursun)}
.ozellik ul{list-style:none;margin:22px 0 0;padding:0;display:grid;gap:10px;font-size:min(1.1vw,16px);color:#2a2a2a}
.ozellik li{display:flex;gap:12px}
.ozellik li::before{content:"";flex:none;width:7px;height:7px;margin-top:.55em;background:var(--mavi)}
.ozellik__gorsel{position:relative;display:flex;justify-content:center}
.ozellik__gorsel .cep{width:min(21vw,300px)}
.ikili{display:flex;gap:min(2vw,28px);align-items:flex-start}
.ikili .cep{width:min(17vw,246px)}
.ikili .cep:last-child{margin-top:min(5vw,72px)}
/* plan yakın çekim: kiriş ve kapı etiketleriyle */
.yakin{position:relative;width:min(36vw,520px);overflow:hidden;border-radius:24px;background:#0B0C0E;box-shadow:0 30px 60px -24px rgba(20,24,30,.4)}
.yakin .ekran{display:block;width:100%;height:auto}
.etiket{position:absolute;white-space:nowrap;padding:8px 12px;border-radius:10px;background:#fff;font:500 min(1vw,14px)/1.3 var(--f);color:#151515;box-shadow:0 8px 20px -8px rgba(0,0,0,.4)}
.etiket b{font-weight:600}
.etiket::before{content:"";position:absolute;width:10px;height:10px;background:#fff;transform:rotate(45deg)}
.etiket--kiris{left:50%;top:44%;white-space:nowrap}
.etiket--kiris::before{left:22px;top:-4px}
.etiket--kapi{left:35%;top:60%}
.etiket--kapi::before{left:-4px;top:12px}

/* ---------- nasıl çalışır: gerçek sıra, uygulamadaki düğmelerle ---------- */
.adimlar{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:min(1.6vw,22px);margin-top:min(4vw,56px);padding:0;list-style:none;counter-reset:adim}
.adim{position:relative;display:flex;flex-direction:column;padding:min(2.4vw,34px);border:1px solid #d9d4c8;border-radius:20px;background:rgba(255,255,255,.45)}
.adim__sira{font:600 min(1vw,14px)/1 var(--f);color:#86837b}
.adim h3{margin:14px 0 0;font:600 min(1.6vw,23px)/1.25 var(--f);letter-spacing:-0.01em}
.adim p{margin-top:10px;font-size:min(1.05vw,15px);line-height:1.55;color:var(--kursun)}
.adim__ui{display:flex;align-items:center;min-height:86px;margin-top:auto;padding-top:26px}
.hap{display:inline-flex;align-items:center;height:48px;padding:0 24px;border-radius:99px;background:var(--mavi);font:700 17px/1 Inter,var(--f);letter-spacing:-.02em;color:#fff}
.mini-arac{display:flex;gap:4px;padding:6px;border-radius:99px;background:#15181B}
.mini-arac span{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;width:58px;height:58px;border-radius:99px;font:500 11px/1 Inter,var(--f);color:#C5C9CE}
.mini-arac span:first-child{background:var(--mavi);color:#fff}
.mini-arac svg{width:20px;height:20px}

/* ---------- sık sorulan sorular ---------- */
.sss__liste{max-width:860px;margin-top:min(3vw,40px);border-top:1px solid #dcd7cc}
.sss details{border-bottom:1px solid #dcd7cc}
.sss summary{display:flex;align-items:center;justify-content:space-between;gap:20px;padding:22px 0;font:600 min(1.4vw,20px)/1.35 var(--f);cursor:pointer;list-style:none}
.sss summary::-webkit-details-marker{display:none}
.sss summary::after{content:"";flex:none;width:12px;height:12px;background:var(--mavi);transition:transform .2s}
.sss details[open] summary::after{transform:rotate(45deg)}
.sss details p{max-width:44em;margin:-6px 0 22px;font-size:min(1.2vw,17px);line-height:1.65;color:var(--kursun)}
@media (prefers-reduced-motion:reduce){.sss summary::after{transition:none}}

/* ---------- ekosistem bandı ---------- */
.ekosistem{display:flex;align-items:center;gap:min(3vw,44px);padding:min(3.4vw,48px) 0;border-top:1px solid #dcd7cc;border-bottom:1px solid #dcd7cc}
.ekosistem img{height:min(2.8vw,40px);width:auto;flex:none}
.ekosistem p{flex:1;font-size:min(1.3vw,19px);line-height:1.5;color:#2a2a2a}
.ekosistem .metin-link{flex:none}

/* ---------- kapanış: uygulamanın koyu teması ---------- */
.kapanis{position:relative;overflow:hidden;margin-top:min(8vw,116px);background:#0B0C0E;color:#fff}
.kapanis .izgara{background-image:linear-gradient(#1a1d22 1px,transparent 1px),linear-gradient(90deg,#1a1d22 1px,transparent 1px);-webkit-mask-image:none;mask-image:none}
.kapanis .kap{position:relative;display:flex;align-items:center;justify-content:space-between;gap:40px;min-height:min(30vw,430px)}
.kapanis h2{margin:0;font:600 min(3.6vw,52px)/1.1 var(--f);letter-spacing:-0.025em}
.kapanis p{margin:14px 0 30px;font-size:min(1.25vw,18px);color:#a9adb3}
.kapanis .metin-link{color:#fff}
.kapanis__eylem{display:flex;flex-wrap:wrap;align-items:center;gap:16px 28px}
.kapanis .cep{align-self:flex-end;width:min(18vw,260px);margin-bottom:max(-24vw,-340px);transform:rotate(6deg)}
'''
MOBIL = r'''
  .sinema{height:380vh;margin-top:-76px}
  .sinema__metin{justify-content:flex-start;padding-top:96px}
  .sinema__metin > div{max-width:none}
  .urun-logo{height:36px}
  .sinema h1{margin-top:16px;font-size:clamp(2rem,8.6vw,3.2rem)}
  .giris-p__alt{font-size:1rem}
  .giris-p__eylem{gap:14px 22px;margin-top:22px}
  .giris-p__not{font-size:13.5px}
  .metin-link{font-size:1rem}
  .sinema__cep{width:min(46vw,220px)}
  .sinema__etiket{font-size:12.5px;padding:7px 10px}
  .sinema__alt{left:0;right:0;top:auto;bottom:0;max-width:none;padding:72px 20px 30px;text-align:center;background:linear-gradient(rgba(11,12,14,0),#0B0C0E 45%);transform:none}
  .sinema__alt p{font-size:1.5rem}
  .sinema__eskiz{top:auto;bottom:6%;width:150%;right:-30%}
  .sinema__eskiz .not{display:none}
  .ozellik__gorsel .not{position:relative;left:auto;right:auto;top:auto;bottom:auto;align-self:flex-start;margin:0 0 16px;font-size:12px}
  .ozellik__gorsel{flex-direction:column;align-items:center}
  .sinema__alt span{font-size:.95rem}
  .izgara{-webkit-mask-image:radial-gradient(ellipse 90% 60% at 50% 75%,#000 30%,transparent 75%);mask-image:radial-gradient(ellipse 90% 60% at 50% 75%,#000 30%,transparent 75%)}
  .cep{padding:7px;border-radius:34px}
  .cep__ekran{border-radius:28px}
  .magaza a{height:52px}
  .bilgiler{grid-template-columns:1fr 1fr;gap:24px 20px;padding:32px 0}
  .bilgiler h3{font-size:15px}
  .bilgiler p{font-size:14px}
  .bolum{padding-top:64px;padding-bottom:64px}
  .bolum__bas h2{font-size:1.9rem}
  .bolum__bas p{font-size:1rem}
  .ozellik{grid-template-columns:1fr;gap:32px;margin-top:64px}
  .ozellik--ters .ozellik__gorsel{order:0}
  .ozellik__ad{font-size:14px}
  .ozellik h3{font-size:1.6rem}
  .ozellik p,.ozellik ul{font-size:1rem}
  .ozellik__gorsel .cep{width:min(62vw,280px)}
  .ikili .cep{width:min(42vw,200px)}
  .yakin{width:100%}
  .etiket{font-size:12.5px;padding:6px 10px}
  .adimlar{grid-template-columns:1fr;margin-top:32px}
  .adim{padding:26px}
  .adim__sira{font-size:13px}
  .adim h3{font-size:1.25rem}
  .adim p{font-size:1rem}
  .sss summary{font-size:1.05rem;padding:18px 0}
  .sss details p{font-size:1rem}
  .ekosistem{flex-direction:column;align-items:flex-start;gap:16px;padding:36px 0}
  .ekosistem img{height:32px}
  .ekosistem p{font-size:1.05rem}
  .kapanis{margin-top:64px}
  .kapanis .kap{flex-direction:column;align-items:flex-start;padding-top:56px;min-height:0}
  .kapanis h2{font-size:2rem}
  .kapanis p{font-size:1rem}
  .kapanis .cep{align-self:center;width:62vw;margin-bottom:-60vw}
'''

MINI = lambda ad: f'<svg viewBox="-26 -26 52 52">{E.ikon(ad)}</svg>'
GOVDE = f'''  <section class="sinema" aria-label="pafta. tanıtımı">
    <div class="sinema__sahne">
      <div class="izgara" aria-hidden="true"></div>
      <div class="sinema__eskiz" aria-hidden="true">
        <img src="assets/gorseller/pafta-eskiz.webp" width="1536" height="1024" alt="">
        <!-- mavi düzlem görselin piksel koordinatlarında: sağdaki kapı açıklığı (logodaki kapı) -->
        <svg viewBox="0 0 1536 1024"><polygon class="duzlem" points="1392,332 1478,318 1478,718 1392,693"/></svg>
        <p class="not"><span>Duvar duvar,</span><span>kiriş</span><span>kiriş.</span></p>
      </div>
      <div class="sinema__karanlik" aria-hidden="true"></div>
      <div class="kap sinema__metin">
        <div>
          <img class="urun-logo" src="assets/logolar/pafta-logo.svg" alt="pafta." width="640" height="206">
          <h1>Ölçü sahada, plan elinde.</h1>
          <p class="giris-p__alt">Duvarı çizin, ölçüler kendiliğinden yazılsın. Kirişler, kapılar, pencereler ve toplam alan; hepsi müşterinin dosyasında, bulutta.</p>
          <div class="giris-p__eylem">
            {magaza()}
            <a class="metin-link" href="#nasil">Nasıl çalışır</a>
          </div>
          <p class="giris-p__not"><b>Ücretsiz.</b> İndirin, hemen ölçmeye başlayın.</p>
        </div>
      </div>
      <div class="sinema__cep">
        <div class="cep"><div class="cep__ekran">
          <div class="sinema__ekran">{E.ana_ekran('s1')}</div>
          <div class="sinema__ekran">{E.musteri_ekrani('s2')}</div>
          <div class="sinema__ekran">{E.plan_ekrani('s3')}</div>
          <span class="cep__ada" aria-hidden="true"></span><span class="cep__parilti" aria-hidden="true"></span>
        </div></div>
      </div>
      <!-- etiketler planın noktalarına iliştirilir (ekran görüntüsünün 924×2000 koordinatları) -->
      <span class="sinema__etiket" data-x="470" data-y="706" data-yon="alt" aria-hidden="true"><b>Kiriş</b> 6,27 m, h 80 cm</span>
      <span class="sinema__etiket" data-x="225" data-y="872" data-yon="alt" aria-hidden="true"><b>Kapı</b> 90/210</span>
      <span class="sinema__etiket" data-x="420" data-y="1200" data-yon="alt" aria-hidden="true"><b>Ölçüler</b> kendiliğinden</span>
      <div class="sinema__alt"><p>Duvarı çizin, ölçü yazılsın.</p><span>Toplamlar ve alan siz çizdikçe hazır.</span></div>
    </div>
  </section>

  <section class="kap" aria-label="Kısaca pafta.">
    <div class="bilgiler">
      <div><h3>Ölçekli ızgara</h3><p>Bir kare 50 cm. Çizdiğiniz her duvar ölçekte.</p></div>
      <div><h3>Ölçüler kendiliğinden</h3><p>Duvar boyları, ara ölçüler, toplamlar ve alan.</p></div>
      <div><h3>Buluta kayıt</h3><p>Planlar müşterinin dosyasında saklanır.</p></div>
      <div><h3>Açık ve koyu tema</h3><p>Sahada güneşte de, akşam ofiste de rahat okunur.</p></div>
    </div>
  </section>

  <section class="kap bolum" aria-labelledby="ozellik-baslik">
    <div class="bolum__bas">
      <h2 id="ozellik-baslik">Röleve için gereken her şey, tek ekranda.</h2>
      <p>Metre, kâğıt ve kalemle sahada yaptığınız işi telefonda yapın; ofise döndüğünüzde plan hazır olsun.</p>
    </div>

    <div class="ozellik">
      <div>
        <p class="ozellik__ad">Duvar</p>
        <h3>Duvarı çizin, ölçü yazılsın.</h3>
        <p>Duvar aracıyla çizdiğiniz her duvarın uzunluğu plana kendiliğinden yazılır. Ara ölçüler zincir hâlinde dizilir, toplamlar ve toplam alan köşede hazır bekler.</p>
        <ul><li>Bir kare 50 cm olan ölçekli ızgara</li><li>Ara ölçüler, toplam ölçüler ve m²</li><li>Geri al, Sığdır ve İncele ile rahat düzenleme</li></ul>
      </div>
      <div class="ozellik__gorsel"><p class="not" aria-hidden="true"><span>Ölçü</span><span>kendiliğinden</span><span>yazılır.</span></p>{E.telefon(E.plan_ekrani('o1'))}</div>
    </div>

    <div class="ozellik ozellik--ters">
      <div>
        <p class="ozellik__ad">Kiriş, kapı, pencere</p>
        <h3>Kirişi de ölçün, kapıyı da.</h3>
        <p>Kiriş aracıyla kirişin yerini ve yüksekliğini işaretleyin. Kapı ve pencereleri Ekle ile duvara yerleştirin; ölçüleri planın üstünde görünür.</p>
        <ul><li>Kiriş boyu ve yüksekliği</li><li>Kapı ölçüsü, örneğin 90/210</li><li>Pencere ve kolon</li></ul>
      </div>
      <div class="ozellik__gorsel yakin-alan">
        <p class="not" aria-hidden="true"><span>Kirişi</span><span>unutma.</span></p>
        <div class="yakin">
          {E.plan_ekrani('o2', viewbox='60 500 820 640')}
          <span class="etiket etiket--kiris" aria-hidden="true"><b>Kiriş</b> 6,27 m, h 80 cm</span>
          <span class="etiket etiket--kapi" aria-hidden="true"><b>Kapı</b> 90/210</span>
        </div>
      </div>
    </div>

    <div class="ozellik">
      <div>
        <p class="ozellik__ad">Müşteriler</p>
        <h3>Her müşterinin planları kendi dosyasında.</h3>
        <p>Müşteri ekleyin, altına odaların planlarını açın. Son değişen en üstte durur, her şey buluta kaydedilir.</p>
        <ul><li>Müşteri ve plan sayısı bir bakışta</li><li>Buluta otomatik kayıt</li><li>Açık ve koyu tema</li></ul>
      </div>
      <div class="ozellik__gorsel ikili"><p class="not" aria-hidden="true"><span>Her oda</span><span>kendi</span><span>planında.</span></p>{E.telefon(E.ana_ekran('o3'))}{E.telefon(E.musteri_ekrani('o4'))}</div>
    </div>
  </section>

  <section class="bant" aria-label="pafta.'nın yaklaşımı">
    <div class="bant__ic">
      <p class="bant__metin">Ölçü<br>bir kez<br>alınır.</p>
      <div class="bant__eskiz" aria-hidden="true">
        <img src="assets/gorseller/pafta-bant.webp" alt="" width="1536" height="400" loading="lazy">
        <svg viewBox="0 0 1536 400"><polygon class="mavi" points="832,170 918,170 918,318 832,318"/></svg>
      </div>
    </div>
  </section>

  <section class="kap bolum" id="nasil" aria-labelledby="nasil-baslik">
    <div class="bolum__bas">
      <h2 id="nasil-baslik">Üç adımda röleve.</h2>
      <p>Sahaya vardığınızda uygulamayı açın; gerisi duvar duvar ilerler.</p>
    </div>
    <ol class="adimlar">
      <li class="adim">
        <span class="adim__sira">1. adım</span>
        <h3>Müşteriyi ekleyin.</h3>
        <p>Ana ekrandan yeni müşteri açın. Bütün planları onun dosyasında toplanır.</p>
        <div class="adim__ui" aria-hidden="true"><span class="hap">+ Yeni Müşteri</span></div>
      </li>
      <li class="adim">
        <span class="adim__sira">2. adım</span>
        <h3>Odanın planını açın.</h3>
        <p>Salon, mutfak, banyo; her oda için ayrı bir plan.</p>
        <div class="adim__ui" aria-hidden="true"><span class="hap">+ Yeni Plan</span></div>
      </li>
      <li class="adim">
        <span class="adim__sira">3. adım</span>
        <h3>Duvarları ve kirişleri çizin.</h3>
        <p>Ölçüler, toplamlar ve alan siz çizdikçe plana yazılır.</p>
        <div class="adim__ui" aria-hidden="true"><span class="mini-arac"><span>{MINI('duvar')}Duvar</span><span>{MINI('kiris')}Kiriş</span><span>{MINI('ekle')}Ekle</span></span></div>
      </li>
    </ol>
  </section>

  <section class="kap bolum sss" id="sss" aria-labelledby="sss-baslik">
    <div class="bolum__bas"><h2 id="sss-baslik">Sık sorulan sorular</h2></div>
    <div class="sss__liste">
      <details><summary>Ölçüler nerede saklanır?</summary><p>Her plan, müşterinin dosyasında durur ve buluta kaydedilir. Telefon değişse de planlar kaybolmaz.</p></details>
      <details><summary>Çizim ölçekli mi?</summary><p>Evet. Bir kare 50 cm olan ızgara üzerinde çizersiniz; duvar boyları, ara ölçüler, toplamlar ve alan bu ölçeğe göre yazılır.</p></details>
      <details><summary>pafta. ücretli mi?</summary><p>Hayır, pafta. ücretsiz.</p></details>
      <details><summary>Kiriş, kapı ve pencere de ölçülüyor mu?</summary><p>Kiriş aracıyla kirişin yerini ve yüksekliğini, Ekle ile kapı ve pencereleri ölçüleriyle birlikte plana koyarsınız.</p></details>
    </div>
  </section>

  <section class="kap">
    <div class="ekosistem">
      <img src="assets/logolar/kroki-crm.png" alt="kroki crm" width="900" height="278" loading="lazy">
      <p>Ölçüden sonrası için kroki crm. Müşteriyi, şantiyeyi ve tahsilatı aynı ekosistemde yönetin.</p>
      <a class="metin-link" href="kroki-crm.html">kroki crm’i tanıyın</a>
    </div>
  </section>

  <section class="kapanis" id="indir" aria-labelledby="indir-baslik">
    <div class="izgara" aria-hidden="true"></div>
    <div class="kap">
      <div>
        <h2 id="indir-baslik">pafta. ücretsiz.</h2>
        <p>İndirin, hemen kullanmaya başlayın. Mağazalara çıktığında haber vermemizi isterseniz bize yazın.</p>
        <div class="kapanis__eylem">
          {magaza(ek=' magaza--acik')}
          <a class="metin-link" href="index.html?urun=pafta.#iletisim">Çıkınca haber ver</a>
        </div>
      </div>
      {E.telefon(E.plan_ekrani('k1'))}
    </div>
  </section>'''



SINEMA_JS = r'''
  // giriş: kaydırma ilerlemesine göre telefonun duruşu, ekranı ve planın çizimi
  (function () {
    const bolum = document.querySelector('.sinema'), sahne = bolum.querySelector('.sinema__sahne');
    const cep = bolum.querySelector('.sinema__cep'), metin = bolum.querySelector('.sinema__metin');
    const eskiz = bolum.querySelector('.sinema__eskiz'), karanlik = bolum.querySelector('.sinema__karanlik'), alt = bolum.querySelector('.sinema__alt');
    const ekranlar = [...bolum.querySelectorAll('.sinema__ekran')], plan = ekranlar[2].querySelector('svg');
    const duvarlar = [...plan.querySelectorAll('.ciz-duvar path')];
    // ölçü grupları çiziliş sırasıyla belirir (data-sira: 1,5–3,3)
    const olculer = [...plan.querySelectorAll('.ciz-olcu')].map(g => ({ g, sira: (parseFloat(g.dataset.sira) - 1.5) / 1.8 }));
    const etiketler = [...bolum.querySelectorAll('.sinema__etiket')];
    const hareket = matchMedia('(prefers-reduced-motion: reduce)');
    duvarlar.forEach(y => { y.style.strokeDasharray = 1; });
''' + O.ARA_JS + r'''    let bekliyor = false, sonCizim = '';

    function ciz() {
      bekliyor = false;
      const W = innerWidth, H = sahne.clientHeight, dar = W < 900;
      const r = bolum.getBoundingClientRect();
      const p = hareket.matches ? 0 : sinir(-r.top / (r.height - H));
      // sahne geçildikten sonra (p sabit) her kaydırmada aynı değerler yeniden yazılmaz
      const imza = `${p}|${W}|${H}`;
      if (imza === sonCizim) return;
      sonCizim = imza;
      const don = ara(.08, .4, p), yak = ara(.47, .76, p);
      // ekranın içine girerken plan kutusu (924×2000 ekranında 820×940) görünüme sığar
      const ew = cep.offsetWidth * .93, eh = ew * 2000 / 924;
      const S = Math.min(W * .92 / (ew * 820 / 924), H * .64 / (eh * 940 / 2000));
      const x0 = dar ? 0 : W * .22, y0 = dar ? H * .3 : H * .04;
      const olcek = kar(kar(1, 1.1, don), S, yak);
      cep.style.transform = `translate(-50%,-50%) translate3d(${kar(x0, 0, don) + (dar ? 0 : W * .14) * yak}px,${kar(y0, 0, don) - (dar ? H * .07 : 0) * yak}px,0) ` +
        `rotateX(${kar(14, 0, don)}deg) rotateY(${kar(-32, 0, don)}deg) rotateZ(${kar(6, 0, don)}deg) scale(${olcek})`;
      cep.style.setProperty('--parilti', ((1 - don) * .6).toFixed(3));
      const m = 1 - ara(.06, .2, p);
      eskiz.style.opacity = .15 + .85 * m;
      metin.style.opacity = m; metin.style.transform = `translateY(${(1 - m) * -40}px)`; metin.style.visibility = m ? '' : 'hidden';
      ekranlar[1].style.opacity = ara(.25, .31, p);
      ekranlar[2].style.opacity = ara(.38, .44, p);
      karanlik.style.opacity = ara(.6, .74, p);
      const u = ara(.5, .7, p);
      duvarlar.forEach(y => { y.style.strokeDashoffset = 1 - u; });
      olculer.forEach(o => { o.g.style.opacity = sinir((p - (.62 + o.sira * .2)) / .03); });
      const e = ara(.84, .9, p), k = plan.getBoundingClientRect();
      etiketler.forEach((el, i) => {
        const g = ara(.84 + i * .025, .9 + i * .025, p);
        el.style.opacity = g;
        el.style.transform = `translate(${k.left + el.dataset.x / 924 * k.width}px,${k.top + el.dataset.y / 2000 * k.height}px) translate(-50%,${el.dataset.yon === 'alt' ? '30%' : '-130%'}) translateY(${(1 - g) * 10}px)`;
      });
      alt.style.opacity = ara(.88, .95, p);
    }
    const iste = () => { if (!bekliyor) { bekliyor = true; requestAnimationFrame(ciz); } };
    addEventListener('scroll', iste, { passive: true });
    addEventListener('resize', iste);
    hareket.addEventListener('change', iste);
    ciz();
  })();
'''

if __name__ == '__main__':
    ACIKLAMA = 'Röleveyi telefonda çizin: duvarlar, kirişler, kapılar, pencereler ve ölçüler plana kendiliğinden yazılsın. Ücretsiz röleve ve ölçü uygulaması.'
    O.sayfa('pafta.html', 'pafta. — Ücretsiz röleve ve ölçü alma uygulaması', ACIKLAMA,
            css=CSS.strip() + '\n' + ANA_CSS.strip(), mobil=MOBIL.strip('\n') + '\n' + ANA_MOBIL.rstrip(),
            govde=f'<main>\n{GOVDE}\n</main>', js=SINEMA_JS + '\n', ikon='assets/logolar/pafta-ikon.svg',
            css_notu=O.ORTAK_NOT + ' Uygulama ekranları Inter ile yazılır.',
            veriler=[O.uygulama('pafta.', ACIKLAMA, 'pafta.html', 'iOS, Android', {'@type': 'Offer', 'price': 0, 'priceCurrency': 'TRY'}), O.sss(GOVDE)])
