"""kroki crm uygulamasının telefon ekranları: kullanıcının ekran görüntülerinden (referans/kroki-crm/ekranlar) vektör olarak
yeniden çizildi. Koordinatlar ekran görüntüsünün 739×1600 hâlindeki pikselleridir; oran pafta ekranlarıyla aynı (924/2000),
bu yüzden aynı telefon çerçevesine girer. Gerçek müşteri adları ve tutarlar örnekle değiştirildi."""

YAZI = "font-family=\"Inter, 'SF Pro Display', -apple-system, 'Segoe UI', sans-serif\""
ZEMIN, KART, CIZGI, SOLUK, MAVI_YAZI = '#0B0C0D', '#141617', '#25292C', '#A0A6AB', '#7BA4F7'

def _durum():
    return '''<rect width="739" height="89" fill="#0B0C0D"/>
  <text x="120" y="58" text-anchor="middle" font-size="28" font-weight="600" fill="#fff">9:41</text>
  <g fill="#fff"><rect x="541" y="48" width="6" height="11" rx="1.5"/><rect x="551" y="43" width="6" height="16" rx="1.5"/><rect x="561" y="38" width="6" height="21" rx="1.5"/><rect x="571" y="33" width="6" height="26" rx="1.5"/></g>
  <path d="M592 43a21 21 0 0 1 29 0M598 50a12 12 0 0 1 17 0" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/><circle cx="606.5" cy="57" r="3.2" fill="#fff"/>
  <rect x="637" y="36" width="46" height="25" rx="7" fill="none" stroke="#fff" stroke-width="2.5" opacity=".5"/><rect x="640.5" y="39.5" width="33" height="18" rx="4.5" fill="#fff"/>'''

def _ust(logo):
    return f'''<image href="{logo}" x="30" y="114" width="173" height="56"/>
  <circle cx="356" cy="142" r="33" fill="#111314" stroke="#2E3235" stroke-width="2"/>
  <g transform="translate(356 142)" fill="none" stroke="#E8E8E6" stroke-width="2.6" stroke-linecap="round"><circle r="7"/><path d="M0-15v-4M0 15v4M-15 0h-4M15 0h4M-10.6-10.6l-2.8-2.8M10.6 10.6l2.8 2.8M-10.6 10.6l-2.8 2.8M10.6-10.6l2.8-2.8"/></g>
  <rect x="410" y="110" width="179" height="65" rx="32.5" fill="#111314" stroke="#2E3235" stroke-width="2"/>
  <g transform="translate(451 142)" fill="none" stroke="#E8E8E6" stroke-width="2.6"><circle r="6"/><circle r="12.5" stroke-dasharray="5 3.2"/></g>
  <text x="475" y="151" font-size="24" fill="#F2F2F0">Ayarlar</text>
  <text x="617" y="150" font-size="20" fill="#8B9196" text-decoration="underline">çıkış yap</text>
  <path d="M0 196H739" stroke="#1F2225" stroke-width="2"/>'''

def _ikon(ad, renk):
    s = f'fill="none" stroke="{renk}" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"'
    return {
        'panel': f'<path {s} d="M-12-12h10v10h-10zM2-12h10v10H2zM-12 2h10v10h-10z"/>',
        'musteri': f'<circle {s} cx="0" cy="-6" r="6"/><path {s} d="M-12 13a12 12 0 0 1 24 0"/>',
        'santiye': f'<path {s} d="M-11 13V-2l8-6v21M-3 13V-12l14 6v19M-14 13h28"/>',
        'takvim': f'<rect {s} x="-12" y="-10" width="24" height="22" rx="3"/><path {s} d="M-12-3h24M-6-14v6M6-14v6"/>',
        'muhasebe': f'<rect {s} x="-13" y="-10" width="26" height="20" rx="4"/><path {s} d="M-13-3h26M5 4h4"/>',
    }[ad]

