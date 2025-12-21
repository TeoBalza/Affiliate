import json

# Input and Output files
INPUT_FILE = '/Users/matteo/Documents/GitHub/forno/compressore/compressore-hu.json'
OUTPUT_FILE = '/Users/matteo/Documents/GitHub/forno/compressore/compressore-sk.json'

# Exact text replacements
REPLACEMENTS = {
    "<u>AZ ÚJ, KIVÉTELES AirForce One 2025</u>": "<u>NOVÝ, VÝNIMOČNÝ AirForce One 2025</u>",
    "A Professzionális Légkompresszor Manométerrel, amely Felfúj, Szív, Fúj és Permetez 115 Liter/perc sebességgel gyorsan és könnyedén, tökéletes kerekekhez, festéshez, otthoni tisztításhoz, nyomásos fúráshoz és kézműves munkákhoz": "Profesionálny vzduchový kompresor s manometrom, ktorý nafukuje, saje, fúka a strieka rýchlosťou 115 litrov/minútu, rýchlo a ľahko, ideálny pre kolesá, maľovanie, domáce čistenie, tlakové vŕtanie a remeselné práce",
    "Kompakt és halk, olajmentes és karbantartásmentes szivattyúval, leeresztő szeleppel, 8 BAR teljesítménnyel és 18V-os akkumulátorral a biztonságos, hatékony munkához bárhol": "Kompaktný a tichý, s bezolejovým a bezúdržbovým čerpadlom, vypúšťacím ventilom, výkonom 8 BAR a 18V batériou pre bezpečnú a efektívnu prácu kdekoľvek",
    "TELJES KÉSZLET AJÁNLAT": "PONUKA KOMPLETNEJ SADY",
    "AirForce One<br>+ Univerzális felfújófej készlet<br>+ 2 db akkumulátor mellékelve<br>+ 1 db 5 méteres cső<br>+ Fúvófej<br>+ Szerszámtartó táska<br>+ 1 pár újrahasználható kesztyű<br>CSAK 19999 Ft": "AirForce One<br>+ Súprava univerzálnych nafukovacích hláv<br>+ 2 ks batérií v balení<br>+ 1 ks 5-metrovej hadice<br>+ Fúkacia tryska<br>+ Taška na náradie<br>+ 1 pár opakovane použiteľných rukavíc<br>LEN 49 €",
    "74663 Ft helyett": "namiesto 100 €",
    "Ügyfélszolgálat és alkatrészek 2 ÉVIG benne vannak": "Zákaznícka podpora a náhradné diely na 2 ROKY v cene",
    "Töltse ki az űrlapot a rendeléshez": "Vyplňte formulár pre objednávku",
    "Forradalmasítsd a munkád levegővel: erő, csend és kompakt sokoldalúság minden projekthez, a felfújástól a festésig": "Revolucionujte svoju prácu so vzduchom: sila, ticho a kompaktná všestrannosť pre každý projekt, od nafukovania po maľovanie",
    
    # HTML Editor Content 1
    "<h4 class=\"a-size-large a-spacing-none\"><!--StartFragment --></h4><h3><!--StartFragment --></h3><h3><span style=\"text-decoration: underline;\">Kompakt teljesítmény 1LE</span></h3><p><strong>Egy lóerős elektromos motorral felszerelve ez a kompresszor eléri a 8 Bar maximális nyomást és 115 liter/perc légáramot. Ideális teljesítmény kerekek felfújásához, por kifújásához, szögeléshez vagy precíz festéshez, akár otthoni vagy kézműves környezetben is</strong><br /><!--EndFragment --></p><p><!--EndFragment --></p><p><!--EndFragment --></p>":
    "<h4 class=\"a-size-large a-spacing-none\"><!--StartFragment --></h4><h3><!--StartFragment --></h3><h3><span style=\"text-decoration: underline;\">Kompaktný výkon 1 HP</span></h3><p><strong>Vybavený elektrickým motorom s výkonom jednej konskej sily, tento kompresor dosahuje maximálny tlak 8 Bar a prietok vzduchu 115 litrov/minútu. Ideálny výkon na nafukovanie kolies, vyfukovanie prachu, klincovanie alebo precízne maľovanie, či už v domácom alebo remeselnom prostredí</strong><br /><!--EndFragment --></p><p><!--EndFragment --></p><p><!--EndFragment --></p>",

    # HTML Editor Content 2
    "<h4 class=\"a-spacing-mini\"><!--StartFragment --></h4><h3><!--StartFragment --></h3><h3><span style=\"text-decoration: underline;\">12 literes alumínium tartály olajmentes szivattyúval és leeresztő szeleppel</span></h3><p><strong>Könnyű és strapabíró, a 12 literes tartály jó autonómiát biztosít szakaszos munkákhoz. Az olajmentes szivattyú karbantartásmentes működést garantál, míg a leeresztő szelep megkönnyíti a kondenzvíz eltávolítását, javítva a rendszer hatékonyságát és tisztaságát</strong><br /><!--EndFragment --></p><p><!--StartFragment --></p>":
    "<h4 class=\"a-spacing-mini\"><!--StartFragment --></h4><h3><!--StartFragment --></h3><h3><span style=\"text-decoration: underline;\">12-litrová hliníková nádrž s bezolejovým čerpadlom a vypúšťacím ventilom</span></h3><p><strong>Ľahká a odolná 12-litrová nádrž zaisťuje dobrú autonómiu pre prerušované práce. Bezolejové čerpadlo zaručuje bezúdržbovú prevádzku, zatiaľ čo vypúšťací ventil uľahčuje odstraňovanie kondenzátu, čím zvyšuje účinnosť a čistotu systému</strong><br /><!--EndFragment --></p><p><!--StartFragment --></p>",

    # HTML Editor Content 3
    "<h3><!--StartFragment --></h3><h3><!--StartFragment --></h3><h3><span style=\"text-decoration: underline;\">Halk és könnyen szállítható</span></h3><p><strong>Mindössze 62 dB zajkibocsátással ideális beltéri használatra anélkül, hogy zavarna. A kompakt és olajmentes kialakítás praktikus mozgatást és használatot tesz lehetővé bárhol: otthon, garázsban vagy műhelyben</strong><br /><!--EndFragment --></p><p><!--StartFragment --></p>":
    "<h3><!--StartFragment --></h3><h3><!--StartFragment --></h3><h3><span style=\"text-decoration: underline;\">Tichý a ľahko prenosný</span></h3><p><strong>S hlučnosťou iba 62 dB je ideálny na vnútorné použitie bez toho, aby rušil. Kompaktný a bezolejový dizajn umožňuje praktické presúvanie a použitie kdekoľvek: doma, v garáži alebo v dielni</strong><br /><!--EndFragment --></p><p><!--StartFragment --></p>",

    # HTML Editor Content 4
    "<h4 class=\"a-spacing-mini\"><!--StartFragment --></h4><h3><!--StartFragment --></h3><h3><!--StartFragment --></h3><h3><span style=\"text-decoration: underline;\">ECO technológia olaj nélkül</span></h3><p><strong>Az olajmentes rendszer kiküszöböli a karbantartás szükségességét és tiszta működést biztosít. Az ECO technológia alacsony fordulatszámmal csökkenti az energiafogyasztást és meghosszabbítja a kompresszor élettartamát, fenntartható és megbízható megoldást kínálva</strong><br /><!--EndFragment --></p><p class=\"a-spacing-mini\"><!--StartFragment --></p>":
    "<h4 class=\"a-spacing-mini\"><!--StartFragment --></h4><h3><!--StartFragment --></h3><h3><!--StartFragment --></h3><h3><span style=\"text-decoration: underline;\">ECO technológia bez oleja</span></h3><p><strong>Bezolejový systém eliminuje potrebu údržby a zaisťuje čistú prevádzku. ECO technológia s nízkymi otáčkami znižuje spotrebu energie a predlžuje životnosť kompresora, ponúkajúc udržateľné a spoľahlivé riešenie</strong><br /><!--EndFragment --></p><p class=\"a-spacing-mini\"><!--StartFragment --></p>",

    "Ha ma rendeled meg, ajándékba kapod:<br><br>AirForce One<br>+ Univerzális felfújófej készlet<br>+ 2 db akkumulátor mellékelve<br>+ 1 db 5 méteres cső<br>+ Fúvófej<br>+ Szerszámtartó táska<br>+ 1 pár újrahasználható kesztyű<br>+Gyors és biztosított szállítás":
    "Ak si objednáte dnes, dostanete ako darček:<br><br>AirForce One<br>+ Súprava univerzálnych nafukovacích hláv<br>+ 2 ks batérií v balení<br>+ 1 ks 5-metrovej hadice<br>+ Fúkacia tryska<br>+ Taška na náradie<br>+ 1 pár opakovane použiteľných rukavíc<br>+ Rýchle a poistené doručenie",

    # Icon List Items
    "AirForce One": "AirForce One",
    "Univerzális felfújófej készlet": "Súprava univerzálnych nafukovacích hláv",
    "2 db akkumulátor mellékelve": "2 ks batérií v balení",
    "1 db 5 méteres cső": "1 ks 5-metrovej hadice",
    "Fúvófej": "Fúkacia tryska",
    "Szerszámtartó táska": "Taška na náradie",
    "1 pár újrahasználható kesztyű": "1 pár opakovane použiteľných rukavíc",
    "2 év műszaki támogatás": "2 roky technickej podpory",
    "Gyors házhoz szállítás": "Rýchle doručenie domov",
    "Gyors szállítás": "Rýchle doručenie",
    "Alumínium anyag: Könnyű és korrózióálló szerkezet, ideális hosszan tartó használatra és könnyű szállításra anélkül, hogy a tartósság csorbulna": "Hliníkový materiál: Ľahká a korózii odolná konštrukcia, ideálna na dlhodobé používanie a jednoduchú prepravu bez zníženia odolnosti",
    "1LE-s motor: Erős és megbízható, akár 8 Bar és 115 l/perc teljesítmény felfújáshoz, kifújáshoz és festéshez": "Motor 1 HP: Silný a spoľahlivý, výkon až 8 Bar a 115 l/min na nafukovanie, vyfukovanie a maľovanie",
    "12 literes tartály: Optimális kapacitás a jó munkavégzési autonómia érdekében, csökkenti a töltési szüneteket és növeli a termelékenységet": "12-litrová nádrž: Optimálna kapacita pre dobrú pracovnú autonómiu, znižuje prestávky na plnenie a zvyšuje produktivitu",
    "Kompakt és hordozható kialakítás: Könnyen mozgatható és tárolható, ideális otthoni környezetbe, garázsba vagy kis műhelyekbe, ahol korlátozott a hely": "Kompaktný a prenosný dizajn: Ľahko sa presúva a skladuje, ideálny do domáceho prostredia, garáže alebo malých dielní s obmedzeným priestorom",
    "Olajmentes szivattyú: Tiszta és karbantartásmentes működést biztosít, ideális olyan helyeken, ahol fontos a levegő tisztasága": "Bezolejové čerpadlo: Zaisťuje čistú a bezúdržbovú prevádzku, ideálne na miestach, kde je dôležitá čistota vzduchu",
    "Leeresztő szelep: Egyszerű és gyors kondenzvíz eltávolítást tesz lehetővé, javítva a kompresszor hatékonyságát és élettartamát": "Vypúšťací ventil: Umožňuje jednoduché a rýchle odstránenie kondenzátu, čím zlepšuje účinnosť a životnosť kompresora",
    "62 dB-es halk működés: Ultra csendes működés, tökéletes beltéri vagy közös használatra, anélkül hogy zavarná a környezetet": "Tichá prevádzka 62 dB: Ultra tichá prevádzka, ideálna na vnútorné alebo spoločné použitie bez rušenia okolia",
    "Olajmentes technológia és nincs szükség karbantartásra: A rendszer tiszta működést garantál, csökkenti a költségeket és megkönnyíti a használatot": "Bezolejová technológia a žiadna údržba: Systém zaručuje čistú prevádzku, znižuje náklady a uľahčuje používanie",
    "ECO alacsony fordulatszámmal és csökkentett fogyasztással: Fenntartható kompresszor, amely hosszú élettartamot biztosít és kíméli a környezetet": "ECO s nízkymi otáčkami a zníženou spotrebou: Udržateľný kompresor, ktorý zaisťuje dlhú životnosť a šetrí životné prostredie",
    "Sokoldalú használat: Alkalmas autó-, motor- és kerékpárgumik, labdák, matracok felfújására, valamint por vagy szennyeződés kifújására felületekről és alkatrészekről": "Všestranné použitie: Vhodné na nafukovanie pneumatík áut, motoriek a bicyklov, lôpt, matracov, ako aj na vyfukovanie prachu alebo nečistôt z povrchov a súčiastok",
    "Ideális barkácsoláshoz és kézművességhez: Tökéletes társ hobbistáknak és szakembereknek, akik kompakt és halk formátumban keresnek magas teljesítményt": "Ideálne pre kutilstvo a remeslá: Dokonalý spoločník pre hobbystov a profesionálov, ktorí hľadajú vysoký výkon v kompaktnom a tichom formáte",
    "Használatra kész: Könnyen elindítható, nem igényel bonyolult előkészületeket: csak csatlakoztatni kell és már kezdődhet is a munka, akár kezdők számára is": "Pripravený na použitie: Ľahko sa spúšťa, nevyžaduje zložité prípravy: stačí zapojiť a práca sa môže začať, aj pre začiatočníkov",
    "Elégedettségi vagy pénzvisszafizetési garancia": "Záruka spokojnosti alebo vrátenia peňazí",

    "Továbbá, ha ma rendeled meg, ajándékba kapsz egy ingyenes garancia-kiterjesztést a cserealkatrészekre, amely 2 évig érvényes.": "Navyše, ak si objednáte dnes, dostanete zadarmo predĺženú záruku na náhradné diely platnú 2 roky.",
    "Töltse ki az alábbi űrlapot a professzionális AirForce One kompresszor megrendeléséhez garanciával és szállítással, mindössze 19999 Ft-ért": "Vyplňte nižšie uvedený formulár a objednajte si profesionálny kompresor AirForce One so zárukou a doručením, len za 49 €",
    
    # Disclaimer and Footer
    "<p style=\"margin-bottom: 0.9rem; caret-color: #333333; color: #333333; font-size: 12px; text-align: center; text-size-adjust: auto;\">This site is not a part of the Facebook website or Facebook Inc. Additionally, this site is NOT endorsed by Facebook in any way. Facebook is a trademark of Facebook, Inc</p>":
    "<p style=\"margin-bottom: 0.9rem; caret-color: #333333; color: #333333; font-size: 12px; text-align: center; text-size-adjust: auto;\">Táto stránka nie je súčasťou webovej stránky Facebook ani spoločnosti Facebook Inc. Okrem toho táto stránka NIE JE žiadnym spôsobom podporovaná spoločnosťou Facebook. Facebook je ochranná známka spoločnosti Facebook, Inc.</p>",
    
    "<p>© 2023 Tutti i diritti riservati.</p>": "<p>© 2023 Všetky práva vyhradené.</p>",
    "<p data-start=\"4857\" data-end=\"4876\">PRIVACY | CONTATTI</p>": "<p data-start=\"4857\" data-end=\"4876\">OCHRANA SÚKROMIA | KONTAKT</p>"
}

def translate_recursive(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, str):
                if value in REPLACEMENTS:
                    data[key] = REPLACEMENTS[value]
                else:
                    # Check if the string matches loosely (e.g. ignoring whitespace differences if exact match fails)
                    # For now, strict match is safest.
                    pass
            elif isinstance(value, (dict, list)):
                translate_recursive(value)
    elif isinstance(data, list):
        for item in data:
            translate_recursive(item)

def main():
    try:
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        translate_recursive(data)
        
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False) # Elementor JSONs can be minified usually, but let's see. The input was minified.
            
        print(f"Successfully translated {INPUT_FILE} to {OUTPUT_FILE}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
