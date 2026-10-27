"""pafta. uygulamasının ekranları: kullanıcının telefon ekran görüntülerinden (referans/pafta) vektör olarak yeniden çizildi.
Koordinatlar ekran görüntüsünün 924×2000 hâlindeki pikselleridir. Gerçek müşteri adları örnek adlarla değiştirildi."""

YAZI = "font-family=\"Inter, 'SF Pro Display', -apple-system, 'Segoe UI', sans-serif\""
MAVI = '#1C86EE'
KIRMIZI = '#F26B6B'

def durum_cubugu(renk):
    return f'''<text x="150" y="77" text-anchor="middle" font-size="34" font-weight="600" fill="{renk}">9:41</text>
  <g fill="{renk}"><rect x="676" y="62" width="8" height="14" rx="2"/><rect x="689" y="56" width="8" height="20" rx="2"/><rect x="702" y="50" width="8" height="26" rx="2"/><rect x="715" y="44" width="8" height="32" rx="2"/></g>
  <path d="M742 56a26 26 0 0 1 36 0M749 64a16 16 0 0 1 22 0" fill="none" stroke="{renk}" stroke-width="5" stroke-linecap="round"/><circle cx="760" cy="72" r="4" fill="{renk}"/>
  <rect x="797" y="47" width="56" height="30" rx="9" fill="none" stroke="{renk}" stroke-width="3" opacity=".5"/><rect x="801" y="51" width="40" height="22" rx="6" fill="{renk}"/><rect x="856" y="56" width="4" height="12" rx="2" fill="{renk}" opacity=".5"/>'''

def olcu(x1, y1, x2, y2, etiket, ex=None, ey=None, dik=False, renk=KIRMIZI, sira=0):
    """ölçü çizgisi: uçlarda eğik çentik, ortada etiket (zemin rengiyle kesilmiş); sira: giriş sahnesinde belirme sırası"""
    ex = (x1 + x2) / 2 if ex is None else ex
    ey = (y1 + y2) / 2 if ey is None else ey
    cent = ''.join(f'<path d="M{x - 9} {y + 9}L{x + 9} {y - 9}"/>' for x, y in [(x1, y1), (x2, y2)])
    if dik:
        cent += f'<path d="M{x1 - 14} {y1}H{x1 + 14}M{x2 - 14} {y2}H{x2 + 14}"/>'
    else:
        cent += f'<path d="M{x1} {y1 - 14}V{y1 + 14}M{x2} {y2 - 14}V{y2 + 14}"/>'
    don = f' transform="rotate(90 {ex} {ey})"' if dik else ''
    uz = len(etiket) * 15 + 16
    yazi = f'''<g{don}><rect x="{ex - uz / 2}" y="{ey - 20}" width="{uz}" height="40" fill="#0B0C0E"/><text x="{ex}" y="{ey + 11}" text-anchor="middle" font-size="30" font-weight="600" fill="{renk}">{etiket}</text></g>''' if etiket else ''
    return f'''<g class="ciz-olcu" data-sira="{sira}">
    <g stroke="#8E949B" stroke-width="2" fill="none"><path d="M{x1} {y1}L{x2} {y2}"/>{cent}</g>
    {yazi}
  </g>'''

