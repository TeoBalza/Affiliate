import json
import re

# File paths
INPUT_FILE = '/Users/matteo/Documents/GitHub/forno/lucidatrice/lucidatrice-it.json'
OUTPUT_FILE = '/Users/matteo/Documents/GitHub/forno/lucidatrice/lucidatrice-ro.json'

# Translation Map (Italian -> Romanian)
TRANSLATIONS = {
    "SVENDITA TOTALE": "LICHIDARE TOTALĂ",
    "La Potente Lucidatrice Roto-Orbitale e Angolare con Motore Brushless a Doppia Azione che Lucida, Incera e Rimuove Graffi, Macchie e Aloni da ogni tipo di superficie in sicurezza e senza fatica": "Puternica mașină de șlefuit roto-orbitală și unghiulară, cu motor fără perii cu acțiune dublă, care lustruiește, ceruiește și îndepărtează zgârieturile, petele și urmele de pe orice tip de suprafață, în siguranță și fără efort",
    "Lavora perfettamente Auto, Moto, Barche, Mobili, Piastrelle, Marmo, Legno e tanto altro grazie al Potente Motore Brushless da 3000 Watt con 6 Livelli di Velocità e Doppia Batteria da 18V  ": "Funcționează perfect pe mașini, motociclete, bărci, mobilă, gresie, marmură, lemn și multe altele, datorită motorului puternic fără perii de 3000 wați, cu 6 trepte de viteză și baterie dublă de 18V  ",
    
    "OFFERTA TUTTO INCLUSO": "OFERTĂ ALL INCLUSIVE",
    "GARANZIA RICAMBI 4 ANNI": "GARANȚIE PIESE DE SCHIMB 4 ANI",
    "Compila il modulo per ordinare": "Completează formularul pentru a comanda",
    "Lavori professionali e fai da te con la Potente Lucidatrice Roto-orbitale 180mm": "Lucrări profesionale și DIY cu puternica mașină de șlefuit roto-orbitală de 180mm",
    "Scheda Tecnica Lucidatrice Rotorbitale:": "Fișă tehnică mașină de șlefuit roto-orbitală:",
    "Cosa riceverai a casa?": "Ce vei primi acasă?",
    
    # Complex strings (HTML Editors)
    "<p>Risultati straordinari grazie al potente Motore Brushless da 19.000 Giri/Min e 3000W.&nbsp;</p>\n<p>Con 2 Filtri D'aria e 6 diverse regolazioni di velocità&nbsp;il motore non si surriscalda mai anche dopo molte ore di utilizzo</p>\n<p>Con un peso di soli 800g è realizzata interamente in Acciaio Inox e Alluminio, con impugnatura ergonomica, è leggera, facile da maneggiare e non affatica mani e braccia</p>": 
    "<p>Rezultate extraordinare datorită motorului puternic fără perii de 19.000 RPM și 3000W.&nbsp;</p>\n<p>Cu 2 filtre de aer și 6 setări diferite de viteză&nbsp;motorul nu se supraîncălzește niciodată, chiar și după multe ore de utilizare</p>\n<p>Cu o greutate de doar 800g, este realizată integral din oțel inoxidabil și aluminiu, cu mâner ergonomic, fiind ușoară, facil de manevrat și nu obosește mâinile și brațele</p>",
    
    "<p>La Potente Lucidatrice Rotorbitale è perfetta per lucidare e rimettere a nuovo Auto, Moto o Barche</p><p>Inoltre, grazie all'orbita fino a 180 mm e ai 4 Dischi inclusi rimuove graffi e macchie da Legno, Marmo, Piastrelle, Pavimenti e tanto altro</p>":
    "<p>Puternica mașină de șlefuit roto-orbitală este perfectă pentru a lustrui și recondiționa mașini, motociclete sau bărci</p><p>În plus, datorită orbitei de până la 180 mm și a celor 4 discuri incluse, îndepărtează zgârieturile și petele de pe lemn, marmură, gresie, podele și multe altele</p>",
    
    "<p>La Lucidatrice è super silenziosa e 100% Sicura da utilizzare</p><p>Infatti è dotata di un guscio protettivo che ti ripara da schegge, polvere e detriti</p><p>Grazie alla doppia impugnatura, non affatica braccia e schiena durante l'utilizzo</p>":
    "<p>Mașina de șlefuit este super silențioasă și 100% sigură de utilizat</p><p>De fapt, este dotată cu o carcasă de protecție care te apără de așchii, praf și resturi</p><p>Datorită mânerului dublu, nu obosește brațele și spatele în timpul utilizării</p>",
    
    "<p>Le due batteria da 18V  garantiscono ben 6 ore di lavoro continuo alla massima potenza</p><p>Inoltre, la nuova lucidatrice riconosce il tipo di lavoro che stai eseguendo e calibra in maniera automatica velocità e potenza in modo da garantirti le massime prestazioni</p>":
    "<p>Cele două baterii de 18V garantează 6 ore de lucru continuu la putere maximă</p><p>În plus, noua mașină de șlefuit recunoaște tipul de lucrare pe care îl execuți și calibrează automat viteza și puterea pentru a-ți garanta performanțe maxime</p>",
    
    "<p style=\"margin-bottom: 0.9rem; caret-color: #333333; color: #333333; font-size: 12px; text-align: center; text-size-adjust: auto;\"><span style=\"font-size: 10px;\">This site is not a part of the Facebook website or Facebook Inc. Additionally, this site is NOT endorsed by Facebook in any way. Facebook is a trademark of Facebook, Inc</span></p>":
    "<p style=\"margin-bottom: 0.9rem; caret-color: #333333; color: #333333; font-size: 12px; text-align: center; text-size-adjust: auto;\"><span style=\"font-size: 10px;\">Acest site nu face parte din site-ul Facebook sau Facebook Inc. În plus, acest site NU este aprobat de Facebook în niciun fel. Facebook este o marcă înregistrată a Facebook, Inc</span></p>",
    
    "<p>\u00a9 2023 Tutti i diritti riservati.</p>":
    "<p>\u00a9 2023 Toate drepturile rezervate.</p>",
    
    "<p>PRIVACY<span style=\"color: var( --e-global-color-text ); font-weight: var( --e-global-typography-text-font-weight );\"> </span> CONTATTI</p>":
    "<p>CONFIDENȚIALITATE<span style=\"color: var( --e-global-color-text ); font-weight: var( --e-global-typography-text-font-weight );\"> </span> CONTACT</p>",
    
    # Prices updated: 339 LEI discount, 680 LEI full
    # Original: 79€ / 395€ (assuming original text, although prompt says 'Scontato è LEI 339, prezzo intero LEI 680')
    # The source file 'lucidatrice-it.json' likely contains "79€" and "395€" strings from previous context.
    
    "Lucidatrice Roto-Orbitale<br>+ 1 Disco per Smerigliatura<br>+ 1 Disco per Lucidatura<br>+ 1 Disco per Inceratura<br>+ 1 Disco Graffi e Macchie<br>+ 1 Disco Universale<br> + 2 Batterie 18V<br>+ Caricabatterie<br>+ Valigetta e Kit Accessori<br>A SOLI 79\u20ac":
    "Mașină de șlefuit roto-orbitală<br>+ 1 Disc de șlefuire<br>+ 1 Disc de lustruire<br>+ 1 Disc de ceruire<br>+ 1 Disc pentru zgârieturi și pete<br>+ 1 Disc universal<br> + 2 Baterii 18V<br>+ Încărcător<br>+ Valiză și kit accesorii<br>LA DOAR 339 LEI",
    
    "Lucidatrice Rotorbitale<br>+ 1 Disco per Lucidatura<br>+ 1 Disco per Inceratura<br>+ 1 Disco graffi e macchie<br>+ 1 Disco Universale<br> + 2 Batterie 18V<br>+ Caricabatterie<br>+ Valigetta e Accessori<br>+ Ricambi per 4 Anni<br>A SOLI 79\u20ac":
    "Mașină de șlefuit roto-orbitală<br>+ 1 Disc de lustruire<br>+ 1 Disc de ceruire<br>+ 1 Disc pentru zgârieturi și pete<br>+ 1 Disc universal<br> + 2 Baterii 18V<br>+ Încărcător<br>+ Valiză și accesorii<br>+ Piese de sch. 4 ani<br>LA DOAR 339 LEI",
    
    "OFFERTA TUTTO INCLUSO a soli \u20ac 79": "OFERTĂ ALL INCLUSIVE la doar 339 LEI",
    
    "invece di \u20ac395": "în loc de 680 LEI",
    
    # Icon List Items
    "Orbita fino a 180mm": "Orbită până la 180 mm",
    "Perfetta per: Lucidare, Incerare, Rimuovere Graffi, Segni e Macchie, Riportare a nuovo superfici": "Perfectă pentru: Lustruire, ceruire, îndepărtarea zgârieturilor, urmelor și petelor, recondiționarea suprafețelor",
    "Motore Brushless 1900W": "Motor fără perii 1900W",
    "19.000 Giri/Min": "19.000 RPM",
    "Doppia Batteria 18V": "Baterie dublă 18V",
    "Per Auto, Moto, Barche, Legno, Piastrelle, Pavimenti e tanto altro": "Pentru mașini, motociclete, bărci, lemn, gresie, podele și multe altele",
    "4 Dischi Intercambiabili ": "4 discuri interschimbabile ",
    "6 Ore di lavoro alla massima potenza": "6 ore de lucru la putere maximă",
    "Impugnatura ergonomica anti fatica": "Mâner ergonomic anti-oboseală",
    "Pesa solo 800 grammi": "Cântărește doar 800 de grame",
    "100% Sicura e Affidabile": "100% Sigură și fiabilă",
    "Qualit\u00e0 Premium": "Calitate Premium",
    "Garanzia e Ricambi per 4 Anni ": "Garanție și piese de schimb 4 ani ",
    "Reso Gratuito 60 giorni": "Retur gratuit 60 de zile",
    "Pagamento alla consegna  e Spedizione Rapida": "Plată la livrare și expediere rapidă",
    
    "Lucidatrice Rotorbitale": "Mașină de șlefuit roto-orbitală",
    "1 Disco per Lucidatura": "1 Disc de lustruire",
    "1 Disco per Inceratura": "1 Disc de ceruire",
    "1 Disco per Rimuovere Macchie e Graffi": "1 Disc pentru pete și zgârieturi",
    "1 Disco Universale": "1 Disc universal",
    "Due batterie da 18V": "Două baterii de 18V",
    "Caricabatterie": "Încărcător",
    "Kit cambio dischi": "Kit schimbare discuri",
    "Guanti da Lavoro": "Mănuși de lucru",
    "Valigetta Professionale": "Valiză profesională",
    "Garanzia Ricambi 4 Anni": "Garanție piese de schimb 4 ani",
    "Consegna Rapida Assicurata": "Livrare rapidă asigurată", # Duplicate key check? No, value matches below
    "Reso Gratuito 60 giorni": "Retur gratuit 60 de zile"
}


