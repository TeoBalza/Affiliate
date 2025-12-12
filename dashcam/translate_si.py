
import json

input_path = '/Users/matteo/Documents/GitHub/forno/dashcam/dashcam-it.json'
output_path = '/Users/matteo/Documents/GitHub/forno/dashcam/dashcam-si.json'

with open(input_path, 'r') as f:
    data = json.load(f)

# Helper to find element by ID recursively
def find_element(container, target_id):
    if isinstance(container, dict):
        if container.get('id') == target_id:
            return container
        
        # Check elements
        if 'elements' in container:
            for el in container['elements']:
                res = find_element(el, target_id)
                if res: return res
        # Check content (root is a dict with content list)
        if 'content' in container:
            for el in container['content']:
                res = find_element(el, target_id)
                if res: return res
                
    elif isinstance(container, list):
        for item in container:
            res = find_element(item, target_id)
            if res: return res
    return None

# Replacements Map
replacements = {
    "1da1b9b2": {"key": "title", "val": "Inovativna avtomobilska kamera z GPS-om, ki snema in locira vaš avtomobil, da prepreči nesreče, kraje in zavarovalniške goljufije"},
    "137c051e": {"key": "title", "val": "Daljinski nadzor z obvestili na telefonu v primeru kraje ali sumljivih gibov.\\nSprednja in zadnja kamera 4K za 360-stopinjski pogled z neprekinjenim snemanjem tudi ponoči.\\nHitra namestitev brez mehanika"},
    "67a5dc66": {"key": "inner_text", "val": "ZADNJE KAMERE NA VOLJO"},
    "a0e4117": {"key": "title", "val": "1 SmartCam\u00ae<br>+ Memoria da 512 GB<br>+ Kit Installazione rapida<br>+ Reso Gratuito<br> A SOLI 59\u20ac"}, # Keep Title partially? Wait. I should translate the Item list inside the title.
    # Correction for "1 SmartCam..." part: "1 SmartCam®<br>+ 512 GB pomnilnika<br>+ Komplet za hitro namestitev<br>+ Brezplačno vračilo<br> SAMO 59 €"
    # Wait, the unicode \u20ac is €, \u00ae is ®. I should put them in the replacement string as python string escapes or literal chars if I use ensure_ascii=True.
    
    "4c2cbd67": {"key": "title", "val": "namesto 120 \u20ac"}, # Price 229 -> 120
    "2aec8124": {"key": "title", "val": "PODALJŠANA GARANCIJA 4 LETA"},
    "4ca914b8": {"key": "title", "val": "Izpolnite obrazec za naročilo"},
    "1abea8bd": {"key": "title", "val": "STALNO SPREMLJAJTE VSE, KAR SE DOGAJA ZNOTRAJ IN ZUNAJ VAŠEGA AVTOMOBILA"},
    "5d33d980": {"key": "editor", "val": "<p>SmartCam\u00ae snema video in zvok 24 ur na dan znotraj in zunaj vašega avtomobila.</p><p>Kamera SmartCam\u00ae zajame vse, kar se dogaja z vašim vozilom, tudi ko je ugasnjeno, in vam pošlje opozorila na telefon v primeru nevarnosti, udarcev, nesreč ali sumljivih gibov.</p><p>Zahvaljujoč priloženi 512 GB pomnilniški kartici kamera neprekinjeno snema do 30 dni ter vam zagotavlja video in avdio posnetke za zaščito pred zavarovalniškimi goljufijami in lažnimi odškodninskimi zahtevki.</p><p>Poleg tega lahko kadarkoli preprosto prenesete video in avdio posnetke na računalnik ali telefon in nadaljujete s snemanjem kot običajno.</p>"},
    "27668d02": {"key": "editor", "val": "<p>Dvojna vgrajena 360-stopinjska kamera pokriva celotno vozilo z možnostjo povečave za zaznavanje podrobnosti, registrskih tablic ali obrazov.</p><p>Tehnologija 4K z infrardečim objektivom zagotavlja jasen in natančen pogled tudi ponoči in na dolge razdalje.</p><p>Sprednjo in zadnjo kamero lahko upravljate neposredno s telefona z brezplačno aplikacijo.</p>"},
    "47a97986": {"key": "editor", "val": "<p>Revolucionarna kamera SmartCam\u00ae je edina na trgu z vgrajenim GPS-om, ki deluje brez interneta ali Bluetootha.</p><p>Zahvaljujoč vgrajenim satelitskim karticam se SmartCam\u00ae po priključitvi samodejno poveže s satelitskim omrežjem in 24 ur na dan locira vaš avtomobil in premike.</p><p>Poleg tega lahko lokacijo svojega avtomobila spremljate neposredno na telefonu zahvaljujoč vključeni brezplačni aplikaciji.</p>"},
    "403f0e53": {"key": "editor", "val": "<p>Namestitev kamere SmartCam\u00ae je res zelo preprosta in ne potrebujete pomoči ali obiska delavnice.</p><p>Dovolj je, da kamero pritrdite na vetrobransko steklo z izjemno močnimi priseski, priključite SmartCam\u00ae na vžigalnik za cigarete s priloženim 5-metrskim napajalnim kablom in snemanje se bo samodejno začelo.</p>"},
    "cc0f53b": {"key": "editor", "val": "<p>Ko je SmartCam\u00ae priključena na vžigalnik za cigarete, se samodejno polni, kar zagotavlja neprekinjeno snemanje pri ugasnjenem avtomobilu do 3 dni.</p><p>Funkcija varčevanja z baterijo preprečuje praznjenje akumulatorja vašega avtomobila.</p>"},
    "22d2c611": {"key": "title", "val": "1 SmartCam\u00ae<br>+ 512 GB pomnilnika<br>+ Komplet za hitro namestitev<br>+ Brezplačno vračilo<br> SAMO 59 \u20ac"},
    "72cd6e4d": {"key": "title", "val": "namesto 120 \u20ac"},
    "17e447e1": {"key": "title", "val": "Izpolnite obrazec za naročilo"},
    "68b217a8": {"key": "title", "val": "Če naročite danes, prejmete brezplačno: <br><br>5-metrski napajalni kabel<br>+ Nosilec s priseskom za vetrobransko steklo<br>+ 512 GB pomnilnika<br>+ Brezplačno vračilo"},
    "5e72a626": {"key": "title", "val": "Poleg tega ob današnjem naročilu prejmete tudi brezplačno podaljšanje garancije za 4 leta"},
    "607cb160": {"key": "title", "val": "IZPOLNITE SPODNJI OBRAZEC ZA NAROČILO SmartCam\u00ae ZA SAMO 59 \u20ac"},
    "6ccac8b0": {"key": "editor", "val": '<p style=\"margin-bottom: 0.9rem; caret-color: #333333; color: #333333; font-size: 12px; text-align: center; text-size-adjust: auto;\"><span style=\"font-size: 10px;\">To spletno mesto ni del spletnega mesta Facebook ali Facebook Inc. Poleg tega to spletno mesto NI na noben način povezano s Facebookom. Facebook je blagovna znamka družbe Facebook, Inc</span></p>'},
    "969aafd": {"key": "editor", "val": "<p>\u00a9 2023 Vse pravice pridržane.</p>"},
    "2eebc162": {"key": "editor", "val": "<p>ZASEBNOST<span style=\"color: var( --e-global-color-text ); font-weight: var( --e-global-typography-text-font-weight );\">\u00a0</span>\u00a0KONTAKTI</p>"}
}