def _alt_menu(etkin):
    ogeler = [('panel', 'Panel', 108), ('musteri', 'Müşteriler', 238), ('santiye', 'Şantiyeler', 368), ('takvim', 'Takvim', 499), ('muhasebe', 'Muhasebe', 629)]
    g = ''
    for ad, yazi, x in ogeler:
        e = ad == etkin
        g += f'''<g transform="translate({x} 1443)">{_ikon(ad, '#4C8DF6' if e else '#7E848A')}</g>
  <text x="{x}" y="1482" text-anchor="middle" font-size="20" font-weight="{'700' if e else '400'}" fill="{'#F2F2F0' if e else '#8B9196'}">{yazi}</text>'''
    return f'''<rect x="31" y="1413" width="676" height="90" rx="45" fill="#141617" stroke="#2A2E31" stroke-width="2"/>
  {g}'''

def _cerceve(icerik, etiket, logo, menu):
    return f'''<svg class="ekran" viewBox="0 0 739 1600" {YAZI} role="img" aria-label="{etiket}">
  <rect width="739" height="1600" fill="{ZEMIN}"/>
  {_durum()}
  {_ust(logo)}
  {icerik}
  {_alt_menu(menu)}
</svg>'''

def _isik(kimlik, renk, cx, cy, rx, ry):
    return f'<defs><radialGradient id="{kimlik}" cx="{cx}" cy="{cy}" r="1" gradientTransform="translate({cx} {cy}) scale({rx} {ry}) translate({-cx} {-cy})" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="{renk}" stop-opacity=".55"/><stop offset="1" stop-color="{renk}" stop-opacity="0"/></radialGradient></defs>'

def panel(kimlik, logo):
    """Panel: günün özeti, sıradaki iş"""
    return _cerceve(f'''{_isik(kimlik + '-isik', '#1D4F86', 369, 1106, 330, 110)}
  <text x="30" y="292" font-size="62" font-weight="800" letter-spacing="-3" fill="#F7F6F2">İşlerin yolunda.</text>
  <text x="30" y="352" font-size="26" fill="{SOLUK}">21 Ekim Çarşamba</text>
  <text x="30" y="405" font-size="21" fill="{SOLUK}">3 iş seni bekliyor. Önce sıradakiyle başlayalım.</text>
  <rect x="31" y="460" width="199" height="72" rx="36" fill="#111314" stroke="#3A3E41" stroke-width="2"/>
  <text x="130.5" y="504" text-anchor="middle" font-size="20" font-weight="700" fill="#F2F2F0">+ Yeni Müşteri</text>
  <rect x="246" y="460" width="208" height="72" rx="36" fill="#F2F2F0"/>
  <text x="350" y="504" text-anchor="middle" font-size="20" font-weight="700" fill="#111">+ Randevu Ekle</text>
  <text x="30" y="614" font-size="27" font-weight="700" fill="#F2F2F0">Sıradaki işin</text>
  <rect x="585" y="581" width="123" height="48" rx="24" fill="#101615" stroke="#24302A" stroke-width="2"/>
  <circle cx="613" cy="605" r="6" fill="#37C770"/><text x="631" y="612" font-size="19" fill="{MAVI_YAZI}">Bugün</text>
  <rect x="31" y="662" width="677" height="444" rx="40" fill="{KART}" stroke="{CIZGI}" stroke-width="2"/>
  <rect x="31" y="900" width="677" height="206" rx="40" fill="url(#{kimlik}-isik)"/>
  <text x="75" y="736" font-size="22" font-weight="600" fill="{MAVI_YAZI}">13:30  ·  Şantiye</text>
  <text x="75" y="806" font-size="46" font-weight="800" letter-spacing="-2" fill="#F7F6F2">Seramik ustasıyla</text>
  <text x="75" y="860" font-size="46" font-weight="800" letter-spacing="-2" fill="#F7F6F2">buluşma</text>
  <text x="75" y="908" font-size="22" fill="{SOLUK}">Kadıköy ofis, Ece Yıldız projesi</text>
  <rect x="75" y="958" width="589" height="80" rx="40" fill="none" stroke="#3A3E41" stroke-width="2.5"/>
  <text x="114" y="1007" font-size="27" font-weight="700" fill="#F2F2F0">İşi tamamla</text>
  <text x="30" y="1188" font-size="28" font-weight="700" fill="#F2F2F0">Bugünkü İşler</text>
  <g font-size="22">
    <rect x="31" y="1222" width="677" height="160" rx="30" fill="{KART}" stroke="{CIZGI}" stroke-width="2"/>
    <circle cx="80" cy="1268" r="15" fill="#37C770"/><path d="M73 1268l5 5 9-10" fill="none" stroke="#0B0C0D" stroke-width="3" stroke-linecap="round"/>
    <text x="110" y="1276" fill="#6E7479" text-decoration="line-through">09:30  Ön görüşme, Deniz Arslan</text>
    <circle cx="80" cy="1336" r="14" fill="none" stroke="#5C6166" stroke-width="2.5"/>
    <text x="110" y="1344" fill="#E8E8E6">15:00  Hakediş tahsilatı, Bora Demir</text>
  </g>''', 'kroki crm telefonda, Panel: İşlerin yolunda, sıradaki iş ve bugünkü işler', logo, 'panel')