def plan_cizim():
    """plan ekranındaki L biçimli salon: duvarlar, pencereler, kapılar, kiriş ve ölçüler"""
    duvarlar = ['M338 668H185V700', 'M447 668H745V1300H728', 'M645 1300H628V1033H560', 'M452 1033H185V890', 'M185 805V810']
    yol = ''.join(f'<path d="{d}" pathLength="1"/>' for d in duvarlar)
    pencere = lambda x, y, w, h: f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="#0B0C0E" stroke="#F4F4F4" stroke-width="3"/>' + (
        f'<path d="M{x} {y + h / 2}H{x + w}" stroke="#F4F4F4" stroke-width="2"/>' if w > h else f'<path d="M{x + w / 2} {y}V{y + h}" stroke="#F4F4F4" stroke-width="2"/>')
    return f'''<g>
    <g fill="none" stroke="#F4F4F4" stroke-width="20" stroke-linejoin="miter" class="ciz-duvar">{yol}</g>
    <g fill="none" stroke="#0B0C0E" stroke-width="9" stroke-linejoin="miter" class="ciz-duvar">{yol}</g>
  </g>
  <g class="ciz-olcu" data-sira="1.5">
    {pencere(338, 656, 109, 24)}{pencere(452, 1021, 108, 24)}{pencere(173, 700, 25, 105)}
    <rect x="628" y="1008" width="27" height="27" fill="#F4F4F4"/>
    <path d="M185 810H265M265 810A80 80 0 0 1 185 890" fill="none" stroke="#F4F4F4" stroke-width="4"/>
    <path d="M645 1300V1382M645 1382A83 83 0 0 0 728 1300" fill="none" stroke="#F4F4F4" stroke-width="4"/>
  </g>
  <g class="ciz-olcu" data-sira="1.8">
    <path d="M225 692H720" stroke="#F4F4F4" stroke-width="4" stroke-dasharray="22 14"/>
    <text x="466" y="752" text-anchor="middle" font-size="32" font-weight="600" fill="#3CCB7F">6,27 m</text>
    <text x="312" y="850" text-anchor="middle" font-size="30" font-weight="600" fill="#F4F4F4" transform="rotate(90 312 850)">90/210</text>
  </g>
  {olcu(185, 560, 750, 560, '≈ 6,27 m', sira=2.0)}
  {olcu(185, 617, 750, 617, '', sira=2.1)}
  <g class="ciz-olcu" data-sira="2.1" stroke="#8E949B" stroke-width="2" fill="none"><path d="M329 626L347 608M438 626L456 608"/></g>
  <g class="ciz-olcu" data-sira="2.15" font-size="30" font-weight="600" fill="{KIRMIZI}" text-anchor="middle">
    <rect x="232" y="597" width="96" height="40" fill="#0B0C0E"/><text x="280" y="628">≈140</text>
    <rect x="345" y="597" width="94" height="40" fill="#0B0C0E"/><text x="392" y="628">≈120</text>
    <rect x="534" y="597" width="96" height="40" fill="#0B0C0E"/><text x="582" y="628">≈307</text>
  </g>
  {olcu(92, 668, 92, 1033, '≈ Toplam 4,10 m', dik=True, sira=2.3)}
  {olcu(150, 700, 150, 1033, '≈ 3,80 m', dik=True, sira=2.4)}
  {olcu(265, 690, 265, 805, '≈120', dik=True, sira=2.5)}
  {olcu(185, 983, 635, 983, '', sira=2.6)}
  <g class="ciz-olcu" data-sira="2.65" font-size="30" font-weight="600" fill="{KIRMIZI}" text-anchor="middle">
    <g stroke="#8E949B" stroke-width="2"><path d="M443 992L461 974"/></g>
    <rect x="270" y="963" width="96" height="40" fill="#0B0C0E"/><text x="318" y="994">≈297</text>
    <rect x="458" y="963" width="94" height="40" fill="#0B0C0E"/><text x="505" y="994">≈120</text>
  </g>
  {olcu(185, 1090, 628, 1090, '≈ 4,94 m', sira=2.8)}
  {olcu(775, 668, 775, 1300, '≈ 6,80 m', dik=True, sira=2.9)}
  {olcu(840, 668, 840, 1300, '≈ Toplam 7,10 m', dik=True, sira=3.0)}
  {olcu(700, 1040, 700, 1295, '≈ 3,00 m', dik=True, sira=3.1)}
  {olcu(628, 1250, 750, 1250, '', sira=3.2)}
  <g class="ciz-olcu" data-sira="3.2"><text x="687" y="1434" text-anchor="middle" font-size="32" font-weight="600" fill="{KIRMIZI}">≈ 1,33 m</text></g>'''

def ikon(ad):
    s = 'fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"'
    return {
        'duvar': f'<path {s} d="M-14 14l4-12 18-18 8 8-18 18zM4-12l8 8"/>',
        'kiris': f'<path {s} d="M-20 0h6M-6 0h6M8 0h6M20 0h0"/>',
        'kaydir': f'<path {s} d="M0-20v40M-20 0h40M0-20l-6 6M0-20l6 6M0 20l-6-6M0 20l6-6M-20 0l6-6M-20 0l6 6M20 0l-6-6M20 0l-6 6"/>',
        'ekle': f'<path {s} d="M0-18v36M-18 0h36"/>',
        'geri': f'<path {s} d="M-8-14l-10 10 10 10M-18-4h20a14 14 0 0 1 0 28h-8"/>',
        'sigdir': f'<path {s} d="M-18-8v-10h10M8-18h10v10M18 8v10H8M-8 18h-10V8"/>',
        'temizle': f'<path {s} d="M-16-12h32M-6-12v-6h12v6M-12-12l2 30h20l2-30M-4-4v14M4-4v14"/>',
        'incele': f'<path {s} d="M-22 0s8-14 22-14S22 0 22 0 14 14 0 14-22 0-22 0z"/><circle cx="0" cy="0" r="6" {s}/>',
    }[ad]