# Icon Lists
icon_list_1_id = "4cac95be"
icon_list_1_items = [
    "PROTI NESREČAM IN ZAVAROVALNIŠKIM GOLJUFIJAM",
    "DVOJNA KAMERA 4K",
    "WIFI-GPS",
    "KARTICA 512 GB",
    "DOLGOTRAJNA BATERIJA",
    "HITRA NAMESTITEV",
    "Enostavna uporaba",
    "Zadovoljstvo zagotovljeno ali vračilo denarja"
]

icon_list_2_id = "725285d9"
icon_list_2_items = [
    "1 kamera SmartCam\u00ae",
    "5-metrski napajalni kabel",
    "512 GB pomnilniška kartica",
    "Komplet za hitro namestitev",
    "Brezplačno podaljšanje garancije za 4 leta",
    "Varno plačilo z gotovino ob povzetju",
    "Hitra dostava",
    "Zagotovljeno zadovoljstvo ali vračilo denarja"
]

# Update specific dictionary entry in replacement definition for a0e4117
replacements["a0e4117"] = {"key": "title", "val": "1 SmartCam\u00ae<br>+ 512 GB pomnilnika<br>+ Komplet za hitro namestitev<br>+ Brezplačno vračilo<br> SAMO 59 \u20ac"}

# Process standard fields
for id_val, rep in replacements.items():
    el = find_element(data, id_val)
    if el and 'settings' in el:
        if rep['key'] in el['settings']:
            el['settings'][rep['key']] = rep['val']

# Process Icon Lists
il1 = find_element(data, icon_list_1_id)
if il1 and 'settings' in il1 and 'icon_list' in il1['settings']:
    for i, item in enumerate(il1['settings']['icon_list']):
        if i < len(icon_list_1_items):
            item['text'] = icon_list_1_items[i]

il2 = find_element(data, icon_list_2_id)
if il2 and 'settings' in il2 and 'icon_list' in il2['settings']:
    for i, item in enumerate(il2['settings']['icon_list']):
        if i < len(icon_list_2_items):
            item['text'] = icon_list_2_items[i]

with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, separators=(',', ':')) # Default ensure_ascii=True will escape chars

print("Done")