def musteriler(kimlik, logo):
    """Müşteriler: aşamaya göre süzülen liste; arama ve WhatsApp kısayolu"""
    kisiler = [('EY', 'Ece Yıldız', 'Randevu Takip', 'Salon yenileme'), ('DA', 'Deniz Arslan', 'Keşif Ölçüm', 'Mutfak'),
               ('SK', 'Selin Kaya', 'Teklif Görüşmesi', 'Ofis'), ('BD', 'Bora Demir', 'Anlaşma Sağlandı', 'Müstakil villa'),
               ('MA', 'Merve Aksoy', 'Teklif Takip', 'Müstakil konut')]
    satir = ''
    for i, (bas, ad, asama, is_) in enumerate(kisiler):
        y = 729 + i * 174
        cizgi = f'<path d="M31 {y + 174}H708" stroke="{CIZGI}" stroke-width="2"/>' if i < 4 else ''
        satir += f'''<rect x="63" y="{y + 57}" width="63" height="63" rx="14" fill="#111314" stroke="#2E3235" stroke-width="2"/>
  <text x="94.5" y="{y + 96}" text-anchor="middle" font-size="22" font-weight="600" fill="#C8CCCF">{bas}</text>
  <text x="146" y="{y + 58}" font-size="28" font-weight="700" fill="#F7F6F2">{ad}</text>
  <text x="146" y="{y + 97}" font-size="20" fill="{MAVI_YAZI}">{asama}</text>
  <text x="146" y="{y + 137}" font-size="22" fill="{SOLUK}">{is_}</text>
  <circle cx="574" cy="{y + 87}" r="31" fill="#173021"/><path d="M563 {y + 77}c0 12 9 21 21 21l4-5-6-4-3 3c-4-1-7-4-8-8l3-3-4-6z" fill="none" stroke="#3CC27A" stroke-width="2.6" stroke-linejoin="round"/>
  <circle cx="646" cy="{y + 87}" r="31" fill="#173021"/><path d="M634 {y + 101}l3-9a13 13 0 1 1 5 5z" fill="none" stroke="#3CC27A" stroke-width="2.8" stroke-linejoin="round"/>
  {cizgi}'''
    return _cerceve(f'''<text x="30" y="295" font-size="62" font-weight="800" letter-spacing="-3" fill="#F7F6F2">Müşteriler</text>
  <rect x="437" y="237" width="271" height="79" rx="39.5" fill="#F2F2F0"/>
  <text x="572.5" y="287" text-anchor="middle" font-size="25" font-weight="700" fill="#111">+ Yeni Müşteri</text>
  <text x="30" y="353" font-size="26" fill="{SOLUK}">24 kayıtlı müşteri</text>
  <rect x="31" y="415" width="677" height="76" rx="38" fill="#111314" stroke="#2A2E31" stroke-width="2"/>
  <rect x="40" y="425" width="170" height="57" rx="28.5" fill="#F2F2F0"/>
  <text x="125" y="461" text-anchor="middle" font-size="22" font-weight="700" fill="#111">Müşteriler</text>
  <text x="241" y="461" font-size="22" fill="#8B9196">Ustalar</text>
  <rect x="31" y="516" width="677" height="83" rx="41.5" fill="#0E1011" stroke="#2A2E31" stroke-width="2"/>
  <text x="63" y="567" font-size="27" fill="#8F959A">İsim veya proje tipi ara...</text>
  <rect x="31" y="617" width="315" height="83" rx="41.5" fill="#0E1011" stroke="#2A2E31" stroke-width="2"/>
  <text x="63" y="668" font-size="27" fill="#E8E8E6">Tüm aşamalar</text>
  <rect x="31" y="729" width="677" height="900" rx="40" fill="{KART}" stroke="{CIZGI}" stroke-width="2"/>
  {satir}''', 'kroki crm telefonda, Müşteriler: aşamalarıyla müşteri listesi, arama ve WhatsApp düğmeleri', logo, 'musteri')