def arac_cubugu():
    araclar = [('Kiriş', 'kiris', 194), ('Kaydır', 'kaydir', 296), ('Ekle', 'ekle', 424), ('Geri al', 'geri', 525),
               ('Sığdır', 'sigdir', 627), ('Temizle', 'temizle', 729), ('İncele', 'incele', 831)]
    digerleri = ''.join(f'<g transform="translate({x} 1675)" color="#E6E8EB">{ikon(i)}</g><text x="{x}" y="1737" text-anchor="middle" font-size="26" fill="#C5C9CE">{ad}</text>' for ad, i, x in araclar)
    return f'''<rect x="30" y="1617" width="863" height="160" rx="80" fill="#15181B" stroke="#2A2E33" stroke-width="2"/>
  <rect x="45" y="1632" width="96" height="130" rx="48" fill="{MAVI}"/>
  <g transform="translate(93 1675)" color="#fff">{ikon('duvar')}</g><text x="93" y="1737" text-anchor="middle" font-size="26" font-weight="600" fill="#fff">Duvar</text>
  <path d="M361 1650v110" stroke="#2F343A" stroke-width="2"/>
  {digerleri}'''

def plan_ekrani(kimlik, viewbox='0 0 924 2000'):
    """koyu temada plan ekranı (Duvar aracı seçili)"""
    return f'''<svg class="ekran" viewBox="{viewbox}" {YAZI} role="img" aria-label="pafta. plan ekranı: ölçüleri yazılmış L biçimli salon planı, kiriş, kapı ve pencereler; altta Duvar, Kiriş, Kaydır, Ekle araçları">
  <defs><pattern id="{kimlik}-izgara" width="52" height="52" patternUnits="userSpaceOnUse"><path d="M52 0H0V52" fill="none" stroke="#1D2026" stroke-width="2"/></pattern></defs>
  <rect width="924" height="2000" fill="#0B0C0E"/><rect width="924" height="1900" fill="url(#{kimlik}-izgara)"/>
  {durum_cubugu('#fff')}
  <rect x="30" y="137" width="250" height="100" rx="50" fill="#1A1D21"/>
  <path d="M84 170l-17 17 17 17" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="104" y="199" font-size="34" fill="#fff">Ece hanım</text>
  <rect x="294" y="137" width="162" height="100" rx="50" fill="#1A1D21"/><text x="375" y="199" text-anchor="middle" font-size="34" font-weight="700" fill="#fff" letter-spacing="-1">Salon</text>
  <circle cx="843" cy="187" r="51" fill="#1A1D21"/><g fill="#fff"><circle cx="825" cy="187" r="5"/><circle cx="843" cy="187" r="5"/><circle cx="861" cy="187" r="5"/></g>
  <text x="34" y="291" font-size="30" fill="#8C9096">Bir kare = 50 cm</text>
  <g class="ciz-olcu" data-sira="3.3">
    <rect x="527" y="260" width="367" height="165" rx="26" fill="#15181B" stroke="#2A2E33" stroke-width="2"/>
    <text x="558" y="316" font-size="30" font-weight="600" fill="#fff">Toplam ≈29,71 m²</text><path d="M850 300l7 9 7-9z" fill="#fff"/>
    <text x="558" y="381" font-size="32" font-weight="500" fill="{KIRMIZI}">h 80 cm</text>
  </g>
  {plan_cizim()}
  {arac_cubugu()}
</svg>'''

def musteri_satiri(y, bas, ad, plan, zaman):
    return f'''<rect x="75" y="{y + 53}" width="106" height="106" rx="26" fill="#E5F0FC" stroke="#B9D5F4" stroke-width="2"/>
  <text x="128" y="{y + 118}" text-anchor="middle" font-size="34" font-weight="700" fill="#1C6FCF">{bas}</text>
  <text x="212" y="{y + 74}" font-size="38" font-weight="800" fill="#151515" letter-spacing="-1.2">{ad}</text>
  <text x="212" y="{y + 124}" font-size="31" fill="#1C79DF">{plan}</text>
  <text x="212" y="{y + 171}" font-size="30" fill="#707070">{zaman}</text>
  <path d="M820 {y + 90}l16 17-16 17" fill="none" stroke="#2F86E6" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'''

