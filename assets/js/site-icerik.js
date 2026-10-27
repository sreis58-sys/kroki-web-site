/* Sitenin admin panelinden yönetilen içeriğinin başlangıç hâli. Firebase'de içerik yoksa site ve admin paneli bunu kullanır;
   admin panelinde ilk "Kaydet" ile Firebase'e yazılır. Paketler: Desktop/crm app/PRODUCT-DECISIONS.md (22 Ekim 2026). */
window.SITE_VARSAYILAN = {
  paketler: [
    { ad: 'Solo', kim: 'Tek başına çalışanlar için', fiyat: '499', ozellikler: ['1 kullanıcı', 'Müşteriler ve ustalar', 'Şantiye takibi', 'Takvim'], onerilen: false },
    { ad: 'Solo Pro', kim: 'Teklif ve tahsilatı da yönetenler için', fiyat: '749', ozellikler: ['1 kullanıcı', 'Solo’daki her şey', 'Teklif ve sözleşme', 'Tahsilat, makbuz ve muhasebe'], onerilen: false },
    { ad: 'Stüdyo', kim: 'Küçük ekipler için', fiyat: '999', ozellikler: ['4 kullanıcı: siz ve 3 çalışan', 'Solo Pro’daki her şey', 'Ekip erişimi ve yetkiler'], onerilen: true },
    { ad: 'Ofis', kim: 'Büyüyen ofisler için', fiyat: '1.999', ozellikler: ['11 kullanıcı: siz ve 10 çalışan', 'Stüdyo’daki her şey', 'Öncelikli destek', 'Yeni özelliklere ilk erişim'], onerilen: false },
  ],
  // ÖRNEK YORUMLAR: yayına almadan önce admin panelinden gerçek kullanıcı yorumlarıyla değiştir
  yorumlar: [
    { metin: 'Kroki, ofis ile şantiye arasındaki iletişimi ciddi şekilde kolaylaştırdı.', ad: 'M. A.', unvan: 'İç Mimar' },
    { metin: 'Sahada aldığım ölçüler ofise döndüğümde planda hazır bekliyor.', ad: 'S. K.', unvan: 'Mimar' },
    { metin: 'Müşteri, teklif ve ödeme takibi artık tek ekranda; kimse bir şey kaçırmıyor.', ad: 'E. D.', unvan: 'Stüdyo Sahibi' },
  ],
  // boş bırakılan bağlantılar sitede bir yere gitmez; WhatsApp ve e-posta boşsa iletişim bölümünde görünmez
  baglantilar: {
    crmAppStore: '', crmGooglePlay: '', paftaAppStore: '', paftaGooglePlay: '',
    crmWeb: 'https://studyo-crm.web.app/',
    whatsapp: '', eposta: '', instagram: '', linkedin: '', youtube: '',
    // KVKK sayfasındaki veri sorumlusu bilgileri; boşken sayfada köşeli parantezli yer tutucu görünür
    sirketUnvan: '', sirketAdres: '', mersis: '', kep: '',
  },
};

// bağlantı alanları: anahtar, paneldeki adı, türü. Tür, sitede adrese nasıl çevrileceğini ve paneldeki giriş kutusunu belirler:
// magaza: boşken düğmede "Yakında" yazar · url · tel: WhatsApp numarası · eposta · yazi: adres değil, düz yazı (KVKK sayfası)
window.BAGLANTI_ALANLARI = [
  ['crmAppStore', 'kroki crm · App Store adresi', 'magaza'], ['crmGooglePlay', 'kroki crm · Google Play adresi', 'magaza'],
  ['paftaAppStore', 'pafta. · App Store adresi', 'magaza'], ['paftaGooglePlay', 'pafta. · Google Play adresi', 'magaza'],
  ['crmWeb', 'kroki crm · web uygulaması', 'url'],
  ['whatsapp', 'WhatsApp numarası (ör. 0532 000 00 00)', 'tel'], ['eposta', 'E-posta adresi', 'eposta'],
  ['instagram', 'Instagram adresi', 'url'], ['linkedin', 'LinkedIn adresi', 'url'], ['youtube', 'YouTube adresi', 'url'],
  ['sirketUnvan', 'Şirket unvanı (KVKK sayfası)', 'yazi'], ['sirketAdres', 'Şirket adresi', 'yazi'],
  ['mersis', 'MERSİS numarası', 'yazi'], ['kep', 'KEP adresi', 'yazi'],
];

// site ve admin panelinin ortak yardımcıları
window.KROKI = (function () {
  const turler = Object.fromEntries(window.BAGLANTI_ALANLARI.map(([ad, , tur]) => [ad, tur]));
  // Türkiye numarası: baştaki 0 yerine 90; rakam yoksa boş
  const whatsapp = v => { let n = String(v || '').replace(/\D/g, ''); if (n.startsWith('0')) n = '90' + n.slice(1); return n ? `https://wa.me/${n}` : ''; };
  return {
    // deneme kipi (Firebase bağlı değilken): admin paneli ve sitedeki form bu tarayıcıda bu anahtarlarla buluşur
    DEMO: { acik: 'kroki-demo', icerik: 'kroki-demo-icerik', basvurular: 'kroki-demo-basvurular' },
    yerel: {
      oku(a) { try { return JSON.parse(localStorage.getItem(a)); } catch (e) { return null; } },
      yaz(a, v) { try { localStorage.setItem(a, JSON.stringify(v)); return true; } catch (e) { return false; } },
    },
    tur: ad => turler[ad] || 'url',
    whatsapp,
    // bağlantı alanının sitede gideceği adres; boş ya da geçersizse ''
    adres(ad, v) {
      v = String(v || '').trim();
      const tur = turler[ad] || 'url';
      if (!v || tur === 'yazi') return '';
      if (tur === 'tel') return whatsapp(v);
      if (tur === 'eposta') return v.includes('@') ? `mailto:${v}` : '';
      return /^https?:\/\//i.test(v) ? v : `https://${v}`;
    },
  };
})();