def takvim(kimlik, logo):
    """Takvim: ay görünümü; biten işler üstü çizili, iş türleri renkli"""
    mavi, mor, yesil = ('#17243B', '#3E7BEA', '#6F8FC8'), ('#251C35', '#8E6BD8', '#9B86C9'), ('#152A1C', '#37B36A', '#5FAE7C')
    olaylar = {(0, 3): [('Satış', mavi), ('Sunum', mavi)], (0, 4): [('Teklif', mavi), ('Teklif', mavi), ('Ölçü', mavi)], (0, 5): [('Ölçü', mavi)],
               (1, 0): [('Satış', mavi), ('Revize', mavi), ('Revize', mavi)], (1, 3): [('Randevu', mavi)], (1, 4): [('Teklif', mavi)], (1, 5): [('Randevu', mavi)],
               (2, 3): [('Ödeme', mor)], (2, 4): [('Şantiye', yesil), ('Ölçü', mavi), ('Teklif', mavi)], (2, 5): [('Görüşme', yesil), ('Ödeme', mor)],
               (3, 0): [('Elektrik', yesil)], (3, 2): [('Ölçü', mavi)], (3, 4): [('Sunum', mavi)]}
    satirlar = [820, 1025, 1197, 1369, 1541]
    gunler = [[28, 29, 30, 1, 2, 3, 4], [5, 6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24, 25], [26, 27, 28, 29, 30, 31, 1]]
    g = ''
    for r, ust in enumerate(satirlar):
        for c in range(7):
            x = 31 + c * 96.7
            gecmis = (r == 0 and c < 3) or (r == 4 and c == 6)
            if r == 3 and c == 2:
                g += f'<rect x="{x + 1}" y="{ust + 1}" width="94.7" height="170" fill="#1A2943" stroke="#E8E8E6" stroke-width="3"/>'
            g += f'<text x="{x + 10}" y="{ust + 33}" font-size="22" font-weight="600" fill="{"#4A4F53" if gecmis else ("#4C8DF6" if (r, c) == (3, 2) else "#F2F2F0")}">{gunler[r][c]}</text>'
            for k, (ad, (zemin, nokta, yazi)) in enumerate(olaylar.get((r, c), [])):
                yy = ust + 52 + k * 40
                bitti = r < 3 or (r == 3 and c < 2)
                g += f'<rect x="{x + 5}" y="{yy}" width="86" height="30" rx="8" fill="{zemin}"/><circle cx="{x + 15}" cy="{yy + 15}" r="4" fill="{nokta}"/>'
                ciz = ' text-decoration="line-through"' if bitti else ''
                g += f'<text x="{x + 24}" y="{yy + 21}" font-size="17" fill="{yazi}"{ciz}>{ad}</text>'
    izgara = ''.join(f'<path d="M31 {y}H708" stroke="{CIZGI}" stroke-width="2"/>' for y in satirlar) + ''.join(f'<path d="M{31 + c * 96.7} 820V1600" stroke="{CIZGI}" stroke-width="2"/>' for c in range(1, 7))
    basliklar = ''.join(f'<text x="{80 + c * 96.7}" y="797" text-anchor="middle" font-size="22" fill="{SOLUK}">{a}</text>' for c, a in enumerate(['Pt', 'Sa', 'Ça', 'Pe', 'Cu', 'Ct', 'Pz']))
    return _cerceve(f'''<text x="30" y="290" font-size="62" font-weight="800" letter-spacing="-3" fill="#F7F6F2">Takvim</text>
  <text x="30" y="352" font-size="26" fill="{SOLUK}">Randevu ve şantiye ziyaretleri</text>
  <rect x="31" y="408" width="287" height="79" rx="39.5" fill="#F2F2F0"/>
  <text x="174.5" y="458" text-anchor="middle" font-size="27" font-weight="700" fill="#111">+ Randevu Ekle</text>
  <rect x="31" y="536" width="383" height="83" rx="41.5" fill="#111314" stroke="#2A2E31" stroke-width="2"/>
  <text x="99" y="586" text-anchor="middle" font-size="23" fill="#8B9196">Gün</text><text x="222" y="586" text-anchor="middle" font-size="23" fill="#8B9196">Hafta</text>
  <rect x="286" y="545" width="119" height="65" rx="32.5" fill="#F2F2F0"/><text x="345.5" y="586" text-anchor="middle" font-size="23" font-weight="700" fill="#111">Ay</text>
  <text x="708" y="557" text-anchor="end" font-size="19" fill="{SOLUK}">Seçili gün: 21.10.2026</text>
  <circle cx="67" cy="686" r="36" fill="none" stroke="#2E3235" stroke-width="2"/><path d="M71 676l-9 10 9 10" fill="none" stroke="#F2F2F0" stroke-width="2.6" stroke-linecap="round"/>
  <text x="294" y="695" text-anchor="middle" font-size="27" font-weight="700" fill="#F2F2F0">Ekim 2026</text>
  <circle cx="519" cy="686" r="36" fill="none" stroke="#2E3235" stroke-width="2"/><path d="M515 676l9 10-9 10" fill="none" stroke="#F2F2F0" stroke-width="2.6" stroke-linecap="round"/>
  <rect x="568" y="646" width="144" height="80" rx="40" fill="#0E1011" stroke="#3A3E41" stroke-width="3"/>
  <text x="640" y="696" text-anchor="middle" font-size="25" font-weight="700" fill="#F2F2F0">Bugün</text>
  <rect x="31" y="757" width="677" height="900" rx="34" fill="#111314" stroke="{CIZGI}" stroke-width="2"/>
  {basliklar}{izgara}{g}''', 'kroki crm telefonda, Takvim: ekim ayı görünümü; randevu, teklif, ölçü, ödeme ve şantiye işleri', logo, 'takvim')