def ana_ekran(kimlik):
    """açık temada ana ekran: Röleve, müşteri listesi"""
    satirlar = [('EH', 'Ece hanım', '1 plan', 'bugün 09:41'), ('KB', 'Kaan bey', '1 plan', 'dün'), ('SH', 'Selin hanım', '2 plan', 'dün')]
    satir = ''.join(musteri_satiri(846 + i * 215, *r) for i, r in enumerate(satirlar))
    return f'''<svg class="ekran" viewBox="0 0 924 2000" {YAZI} role="img" aria-label="pafta. ana ekranı: Röleve başlığı, 3 müşteri 4 plan, Buluta kaydedildi, Yeni Müşteri düğmesi ve müşteri listesi">
  <defs>
    <pattern id="{kimlik}-izgara" width="52" height="52" patternUnits="userSpaceOnUse"><path d="M52 0H0V52" fill="none" stroke="#DCE7F3" stroke-width="2"/></pattern>
    <linearGradient id="{kimlik}-sol" x1="0" y1="0" x2="0" y2="1"><stop offset=".8" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
    <mask id="{kimlik}-maske"><rect width="924" height="730" fill="url(#{kimlik}-sol)"/></mask>
  </defs>
  <rect width="924" height="2000" fill="#F3F3F1"/>
  <g mask="url(#{kimlik}-maske)">
    <rect width="924" height="730" fill="url(#{kimlik}-izgara)"/>
    <g fill="none" stroke="#8DB9EC" stroke-width="5">
      <path d="M396 390V74H845V390H924M845 390H396"/><path d="M475 64H608M475 84H608" stroke-width="3"/>
      <path d="M396 232H530M615 232H640" stroke-dasharray="26 16"/>
      <path d="M370 74V390M355 74H385M355 390H385" stroke-width="3"/>
      <path d="M607 390V730"/><rect x="591" y="376" width="32" height="32"/><rect x="828" y="62" width="32" height="30"/>
      <path d="M625 525Q650 500 688 497" stroke-width="3"/><path d="M860 62L880 30" stroke-width="3"/>
    </g>
    <text x="327" y="215" font-size="30" font-weight="600" fill="#A9C8EE" transform="rotate(-90 327 215)" text-anchor="middle">320</text>
  </g>
  {durum_cubugu('#151515')}
  <image href="assets/pafta-logo.svg" x="40" y="166" width="172" height="74"/>
  <circle cx="566" cy="197" r="51" fill="#EDEDEB" stroke="#DFDFDD" stroke-width="2"/>
  <g transform="translate(566 197)" fill="none" stroke="#1A1A1A" stroke-width="3.5" stroke-linecap="round"><circle r="10"/><path d="M0-21v-5M0 21v5M-21 0h-5M21 0h5M-15-15l-3-3M15 15l3 3M-15 15l-3 3M15-15l3-3"/></g>
  <rect x="640" y="146" width="244" height="102" rx="51" fill="#EDEDEB" stroke="#DFDFDD" stroke-width="2"/>
  <g transform="translate(694 197)" fill="none" stroke="#1A1A1A" stroke-width="3.5"><circle r="8"/><circle r="17" stroke-dasharray="7 4.6"/></g>
  <text x="732" y="209" font-size="32" fill="#1A1A1A">Ayarlar</text>
  <text x="44" y="405" font-size="92" font-weight="800" fill="#151515" letter-spacing="-4">Röleve</text>
  <text x="44" y="473" font-size="34" fill="#6E6E6E">3 müşteri · 4 plan</text>
  <rect x="44" y="546" width="359" height="82" rx="41" fill="#ECECEA" stroke="#DDDDDB" stroke-width="2"/>
  <path d="M80 602h28a10 10 0 0 0 0-20 14 14 0 0 0-27-3 9 9 0 0 0-1 23z" fill="#fff" stroke="#C9C9C7" stroke-width="2"/>
  <text x="122" y="599" font-size="30" font-weight="500" fill="#5B9BE3">Buluta kaydedildi</text>
  <rect x="415" y="527" width="341" height="117" rx="58" fill="{MAVI}"/>
  <text x="586" y="599" text-anchor="middle" font-size="36" font-weight="700" fill="#fff" letter-spacing="-1">+ Yeni Müşteri</text>
  <text x="44" y="802" font-size="42" font-weight="800" fill="#151515" letter-spacing="-1.5">Müşteriler</text>
  <text x="880" y="798" text-anchor="end" font-size="30" fill="#6E6E6E">son değişen üstte</text>
  <rect x="40" y="846" width="844" height="646" rx="54" fill="#fff" stroke="#E2E2E0" stroke-width="2"/>
  <path d="M40 1061H884M40 1276H884" stroke="#E8E8E6" stroke-width="2"/>{satir}
</svg>'''

