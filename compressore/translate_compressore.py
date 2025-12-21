import json

# Translation Map (Hungarian -> Czech)
translations = {
    "1 db 5 méteres cső": "1 ks 5metrová hadice",
    "1 pár újrahasználható kesztyű": "1 pár opakovaně použitelných rukavic",
    "12 literes tartály: Optimális kapacitás a jó munkavégzési autonómia érdekében, csökkenti a töltési szüneteket és növeli a termelékenységet": "12litrová nádrž: Optimální kapacita pro dobrou pracovní autonomii, snižuje přestávky na doplňování a zvyšuje produktivitu",
    "1LE-s motor: Erős és megbízható, akár 8 Bar és 115 l/perc teljesítmény felfújáshoz, kifújáshoz és festéshez": "Motor 1 HP: Silný a spolehlivý, výkon až 8 barů a 115 l/min pro nafukování, ofukování a lakování",
    "2 db akkumulátor mellékelve": "Včetně 2 ks baterií",
    "2 év műszaki támogatás": "2 roky technické podpory",
    "62 dB-es halk működés: Ultra csendes működés, tökéletes beltéri vagy közös használatra, anélkül hogy zavarná a környezetet": "Tichý chod 62 dB: Ultra tichý provoz, ideální pro vnitřní nebo společné použití bez rušení okolí",
    "74663 Ft helyett": "Místo 2600 Kč",
    "<h3><!--StartFragment --></h3><h3><!--StartFragment --></h3><h3><span style=\"text-decoration: underline;\">Halk és könnyen szállítható</span></h3><p><strong>Mindössze 62 dB zajkibocsátással ideális beltéri használatra anélkül, hogy zavarna. A kompakt és olajmentes kialakítás praktikus mozgatást és használatot tesz lehetővé bárhol: otthon, garázsban vagy műhelyben</strong><br /><!--EndFragment --></p><p><!--StartFragment --></p>": "<h3><!--StartFragment --></h3><h3><!--StartFragment --></h3><h3><span style=\"text-decoration: underline;\">Tichý a snadno přenosný</span></h3><p><strong>s hlučností pouhých 62 dB je ideální pro vnitřní použití bez rušení. Kompaktní a bezolejový design umožňuje praktický přesun a použití kdekoli: doma, v garáži nebo v dílně</strong><br /><!--EndFragment --></p><p><!--StartFragment --></p>",
    "<h4 class=\"a-size-large a-spacing-none\"><!--StartFragment --></h4><h3><!--StartFragment --></h3><h3><span style=\"text-decoration: underline;\">Kompakt teljesítmény 1LE</span></h3><p><strong>Egy lóerős elektromos motorral felszerelve ez a kompresszor eléri a 8 Bar maximális nyomást és 115 liter/perc légáramot. Ideális teljesítmény kerekek felfújásához, por kifújásához, szögeléshez vagy precíz festéshez, akár otthoni vagy kézműves környezetben is</strong><br /><!--EndFragment --></p><p><!--EndFragment --></p><p><!--EndFragment --></p>": "<h4 class=\"a-size-large a-spacing-none\"><!--StartFragment --></h4><h3><!--StartFragment --></h3><h3><span style=\"text-decoration: underline;\">Kompaktní výkon 1 HP</span></h3><p><strong>Vybaven elektromotorem o výkonu jedné koňské síly dosahuje tento kompresor maximálního tlaku 8 barů a průtoku vzduchu 115 litrů/min. Ideální výkon pro nafukování kol, ofukování prachu, hmoždinkování nebo přesné lakování, a to i v domácím či řemeslném prostředí</strong><br /><!--EndFragment --></p><p><!--EndFragment --></p><p><!--EndFragment --></p>",
    "<h4 class=\"a-spacing-mini\"><!--StartFragment --></h4><h3><!--StartFragment --></h3><h3><!--StartFragment --></h3><h3><span style=\"text-decoration: underline;\">ECO technológia olaj nélkül</span></h3><p><strong>Az olajmentes rendszer kiküszöböli a karbantartás szükségességét és tiszta működést biztosít. Az ECO technológia alacsony fordulatszámmal csökkenti az energiafogyasztást és meghosszabbítja a kompresszor élettartamát, fenntartható és megbízható megoldást kínálva</strong><br /><!--EndFragment --></p><p class=\"a-spacing-mini\"><!--StartFragment --></p>": "<h4 class=\"a-spacing-mini\"><!--StartFragment --></h4><h3><!--StartFragment --></h3><h3><!--StartFragment --></h3><h3><span style=\"text-decoration: underline;\">ECO technologie bez oleje</span></h3><p><strong>Bezolejový systém eliminuje nutnost údržby a zajišťuje čistý provoz. Technologie ECO s nízkými otáčkami snižuje spotřebu energie a prodlužuje životnost kompresoru, nabízí tak udržitelné a spolehlivé řešení</strong><br /><!--EndFragment --></p><p class=\"a-spacing-mini\"><!--StartFragment --></p>",
    "<h4 class=\"a-spacing-mini\"><!--StartFragment --></h4><h3><!--StartFragment --></h3><h3><span style=\"text-decoration: underline;\">12 literes alumínium tartály olajmentes szivattyúval és leeresztő szeleppel</span></h3><p><strong>Könnyű és strapabíró, a 12 literes tartály jó autonómiát biztosít szakaszos munkákhoz. Az olajmentes szivattyú karbantartásmentes működést garantál, míg a leeresztő szelep megkönnyíti a kondenzvíz eltávolítását, javítva a rendszer hatékonyságát és tisztaságát</strong><br /><!--EndFragment --></p><p><!--StartFragment --></p>": "<h4 class=\"a-spacing-mini\"><!--StartFragment --></h4><h3><!--StartFragment --></h3><h3><span style=\"text-decoration: underline;\">12litrová hliníková nádrž s bezolejovým čerpadlem a vypouštěcím ventilem</span></h3><p><strong>Lehká a odolná 12litrová nádrž zajišťuje dobrou autonomii pro přerušované práce. Bezolejové čerpadlo zaručuje bezúdržbový provoz, zatímco vypouštěcí ventil usnadňuje odstraňování kondenzátu, čímž zvyšuje účinnost a čistotu systému</strong><br /><!--EndFragment --></p><p><!--StartFragment --></p>",
    "<p data-start=\"4857\" data-end=\"4876\">PRIVACY | CONTATTI</p>": "<p data-start=\"4857\" data-end=\"4876\">OCHRANA SOUKROMÍ | KONTAKTY</p>",
    "<p style=\"margin-bottom: 0.9rem; caret-color: #333333; color: #333333; font-size: 12px; text-align: center; text-size-adjust: auto;\">This site is not a part of the Facebook website or Facebook Inc. Additionally, this site is NOT endorsed by Facebook in any way. Facebook is a trademark of Facebook, Inc</p>": "<p style=\"margin-bottom: 0.9rem; caret-color: #333333; color: #333333; font-size: 12px; text-align: center; text-size-adjust: auto;\">Tento web není součástí webu Facebook ani společnosti Facebook Inc. Kromě toho tento web NENÍ žádným způsobem podporován společností Facebook. Facebook je ochranná známka společnosti Facebook, Inc.</p>",
    "<p>© 2023 Tutti i diritti riservati.</p>": "<p>© 2023 Všechna práva vyhrazena.</p>",
    "<u>AZ ÚJ, KIVÉTELES AirForce One 2025</u>": "<u>NOVÝ A VÝJIMEČNÝ AirForce One 2025</u>",
    "A Professzionális Légkompresszor Manométerrel, amely Felfúj, Szív, Fúj és Permetez 115 Liter/perc sebességgel gyorsan és könnyedén, tökéletes kerekekhez, festéshez, otthoni tisztításhoz, nyomásos fúráshoz és kézműves munkákhoz": "Profesionální vzduchový kompresor s manometrem, který nafukuje, saje, fouká a stříká rychlostí 115 litrů za minutu rychle a snadno, perfektní pro kola, malování, domácí úklid, tlakové vrtání a řemeslné práce",
    "AirForce One<br>+ Univerzális felfújófej készlet<br>+ 2 db akkumulátor mellékelve<br>+ 1 db 5 méteres cső<br>+ Fúvófej<br>+ Szerszámtartó táska<br>+ 1 pár újrahasználható kesztyű<br>CSAK 19999 Ft": "AirForce One<br>+ Sada univerzálních nafukovacích hlavic<br>+ Včetně 2 ks baterií<br>+ 1 ks 5metrové hadice<br>+ Ofukovací tryska<br>+ Taška na nářadí<br>+ 1 pár opakovaně použitelných rukavic<br>JEN 1248 Kč",
    "Alumínium anyag: Könnyű és korrózióálló szerkezet, ideális hosszan tartó használatra és könnyű szállításra anélkül, hogy a tartósság csorbulna": "Hliníkový materiál: Lehká konstrukce odolná proti korozi, ideální pro dlouhodobé používání a snadnou přepravu bez snížení odolnosti",
    "ECO alacsony fordulatszámmal és csökkentett fogyasztással: Fenntartható kompresszor, amely hosszú élettartamot biztosít és kíméli a környezetet": "ECO s nízkými otáčkami a sníženou spotřebou: Udržitelný kompresor, který zajišťuje dlouhou životnost a šetří životní prostředí",
    "Elégedettségi vagy pénzvisszafizetési garancia": "Záruka spokojenosti nebo vrácení peněz",
    "Forradalmasítsd a munkád levegővel: erő, csend és kompakt sokoldalúság minden projekthez, a felfújástól a festésig": "Revolucionalizujte svou práci se vzduchem: síla, ticho a kompaktní všestrannost pro každý projekt, od nafukování po lakování",
    "Fúvófej": "Ofukovací tryska",
    "Gyors házhoz szállítás": "Rychlé doručení domů",
    "Gyors szállítás": "Rychlé doručení",
    "Ha ma rendeled meg, ajándékba kapod:<br><br>AirForce One<br>+ Univerzális felfújófej készlet<br>+ 2 db akkumulátor mellékelve<br>+ 1 db 5 méteres cső<br>+ Fúvófej<br>+ Szerszámtartó táska<br>+ 1 pár újrahasználható kesztyű<br>+Gyors és biztosított szállítás": "Pokud objednáte dnes, dostanete jako dárek:<br><br>AirForce One<br>+ Sada univerzálních nafukovacích hlavic<br>+ Včetně 2 ks baterií<br>+ 1 ks 5metrové hadice<br>+ Ofukovací tryska<br>+ Taška na nářadí<br>+ 1 pár opakovaně použitelných rukavic<br>+ Rychlé a pojištěné doručení",
    "Használatra kész: Könnyen elindítható, nem igényel bonyolult előkészületeket: csak csatlakoztatni kell és már kezdődhet is a munka, akár kezdők számára is": "Připraven k použití: Snadné spuštění, nevyžaduje složité přípravy: stačí připojit a práce může začít, vhodné i pro začátečníky",
    "Ideális barkácsoláshoz és kézművességhez: Tökéletes társ hobbistáknak és szakembereknek, akik kompakt és halk formátumban keresnek magas teljesítményt": "Ideální pro kutilství a řemesla: Perfektní společník pro hobbisty i profesionály, kteří hledají vysoký výkon v kompaktním a tichém provedení",
    "Kompakt és halk, olajmentes és karbantartásmentes szivattyúval, leeresztő szeleppel, 8 BAR teljesítménnyel és 18V-os akkumulátorral a biztonságos, hatékony munkához bárhol": "Kompaktní a tichý, s bezolejovým a bezúdržbovým čerpadlem, vypouštěcím ventilem, výkonem 8 BAR a 18V baterií pro bezpečnou a efektivní práci kdekoli",
    "Kompakt és hordozható kialakítás: Könnyen mozgatható és tárolható, ideális otthoni környezetbe, garázsba vagy kis műhelyekbe, ahol korlátozott a hely": "Kompaktní a přenosný design: Snadno se přenáší a skladuje, ideální pro domácí prostředí, garáže nebo malé dílny s omezeným prostorem",
    "Leeresztő szelep: Egyszerű és gyors kondenzvíz eltávolítást tesz lehetővé, javítva a kompresszor hatékonyságát és élettartamát": "Vypouštěcí ventil: Umožňuje jednoduché a rychlé odstranění kondenzátu, zlepšuje účinnost a životnost kompresoru",
    "Olajmentes szivattyú: Tiszta és karbantartásmentes működést biztosít, ideális olyan helyeken, ahol fontos a levegő tisztasága": "Bezolejové čerpadlo: Zajišťuje čistý a bezúdržbový provoz, ideální v místech, kde je důležitá čistota vzduchu",
    "Olajmentes technológia és nincs szükség karbantartásra: A rendszer tiszta működést garantál, csökkenti a költségeket és megkönnyíti a használatot": "Bezolejová technologie a žádná nutnost údržby: Systém zaručuje čistý provoz, snižuje náklady a usnadňuje použití",
    "Sokoldalú használat: Alkalmas autó-, motor- és kerékpárgumik, labdák, matracok felfújására, valamint por vagy szennyeződés kifújására felületekről és alkatrészekről": "Všestranné použití: Vhodné pro nafukování pneumatik aut, motocyklů a kol, míčů, matrací, stejně jako pro ofukování prachu či nečistot z povrchů a dílů",
    "Szerszámtartó táska": "Taška na nářadí",
    "TELJES KÉSZLET AJÁNLAT": "NABÍDKA KOMPLETNÍ SADY",
    "Továbbá, ha ma rendeled meg, ajándékba kapsz egy ingyenes garancia-kiterjesztést a cserealkatrészekre, amely 2 évig érvényes.": "Navíc, pokud objednáte dnes, získáte zdarma prodlouženou záruku na náhradní díly, která platí 2 roky.",
    "Töltse ki az alábbi űrlapot a professzionális AirForce One kompresszor megrendeléséhez garanciával és szállítással, mindössze 19999 Ft-ért": "Vyplňte níže uvedený formulář pro objednání profesionálního kompresoru AirForce One se zárukou a dopravou jen za 1248 Kč",
    "Töltse ki az űrlapot a rendeléshez": "Vyplňte formulář pro objednání",
    "Univerzális felfújófej készlet": "Sada univerzálních nafukovacích hlavic",
    "Ügyfélszolgálat és alkatrészek 2 ÉVIG benne vannak": "Zákaznický servis a náhradní díly zahrnuty po dobu 2 LET"
}

def translate_recursive(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, str):
                # If exact match
                if value in translations:
                    data[key] = translations[value]
                # Special handling if needed? Usually precise match is safer.
                
            elif isinstance(value, (dict, list)):
                translate_recursive(value)
    elif isinstance(data, list):
        for item in data:
            translate_recursive(item)

def main():
    input_file = "compressore-hu.json"
    output_file = "compressore-cz.json"
    
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    translate_recursive(data)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False) # Minified? Elementor usually prefers minified but readable is fine.
        # Original was minified (one line). I should probably output minimal json to be safe.
        # To match input format (one line), I'll re-dump.
        
    # Re-reading to minify if desired:
    # json.dump usually produces minified if indent is None (default).
    
    print(f"Created {output_file} successfully.")

if __name__ == "__main__":
    main()
