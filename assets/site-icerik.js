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

// bağlantı alanlarının panelde görünen adları ve sırası
window.BAGLANTI_ALANLARI = [
  ['crmAppStore', 'kroki crm · App Store adresi'], ['crmGooglePlay', 'kroki crm · Google Play adresi'],
  ['paftaAppStore', 'pafta. · App Store adresi'], ['paftaGooglePlay', 'pafta. · Google Play adresi'],
  ['crmWeb', 'kroki crm · web uygulaması'],
  ['whatsapp', 'WhatsApp numarası (ör. 0532 000 00 00)'], ['eposta', 'E-posta adresi'],
  ['instagram', 'Instagram adresi'], ['linkedin', 'LinkedIn adresi'], ['youtube', 'YouTube adresi'],
  ['sirketUnvan', 'Şirket unvanı (KVKK sayfası)'], ['sirketAdres', 'Şirket adresi'], ['mersis', 'MERSİS numarası'], ['kep', 'KEP adresi'],
];
// adres değil düz yazı olan alanlar
window.YAZI_ALANLARI = ['sirketUnvan', 'sirketAdres', 'mersis', 'kep'];