def musteri_ekrani(kimlik):
    """koyu temada müşteri ekranı: planlar"""
    return f'''<svg class="ekran" viewBox="0 0 924 2000" {YAZI} role="img" aria-label="pafta. müşteri ekranı: Ece hanım, 1 plan, Yeni Plan düğmesi ve Salon planı">
  <defs>
    <pattern id="{kimlik}-izgara" width="52" height="52" patternUnits="userSpaceOnUse"><path d="M52 0H0V52" fill="none" stroke="#1A1D22" stroke-width="2"/></pattern>
    <linearGradient id="{kimlik}-sol" x1="0" y1="0" x2="0" y2="1"><stop offset=".8" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
    <mask id="{kimlik}-maske"><rect width="924" height="705" fill="url(#{kimlik}-sol)"/></mask>
  </defs>
  <rect width="924" height="2000" fill="#0B0C0E"/>
  <g mask="url(#{kimlik}-maske)">
    <rect width="924" height="705" fill="url(#{kimlik}-izgara)"/>
    <g fill="none" stroke="#1F4E86" stroke-width="5">
      <path d="M924 38H448V432H924"/><path d="M686 40V430" stroke-dasharray="20 14" stroke-width="3"/>
      <path d="M452 380H554M554 380A102 102 0 0 0 452 278" stroke-width="3"/>
      <path d="M448 470H924M448 456V484" stroke-width="3"/><rect x="433" y="22" width="32" height="30"/>
    </g>
    <text x="727" y="517" text-anchor="middle" font-size="32" font-weight="600" fill="#3B6FAF">525</text>
  </g>
  {durum_cubugu('#fff')}
  <rect x="39" y="146" width="284" height="102" rx="51" fill="#1A1D21"/>
  <path d="M94 180l-17 17 17 17" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="117" y="209" font-size="32" fill="#fff">Müşteriler</text>
  <text x="44" y="405" font-size="88" font-weight="800" fill="#fff" letter-spacing="-4">Ece hanım</text>
  <text x="44" y="473" font-size="34" fill="#8A8F96">1 plan</text>
  <rect x="44" y="527" width="284" height="117" rx="58" fill="{MAVI}"/>
  <text x="186" y="599" text-anchor="middle" font-size="36" font-weight="700" fill="#fff" letter-spacing="-1">+ Yeni Plan</text>
  <text x="44" y="778" font-size="42" font-weight="800" fill="#fff" letter-spacing="-1.5">Planlar</text>
  <rect x="40" y="822" width="844" height="218" rx="54" fill="#14171A" stroke="#262A2F" stroke-width="2"/>
  <rect x="75" y="856" width="148" height="148" rx="28" fill="#0B0C0E" stroke="#2A2E33" stroke-width="2"/>
  <path d="M98 876H200V988H178V940H98Z" fill="none" stroke="{MAVI}" stroke-width="6"/><path d="M104 884H194" stroke="{MAVI}" stroke-width="2" stroke-dasharray="6 5"/>
  <text x="254" y="921" font-size="38" font-weight="700" fill="#fff" letter-spacing="-1">Salon</text>
  <text x="254" y="972" font-size="30" fill="#8A8F96">dün</text>
  <circle cx="803" cy="931" r="51" fill="#1E2226"/><g fill="#fff"><circle cx="785" cy="931" r="5"/><circle cx="803" cy="931" r="5"/><circle cx="821" cy="931" r="5"/></g>
  <text x="462" y="1150" text-anchor="middle" font-size="32" fill="#F06A6A">Müşteriyi sil</text>
</svg>'''

def telefon(svg):
    return f'<div class="cep"><div class="cep__ekran">{svg}<span class="cep__ada" aria-hidden="true"></span></div></div>'