def translate_elements(elements):
    for element in elements:
        if "settings" in element:
            settings = element["settings"]
            
            # Check Title
            if "title" in settings:
                txt = settings["title"]
                if txt in TRANSLATIONS:
                    settings["title"] = TRANSLATIONS[txt]
                elif txt.strip() in TRANSLATIONS:
                    # Handle "18V  " trailing space issue generically if strict match fails
                    translated = TRANSLATIONS[txt.strip()]
                    # Preserve trailing space if original had it?
                    # The original had "18V  ", target "18V  "
                    # But simpler to just replace strict.
                    settings["title"] = translated

            # Check Editor
            if "editor" in settings:
                txt = settings["editor"]
                if txt in TRANSLATIONS:
                    settings["editor"] = TRANSLATIONS[txt]

            # Check Inner Text (Progress Bar or Button)
            if "inner_text" in settings:
                txt = settings["inner_text"]
                if txt in TRANSLATIONS:
                    settings["inner_text"] = TRANSLATIONS[txt]
            
            # Button text? Often 'text' key in some elements
            if "text" in settings: 
                txt = settings["text"]
                if txt in TRANSLATIONS:
                    settings["text"] = TRANSLATIONS[txt]

            # Check Icon List
            if "icon_list" in settings:
                for item in settings["icon_list"]:
                    if "text" in item:
                        txt = item["text"]
                        if txt in TRANSLATIONS:
                            item["text"] = TRANSLATIONS[txt]
                        elif txt.strip() in TRANSLATIONS:
                             item["text"] = TRANSLATIONS[txt.strip()]
        
        # Recursion
        if "elements" in element:
            translate_elements(element["elements"])

def main():
    print(f"Reading {INPUT_FILE}...")
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Walk the content
    if "content" in data:
        translate_elements(data["content"])
    
    # Save
    print(f"Saving to {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, separators=(',', ':'))

    print("Done.")

if __name__ == "__main__":
    main()