def muhasebe(kimlik, logo):
    """Muhasebe: aylık gelen, giden, net ve hareketler"""
    def kart(x, y, w, ad, tutar, renk, kutu, ikon, isik, boyut=46):
        return f'''{_isik(kimlik + isik, renk, x + w / 2, y + 247, w * .55, 90)}
  <rect x="{x}" y="{y}" width="{w}" height="247" rx="38" fill="{KART}" stroke="{CIZGI}" stroke-width="2"/>
  <rect x="{x}" y="{y + 120}" width="{w}" height="127" rx="38" fill="url(#{kimlik}{isik})"/>
  <rect x="{x + 35}" y="{y + 32}" width="57" height="57" rx="14" fill="{kutu}"/><g transform="translate({x + 63.5} {y + 60.5})">{ikon}</g>
  <text x="{x + 35}" y="{y + 132}" font-size="23" fill="{SOLUK}">{ad}</text>
  <text x="{x + 35}" y="{y + 207}" font-size="{boyut}" font-weight="800" letter-spacing="-2" fill="#F7F6F2">{tutar}</text>'''
    def hareket(y, ad, alt, tutar, gelen, cizgi=True):
        renk, kutu = ('#3CCB7F', '#17352A') if gelen else ('#E06A6A', '#3A1C1F')
        ok = 'M0-11v20M-8 2l8 8 8-8' if gelen else 'M0 11v-20M-8-2l8-8 8 8'
        return f'''<rect x="82" y="{y}" width="71" height="70" rx="16" fill="{kutu}"/><path d="{ok}" transform="translate(117.5 {y + 35})" fill="none" stroke="{renk}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="176" y="{y + 30}" font-size="24" font-weight="700" fill="#F7F6F2">{ad}</text>
  <text x="176" y="{y + 63}" font-size="18" fill="{SOLUK}">{alt}</text>
  <text x="657" y="{y + 45}" text-anchor="end" font-size="25" font-weight="700" fill="{renk}">{tutar}</text>
  {f'<path d="M75 {y + 100}H665" stroke="{CIZGI}" stroke-width="2"/>' if cizgi else ''}'''
    onay = '<path d="M-9 0l6 6 12-12" fill="none" stroke="#3CCB7F" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
    cuzdan = '<rect x="-11" y="-8" width="22" height="16" rx="3" fill="none" stroke="#E06A6A" stroke-width="2.6"/><path d="M-11-2h22" stroke="#E06A6A" stroke-width="2.6"/>'
    net = '<path d="M-10-10h8v8h-8zM2-10h8v8H2zM-10 2h8v8h-8z" fill="none" stroke="#4C8DF6" stroke-width="2.6"/>'
    return _cerceve(f'''<circle cx="210" cy="246" r="41" fill="none" stroke="#2E3235" stroke-width="2"/><path d="M214 236l-9 10 9 10" fill="none" stroke="#F2F2F0" stroke-width="2.6" stroke-linecap="round"/>
  <text x="369" y="258" text-anchor="middle" font-size="28" font-weight="700" fill="#F2F2F0">Ekim 2026</text>
  <circle cx="528" cy="246" r="41" fill="none" stroke="#2E3235" stroke-width="2"/><path d="M524 236l9 10-9 10" fill="none" stroke="#F2F2F0" stroke-width="2.6" stroke-linecap="round"/>
  {kart(31, 318, 327, 'Gelen', '185.000 TL', '#1F7A4A', '#17352A', onay, '-g', 44)}
  {kart(380, 318, 328, 'Giden', '42.500 TL', '#7A2626', '#3A1C1F', cuzdan, '-c', 44)}
  {kart(31, 585, 677, 'Net', '+142.500 TL', '#1E4F99', '#1A2A45', net, '-n', 50)}
  <rect x="31" y="872" width="677" height="520" rx="40" fill="{KART}" stroke="{CIZGI}" stroke-width="2"/>
  <text x="75" y="955" font-size="33" font-weight="800" fill="#F7F6F2">Hareketler</text>
  {hareket(1010, 'Ece Yıldız', '17.10.2026 · 2. hakediş', '+60.000 TL', True)}
  {hareket(1132, 'Seramik tedarikçisi', '12.10.2026 · Malzeme', '−42.500 TL', False)}
  {hareket(1254, 'Bora Demir', '03.10.2026 · Tahsilat', '+125.000 TL', True, False)}''', 'kroki crm telefonda, Muhasebe: ekim ayında gelen 185.000 TL, giden 42.500 TL, net 142.500 TL ve hareketler', logo, 'muhasebe')
