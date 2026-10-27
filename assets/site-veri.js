/* Admin panelinden yönetilen içeriği siteye uygular ve iletişim formunu gönderir.
   Firebase ayarı varsa içerik Firestore'dan okunur (küçük kalsın diye SDK yerine REST ile); yoksa admin panelinin
   deneme modunda bu tarayıcıya kaydettiği içerik kullanılır. İkisi de yoksa sayfadaki gömülü içerik olduğu gibi kalır. */
(function () {
  const ayar = window.FIREBASE_AYAR;
  const { DEMO, yerel, adres, tur } = window.KROKI;
  const kok = ayar && `https://firestore.googleapis.com/v1/projects/${ayar.projectId}/databases/(default)/documents`;

  // Firestore REST değerleri → düz JavaScript
  const deger = v => 'stringValue' in v ? v.stringValue : 'booleanValue' in v ? v.booleanValue
    : 'integerValue' in v ? Number(v.integerValue) : 'doubleValue' in v ? v.doubleValue
    : 'arrayValue' in v ? (v.arrayValue.values || []).map(deger) : 'mapValue' in v ? alanlar(v.mapValue.fields || {}) : null;
  const alanlar = f => Object.fromEntries(Object.entries(f).map(([k, v]) => [k, deger(v)]));

  async function icerikGetir() {
    if (!ayar) return yerel.oku(DEMO.icerik);
    const yanit = await fetch(`${kok}/site/icerik?key=${ayar.apiKey}`);
    if (!yanit.ok) return null;                                    // içerik henüz kaydedilmemiş: gömülü hâl kalır
    return alanlar((await yanit.json()).fields || {});
  }

  /* ---------- uygulama ---------- */
  const el = (ad, sinif, metin) => { const e = document.createElement(ad); if (sinif) e.className = sinif; if (metin != null) e.textContent = metin; return e; };

  function paketleriYaz(paketler) {
    document.querySelectorAll('[data-paketler]').forEach(izgara => {
      const hedef = izgara.dataset.hedef || '#';
      izgara.replaceChildren(...paketler.map(p => {
        const kart = el('article', 'paket');
        if (p.onerilen) { kart.setAttribute('data-onerilen', ''); kart.append(el('span', 'paket__etiket', 'Önerilen')); }
        kart.append(el('h3', null, p.ad), el('p', 'paket__kim', p.kim));
        const fiyat = el('p', 'paket__fiyat');
        if (/^\d[\d.,]*$/.test(String(p.fiyat).trim())) fiyat.append(`${String(p.fiyat).trim()} TL `, el('small', null, '/ ay'));
        else fiyat.textContent = p.fiyat;                          // ör. "Görüşelim"
        const liste = el('ul');
        (p.ozellikler || []).filter(Boolean).forEach(o => liste.append(el('li', null, o)));
        const dugme = el('a', 'paket__btn', 'Ücretsiz dene'); dugme.href = hedef;
        kart.append(fiyat, liste, dugme);
        return kart;
      }));
    });
  }

  // boş bağlantı bir yere gitmez; mağaza adresi henüz girilmemiş düğme "Yakında" olur
  function baglantilariYaz(b) {
    document.querySelectorAll('[data-bag]').forEach(a => {
      const href = adres(a.dataset.bag, b[a.dataset.bag]);
      a.href = href || '#';
      if (a.hasAttribute('data-bos-gizle')) a.hidden = !href;
      if (tur(a.dataset.bag) === 'magaza') {
        a.toggleAttribute('data-yakinda', !href);
        if (href) a.removeAttribute('aria-disabled'); else a.setAttribute('aria-disabled', 'true');
      }
      if (href && /^https?:/.test(href)) { a.target = '_blank'; a.rel = 'noopener'; } else { a.removeAttribute('target'); }
    });
    // boş bilgi yerine sayfadaki yer tutucu kalır (ör. KVKK sayfasında şirket unvanı)
    document.querySelectorAll('[data-bag-metin]').forEach(s => {
      if (!('yerTutucu' in s.dataset)) s.dataset.yerTutucu = s.textContent;
      s.textContent = String(b[s.dataset.bagMetin] || '').trim() || s.dataset.yerTutucu;
    });
  }
  addEventListener('click', e => { const a = e.target.closest('a[data-yakinda]'); if (a) e.preventDefault(); });

  function uygula(icerik) {
    if (!icerik) return;
    // paketler sayfaya gömülü başlangıç hâliyle aynıysa dokunulmaz (ana sayfada noktaların yeniden kurulmasına gerek kalmaz)
    const yeniPaket = Array.isArray(icerik.paketler) && icerik.paketler.length && JSON.stringify(icerik.paketler) !== JSON.stringify(window.SITE_VARSAYILAN.paketler);
    if (yeniPaket) paketleriYaz(icerik.paketler);
    if (Array.isArray(icerik.yorumlar) && window.yorumlariYukle) window.yorumlariYukle(icerik.yorumlar);
    baglantilariYaz({ ...window.SITE_VARSAYILAN.baglantilar, ...(icerik.baglantilar || {}) });
    if (yeniPaket) dispatchEvent(new Event('site-verisi'));        // ana sayfa: paket çerçevelerini çizen noktalar yeniden ölçer
  }
  // gömülü içerik bile olsa bağlantılar varsayılanla doldurulur (WhatsApp/e-posta boşsa gizlenir)
  baglantilariYaz(window.SITE_VARSAYILAN.baglantilar);
  icerikGetir().then(uygula).catch(() => {});

  /* ---------- iletişim formu ---------- */
  const rastgele = () => Array.from(crypto.getRandomValues(new Uint8Array(15)), b => 'abcdefghijklmnopqrstuvwxyz0123456789'[b % 36]).join('');
  async function gonder(b) {
    if (ayar) {
      const ad = `projects/${ayar.projectId}/databases/(default)/documents/basvurular/${rastgele()}`;
      const s = v => ({ stringValue: v });
      const yanit = await fetch(`${kok}:commit?key=${ayar.apiKey}`, {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ writes: [{
          update: { name: ad, fields: { ad: s(b.ad), iletisim: s(b.iletisim), studyo: s(b.studyo), urun: s(b.urun), mesaj: s(b.mesaj), kvkk: { booleanValue: true }, durum: s('yeni') } },
          updateTransforms: [{ fieldPath: 'tarih', setToServerValue: 'REQUEST_TIME' }],
          currentDocument: { exists: false },
        }] }),
      });
      if (!yanit.ok) throw new Error('gönderilemedi');
      return;
    }
    // Firebase bağlı değil: yalnızca admin panelinin deneme modu açıksa bu tarayıcıya kaydedilir
    if (!yerel.oku(DEMO.acik)) throw new Error('form bağlı değil');
    const liste = yerel.oku(DEMO.basvurular) || [];
    liste.unshift({ id: rastgele(), ...b, kvkk: true, durum: 'yeni', tarih: Date.now() });
    if (!yerel.yaz(DEMO.basvurular, liste)) throw new Error('kaydedilemedi');
  }

  document.querySelectorAll('form[data-basvuru]').forEach(form => {
    // ürün sayfalarından gelen bağlantı ürünü seçili getirir: kroki-web.html?urun=pafta.#iletisim
    const urun = new URLSearchParams(location.search).get('urun');
    if (urun && [...form.urun.options].some(o => o.value === urun)) form.urun.value = urun;
    const durum = form.querySelector('.form__durum'), dugme = form.querySelector('button[type=submit]');
    const yaz = (metin, tur) => { durum.textContent = metin; durum.dataset.tur = tur; };
    form.addEventListener('submit', async e => {
      e.preventDefault();
      if (!form.reportValidity()) return;
      const v = Object.fromEntries(new FormData(form));
      if (v.web) return;                                           // gizli alan doluysa bot: sessizce geç
      const b = { ad: v.ad.trim(), iletisim: v.iletisim.trim(), studyo: (v.studyo || '').trim(), urun: v.urun, mesaj: (v.mesaj || '').trim() };
      dugme.disabled = true; yaz('Gönderiliyor…', 'bekle');
      try {
        await gonder(b);
        form.reset();
        yaz('Teşekkürler, mesajınız bize ulaştı. En kısa sürede dönüş yapacağız.', 'tamam');
      } catch (err) {
        yaz('Mesaj şu an gönderilemedi. Lütfen biraz sonra tekrar deneyin ya da WhatsApp ve e-postadan yazın.', 'hata');
      } finally { dugme.disabled = false; }
    });
  });
})();
