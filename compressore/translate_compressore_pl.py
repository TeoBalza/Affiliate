import json

# Translation Map (Hungarian -> Polish)
translations = {
    "1 db 5 méteres cső": "1 wąż 5-metrowy",
    "1 pár újrahasználható kesztyű": "1 para rękawic wielokrotnego użytku",
    "12 literes tartály: Optimális kapacitás a jó munkavégzési autonómia érdekében, csökkenti a töltési szüneteket és növeli a termelékenységet": "12-litrowy zbiornik: Optymalna pojemność dla dobrej autonomii pracy, skraca przerwy na napełnianie i zwiększa wydajność",
    "1LE-s motor: Erős és megbízható, akár 8 Bar és 115 l/perc teljesítmény felfújáshoz, kifújáshoz és festéshez": "Silnik 1 KM: Mocny i niezawodny, do 8 barów i 115 l/min wydajności do pompowania, przedmuchiwania i malowania",
    "2 db akkumulátor mellékelve": "W zestawie 2 akumulatory",
    "2 év műszaki támogatás": "2 lata wsparcia technicznego",
    "62 dB-es halk működés: Ultra csendes működés, tökéletes beltéri vagy közös használatra, anélkül hogy zavarná a környezetet": "Cicha praca 62 dB: Bardzo cicha praca, idealna do użytku wewnątrz lub we wspólnych pomieszczeniach bez zakłócania otoczenia",
    "74663 Ft helyett": "Zamiast 450 zł", 
    "<h3><!--StartFragment --></h3><h3><!--StartFragment --></h3><h3><span style=\"text-decoration: underline;\">Halk és könnyen szállítható</span></h3><p><strong>Mindössze 62 dB zajkibocsátással ideális beltéri használatra anélkül, hogy zavarna. A kompakt és olajmentes kialakítás praktikus mozgatást és használatot tesz lehetővé bárhol: otthon, garázsban vagy műhelyben</strong><br /><!--EndFragment --></p><p><!--StartFragment --></p>": "<h3><!--StartFragment --></h3><h3><!--StartFragment --></h3><h3><span style=\"text-decoration: underline;\">Cicha i łatwa w transporcie</span></h3><p><strong>Z emisją hałasu wynoszącą zaledwie 62 dB jest idealna do użytku wewnątrz bez zakłóceń. Kompaktowa i bezolejowa konstrukcja umożliwia praktyczne przenoszenie i użytkowanie w dowolnym miejscu: w domu, garażu lub warsztacie</strong><br /><!--EndFragment --></p><p><!--StartFragment --></p>",
    "<h4 class=\"a-size-large a-spacing-none\"><!--StartFragment --></h4><h3><!--StartFragment --></h3><h3><span style=\"text-decoration: underline;\">Kompakt teljesítmény 1LE</span></h3><p><strong>Egy lóerős elektromos motorral felszerelve ez a kompresszor eléri a 8 Bar maximális nyomást és 115 liter/perc légáramot. Ideális teljesítmény kerekek felfújásához, por kifújásához, szögeléshez vagy precíz festéshez, akár otthoni vagy kézműves környezetben is</strong><br /><!--EndFragment --></p><p><!--EndFragment --></p><p><!--EndFragment --></p>": "<h4 class=\"a-size-large a-spacing-none\"><!--StartFragment --></h4><h3><!--StartFragment --></h3><h3><span style=\"text-decoration: underline;\">Kompaktowa moc 1 KM</span></h3><p><strong>Wyposażona w silnik elektryczny o mocy jednego konia mechanicznego, sprężarka ta osiąga maksymalne ciśnienie 8 barów i przepływ powietrza 115 litrów/min. Idealna wydajność do pompowania kół, wydmuchiwania kurzu, wbijania gwoździ lub precyzyjnego malowania, nawet w warunkach domowych lub rzemieślniczych</strong><br /><!--EndFragment --></p><p><!--EndFragment --></p><p><!--EndFragment --></p>",
    "<h4 class=\"a-spacing-mini\"><!--StartFragment --></h4><h3><!--StartFragment --></h3><h3><span style=\"text-decoration: underline;\">ECO technológia olaj nélkül</span></h3><p><strong>Az olajmentes rendszer kiküszöböli a karbantartás szükségességét és tiszta működést biztosít. Az ECO technológia alacsony fordulatszámmal csökkenti az energiafogyasztást és meghosszabbítja a kompresszor élettartamát, fenntartható és megbízható megoldást kínálva</strong><br /><!--EndFragment --></p><p class=\"a-spacing-mini\"><!--StartFragment --></p>": "<h4 class=\"a-spacing-mini\"><!--StartFragment --></h4><h3><!--StartFragment --></h3><h3><span style=\"text-decoration: underline;\">Technologia ECO bez oleju</span></h3><p><strong>System bezolejowy eliminuje konieczność konserwacji i zapewnia czystą pracę. Technologia ECO z niskimi obrotami zmniejsza zużycie energii i wydłuża żywotność sprężarki, oferując zrównoważone i niezawodne rozwiązanie</strong><br /><!--EndFragment --></p><p class=\"a-spacing-mini\"><!--StartFragment --></p>",
    "<h4 class=\"a-spacing-mini\"><!--StartFragment --></h4><h3><!--StartFragment --></h3><h3><span style=\"text-decoration: underline;\">12 literes alumínium tartály olajmentes szivattyúval és leeresztő szeleppel</span></h3><p><strong>Könnyű és strapabíró, a 12 literes tartály jó autonómiát biztosít szakaszos munkákhoz. Az olajmentes szivattyú karbantartásmentes működést garantál, míg a leeresztő szelep megkönnyíti a kondenzvíz eltávolítását, javítva a rendszer hatékonyságát és tisztaságát</strong><br /><!--EndFragment --></p><p><!--StartFragment --></p>": "<h4 class=\"a-spacing-mini\"><!--StartFragment --></h4><h3><!--StartFragment --></h3><h3><span style=\"text-decoration: underline;\">12-litrowy zbiornik aluminiowy z pompą bezolejową i zaworem spustowym</span></h3><p><strong>Lekki i wytrzymały, 12-litrowy zbiornik zapewnia dobrą autonomię przy pracach przerywanych. Pompa bezolejowa gwarantuje bezobsługową pracę, a zawór spustowy ułatwia usuwanie kondensatu, poprawiając wydajność i czystość systemu</strong><br /><!--EndFragment --></p><p><!--StartFragment --></p>",
    "<p data-start=\"4857\" data-end=\"4876\">PRIVACY | CONTATTI</p>": "<p data-start=\"4857\" data-end=\"4876\">PRYWATNOŚĆ | KONTAKT</p>",
    "<p style=\"margin-bottom: 0.9rem; caret-color: #333333; color: #333333; font-size: 12px; text-align: center; text-size-adjust: auto;\">This site is not a part of the Facebook website or Facebook Inc. Additionally, this site is NOT endorsed by Facebook in any way. Facebook is a trademark of Facebook, Inc</p>": "<p style=\"margin-bottom: 0.9rem; caret-color: #333333; color: #333333; font-size: 12px; text-align: center; text-size-adjust: auto;\">Ta strona nie jest częścią serwisu Facebook ani Facebook Inc. Ponadto ta strona NIE jest w żaden sposób sponsorowana przez Facebook. Facebook jest znakiem towarowym Facebook, Inc.</p>",
    "<p>© 2023 Tutti i diritti riservati.</p>": "<p>© 2023 Wszelkie prawa zastrzeżone.</p>",
    "<u>AZ ÚJ, KIVÉTELES AirForce One 2025</u>": "<u>NOWY I WYJĄTKOWY AirForce One 2025</u>",
    "A Professzionális Légkompresszor Manométerrel, amely Felfúj, Szív, Fúj és Permetez 115 Liter/perc sebességgel gyorsan és könnyedén, tökéletes kerekekhez, festéshez, otthoni tisztításhoz, nyomásos fúráshoz és kézműves munkákhoz": "Profesjonalna sprężarka powietrza z manometrem, która pompuje, zasysa, dmucha i natryskuje z prędkością 115 litrów/min szybko i łatwo, idealna do kół, malowania, sprzątania w domu, wiercenia ciśnieniowego i prac rzemieślniczych",
    "AirForce One<br>+ Univerzális felfújófej készlet<br>+ 2 db akkumulátor mellékelve<br>+ 1 db 5 méteres cső<br>+ Fúvófej<br>+ Szerszámtartó táska<br>+ 1 pár újrahasználható kesztyű<br>CSAK 19999 Ft": "AirForce One<br>+ Zestaw uniwersalnych końcówek do pompowania<br>+ W zestawie 2 akumulatory<br>+ 1 wąż 5-metrowy<br>+ Dysza do przedmuchiwania<br>+ Torba na narzędzia<br>+ 1 para rękawic wielokrotnego użytku<br>TYLKO 219 zł",
    "Alumínium anyag: Könnyű és korrózióálló szerkezet, ideális hosszan tartó használatra és könnyű szállításra anélkül, hogy a tartósság csorbulna": "Materiał aluminiowy: Lekka i odporna na korozję konstrukcja, idealna do długotrwałego użytkowania i łatwego transportu bez uszczerbku dla trwałości",
    "ECO alacsony fordulatszámmal és csökkentett fogyasztással: Fenntartható kompresszor, amely hosszú élettartamot biztosít és kíméli a környezetet": "ECO z niskimi obrotami i zmniejszonym zużyciem: Zrównoważona sprężarka, która zapewnia długą żywotność i chroni środowisko",
    "Elégedettségi vagy pénzvisszafizetési garancia": "Gwarancja satysfakcji lub zwrot pieniędzy",
    "Forradalmasítsd a munkád levegővel: erő, csend és kompakt sokoldalúság minden projekthez, a felfújástól a festésig": "Zrewolucjonizuj swoją pracę dzięki powietrzu: moc, cisza i kompaktowa wszechstronność dla każdego projektu, od pompowania po malowanie",
    "Fúvófej": "Dysza do przedmuchiwania",
    "Gyors házhoz szállítás": "Szybka dostawa do domu",
    "Gyors szállítás": "Szybka dostawa",
    "Ha ma rendeled meg, ajándékba kapod:<br><br>AirForce One<br>+ Univerzális felfújófej készlet<br>+ 2 db akkumulátor mellékelve<br>+ 1 db 5 méteres cső<br>+ Fúvófej<br>+ Szerszámtartó táska<br>+ 1 pár újrahasználható kesztyű<br>+Gyors és biztosított szállítás": "Jeśli zamówisz dzisiaj, otrzymasz w prezencie:<br><br>AirForce One<br>+ Zestaw uniwersalnych końcówek do pompowania<br>+ W zestawie 2 akumulatory<br>+ 1 wąż 5-metrowy<br>+ Dysza do przedmuchiwania<br>+ Torba na narzędzia<br>+ 1 para rękawic wielokrotnego użytku<br>+ Szybka i ubezpieczona dostawa",
    "Használatra kész: Könnyen elindítható, nem igényel bonyolult előkészületeket: csak csatlakoztatni kell és már kezdődhet is a munka, akár kezdők számára is": "Gotowy do użycia: Łatwy do uruchomienia, nie wymaga skomplikowanych przygotowań: wystarczy podłączyć i można zaczynać pracę, nawet dla początkujących",
    "Ideális barkácsoláshoz és kézművességhez: Tökéletes társ hobbistáknak és szakembereknek, akik kompakt és halk formátumban keresnek magas teljesítményt": "Idealny dla majsterkowiczów i rzemieślników: Doskonały towarzysz dla hobbystów i profesjonalistów, którzy szukają wysokiej wydajności w kompaktowym i cichym formacie",
    "Kompakt és halk, olajmentes és karbantartásmentes szivattyúval, leeresztő szeleppel, 8 BAR teljesítménnyel és 18V-os akkumulátorral a biztonságos, hatékony munkához bárhol": "Kompaktowa i cicha, z pompą bezolejową i bezobsługową, z zaworem spustowym, o mocy 8 BAR i akumulatorem 18V do bezpiecznej, wydajnej pracy w każdym miejscu",
    "Kompakt és hordozható kialakítás: Könnyen mozgatható és tárolható, ideális otthoni környezetbe, garázsba vagy kis műhelyekbe, ahol korlátozott a hely": "Kompaktowa i przenośna konstrukcja: Łatwa do przenoszenia i przechowywania, idealna do środowisk domowych, garaży lub małych warsztatów z ograniczoną przestrzenią",
    "Leeresztő szelep: Egyszerű és gyors kondenzvíz eltávolítást tesz lehetővé, javítva a kompresszor hatékonyságát és élettartamát": "Zawór spustowy: Umożliwia proste i szybkie usuwanie kondensatu, poprawiając wydajność i żywotność sprężarki",
    "Olajmentes szivattyú: Tiszta és karbantartásmentes működést biztosít, ideális olyan helyeken, ahol fontos a levegő tisztasága": "Pompa bezolejowa: Zapewnia czystą i bezobsługową pracę, idealna w miejscach, gdzie ważna jest czystość powietrza",
    "Olajmentes technológia és nincs szükség karbantartásra: A rendszer tiszta működést garantál, csökkenti a költségeket és megkönnyíti a használatot": "Technologia bezolejowa i brak konieczności konserwacji: System gwarantuje czystą pracę, obniża koszty i ułatwia użytkowanie",
    "Sokoldalú használat: Alkalmas autó-, motor- és kerékpárgumik, labdák, matracok felfújására, valamint por vagy szennyeződés kifújására felületekről és alkatrészekről": "Wszechstronne zastosowanie: Nadaje się do pompowania opon samochodowych, motocyklowych i rowerowych, piłek, materacy, a także do zdmuchiwania kurzu lub brudu z powierzchni i części",
    "Szerszámtartó táska": "Torba na narzędzia",
    "TELJES KÉSZLET AJÁNLAT": "OFERTA PEŁNEGO ZESTAWU",
    "Továbbá, ha ma rendeled meg, ajándékba kapsz egy ingyenes garancia-kiterjesztést a cserealkatrészekre, amely 2 évig érvényes.": "Ponadto, jeśli zamówisz dzisiaj, otrzymasz w prezencie bezpłatne przedłużenie gwarancji na części zamienne, ważne przez 2 lata.",
    "Töltse ki az alábbi űrlapot a professzionális AirForce One kompresszor megrendeléséhez garanciával és szállítással, mindössze 19999 Ft-ért": "Wypełnij poniższy formularz, aby zamówić profesjonalną sprężarkę AirForce One z gwarancją i dostawą za jedyne 219 zł",
    "Töltse ki az űrlapot a rendeléshez": "Wypełnij formularz, aby zamówić",
    "Univerzális felfújófej készlet": "Zestaw uniwersalnych końcówek do pompowania",
    "Ügyfélszolgálat és alkatrészek 2 ÉVIG benne vannak": "Obsługa klienta i części zamienne wliczone przez 2 LATA"
}

def translate_recursive(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, str):
                # If exact match
                if value in translations:
                    data[key] = translations[value]
                
            elif isinstance(value, (dict, list)):
                translate_recursive(value)
    elif isinstance(data, list):
        for item in data:
            translate_recursive(item)

def main():
    input_file = "compressore-hu.json"
    output_file = "compressore-pl.json"
    
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    translate_recursive(data)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False) 
        
    print(f"Created {output_file} successfully.")

if __name__ == "__main__":
    main()
