import json
import re

# File paths
INPUT_FILE = '/Users/matteo/Documents/GitHub/forno/lucidatrice/lucidatrice-it.json'
OUTPUT_FILE = '/Users/matteo/Documents/GitHub/forno/lucidatrice/lucidatrice-bg.json'

# Translation Map (Italian -> Bulgarian)
# Format: Exact Italian String -> Exact Bulgarian String
TRANSLATIONS = {
    "SVENDITA TOTALE": "ПЪЛНА РАЗПРОДАЖБА",
    "La Potente Lucidatrice Roto-Orbitale e Angolare con Motore Brushless a Doppia Azione che Lucida, Incera e Rimuove Graffi, Macchie e Aloni da ogni tipo di superficie in sicurezza e senza fatica": "Мощната ротационно-орбитална и ъглова полираща машина с безчетков мотор с двойно действие, която полира, нанася вакса и премахва драскотини, петна и ореоли от всякакъв вид повърхности безопасно и без умора",
    "Lavora perfettamente Auto, Moto, Barche, Mobili, Piastrelle, Marmo, Legno e tanto altro grazie al Potente Motore Brushless da 3000 Watt con 6 Livelli di Velocità e Doppia Batteria da 18V  ": "Работи перфектно върху автомобили, мотоциклети, лодки, мебели, плочки, мрамор, дърво и много други благодарение на мощния 3000-ватов безчетков мотор с 6 нива на скорост и двойна 18V батерия  ",
    # Note: Added trailing spaces to match strict equality if needed, though will strip in logic usually.
    # The JSON string has trailing space in the file view above: "18V  "
    
    "OFFERTA TUTTO INCLUSO": "ОФЕРТА ВСИЧКО ВКЛЮЧЕНО",
    "GARANZIA RICAMBI 4 ANNI": "ГАРАНЦИЯ ЗА ЧАСТИ 4 ГОДИНИ",
    "Compila il modulo per ordinare": "Попълнете формуляра за поръчка",
    "Lavori professionali e fai da te con la Potente Lucidatrice Roto-orbitale 180mm": "Професионална и 'направи си сам' работа с мощната ротационно-орбитална полираща машина 180мм",
    "Scheda Tecnica Lucidatrice Rotorbitale:": "Технически характеристики на ротационно-орбиталната полираща машина:",
    "Cosa riceverai a casa?": "Какво ще получите вкъщи?",
    
    # Complex strings (HTML Editors)
    "<p>Risultati straordinari grazie al potente Motore Brushless da 19.000 Giri/Min e 3000W.&nbsp;</p>\n<p>Con 2 Filtri D'aria e 6 diverse regolazioni di velocità&nbsp;il motore non si surriscalda mai anche dopo molte ore di utilizzo</p>\n<p>Con un peso di soli 800g è realizzata interamente in Acciaio Inox e Alluminio, con impugnatura ergonomica, è leggera, facile da maneggiare e non affatica mani e braccia</p>": 
    "<p>Изключителни резултати благодарение на мощния безчетков мотор с 19 000 об./мин и 3000 W.&nbsp;</p>\n<p>С 2 въздушни филтъра и 6 различни настройки на скоростта&nbsp;моторът никога не прегрява дори след много часове употреба</p>\n<p>С тегло само 800 г, изработена изцяло от неръждаема стомана и алуминий, с ергономична дръжка, лека, лесна за работа и не уморява ръцете и раменете</p>",
    
    "<p>La Potente Lucidatrice Rotorbitale è perfetta per lucidare e rimettere a nuovo Auto, Moto o Barche</p><p>Inoltre, grazie all'orbita fino a 180 mm e ai 4 Dischi inclusi rimuove graffi e macchie da Legno, Marmo, Piastrelle, Pavimenti e tanto altro</p>":
    "<p>Мощната ротационно-орбитална полираща машина е перфектна за полиране и обновяване на автомобили, мотоциклети или лодки</p><p>Освен това, благодарение на орбитата до 180 мм и включените 4 диска, премахва драскотини и петна от дърво, мрамор, плочки, подове и много други</p>",
    
    "<p>La Lucidatrice è super silenziosa e 100% Sicura da utilizzare</p><p>Infatti è dotata di un guscio protettivo che ti ripara da schegge, polvere e detriti</p><p>Grazie alla doppia impugnatura, non affatica braccia e schiena durante l'utilizzo</p>":
    "<p>Полиращата машина е супер тиха и 100% безопасна за използване</p><p>Всъщност тя е оборудвана със защитен корпус, който ви предпазва от трески, прах и отломки</p><p>Благодарение на двойната дръжка не уморява ръцете и гърба по време на употреба</p>",
    
    "<p>Le due batteria da 18V  garantiscono ben 6 ore di lavoro continuo alla massima potenza</p><p>Inoltre, la nuova lucidatrice riconosce il tipo di lavoro che stai eseguendo e calibra in maniera automatica velocità e potenza in modo da garantirti le massime prestazioni</p>":
    "<p>Двете батерии 18V  гарантират цели 6 часа непрекъсната работа на максимална мощност</p><p>Освен това новата полираща машина разпознава вида работа, която извършвате, и автоматично калибрира скоростта и мощността, за да гарантира върхова производителност</p>",
    
    "<p style=\"margin-bottom: 0.9rem; caret-color: #333333; color: #333333; font-size: 12px; text-align: center; text-size-adjust: auto;\"><span style=\"font-size: 10px;\">This site is not a part of the Facebook website or Facebook Inc. Additionally, this site is NOT endorsed by Facebook in any way. Facebook is a trademark of Facebook, Inc</span></p>":
    "<p style=\"margin-bottom: 0.9rem; caret-color: #333333; color: #333333; font-size: 12px; text-align: center; text-size-adjust: auto;\"><span style=\"font-size: 10px;\">Този сайт не е част от уебсайта на Facebook или Facebook Inc. Освен това, този сайт НЕ е одобрен от Facebook по никакъв начин. Facebook е търговска марка на Facebook, Inc</span></p>",
    
    "<p>\u00a9 2023 Tutti i diritti riservati.</p>":
    "<p>\u00a9 2023 Всички права запазени.</p>",
    
    "<p>PRIVACY<span style=\"color: var( --e-global-color-text ); font-weight: var( --e-global-typography-text-font-weight );\"> </span> CONTATTI</p>":
    "<p>ПОВЕРИТЕЛНОСТ<span style=\"color: var( --e-global-color-text ); font-weight: var( --e-global-typography-text-font-weight );\"> </span> КОНТАКТИ</p>",
    
    # Headings with internal prices or specific formatting
    "Lucidatrice Roto-Orbitale<br>+ 1 Disco per Smerigliatura<br>+ 1 Disco per Lucidatura<br>+ 1 Disco per Inceratura<br>+ 1 Disco Graffi e Macchie<br>+ 1 Disco Universale<br> + 2 Batterie 18V<br>+ Caricabatterie<br>+ Valigetta e Kit Accessori<br>A SOLI 79\u20ac":
    "Ротационно-орбитална полираща машина<br>+ 1 Диск за шлайфане<br>+ 1 Диск за полиране<br>+ 1 Диск за нанасяне на вакса<br>+ 1 Диск за драскотини и петна<br>+ 1 Универсален диск<br> + 2 Батерии 18V<br>+ Зарядно устройство<br>+ Куфар и комплект аксесоари<br>САМО ЗА 134 лв",
    
    "Lucidatrice Rotorbitale<br>+ 1 Disco per Lucidatura<br>+ 1 Disco per Inceratura<br>+ 1 Disco graffi e macchie<br>+ 1 Disco Universale<br> + 2 Batterie 18V<br>+ Caricabatterie<br>+ Valigetta e Accessori<br>+ Ricambi per 4 Anni<br>A SOLI 79\u20ac":
    "Ротационно-орбитална полираща машина<br>+ 1 Диск за полиране<br>+ 1 Диск за нанасяне на вакса<br>+ 1 Диск за драскотини и петна<br>+ 1 Универсален диск<br> + 2 Батерии 18V<br>+ Зарядно устройство<br>+ Куфар и аксесоари<br>+ Резервни части за 4 години<br>САМО ЗА 134 лв",
    
    "OFFERTA TUTTO INCLUSO a soli \u20ac 79": "ОФЕРТА ВСИЧКО ВКЛЮЧЕНО само за 134 лв",
    
    "invece di \u20ac395": "вместо 270 лв",
    
    # Icon List Items
    "Orbita fino a 180mm": "Орбита до 180 мм",
    "Perfetta per: Lucidare, Incerare, Rimuovere Graffi, Segni e Macchie, Riportare a nuovo superfici": "Перфектна за: Полиране, ваксиране, премахване на драскотини, следи и петна, възстановяване на повърхности",
    "Motore Brushless 1900W": "Безчетков мотор 1900W",
    "19.000 Giri/Min": "19 000 об./мин",
    "Doppia Batteria 18V": "Двойна батерия 18V",
    "Per Auto, Moto, Barche, Legno, Piastrelle, Pavimenti e tanto altro": "За автомобили, мотоциклети, лодки, дърво, плочки, подове и много други",
    "4 Dischi Intercambiabili ": "4 сменяеми диска ",
    "6 Ore di lavoro alla massima potenza": "6 часа работа на максимална мощност",
    "Impugnatura ergonomica anti fatica": "Ергономична дръжка против умора",
    "Pesa solo 800 grammi": "Тежи само 800 грама",
    "100% Sicura e Affidabile": "100% Безопасна и надеждна",
    "Qualit\u00e0 Premium": "Премиум качество",
    "Garanzia e Ricambi per 4 Anni ": "Гаранция и резервни части за 4 години ",
    "Reso Gratuito 60 giorni": "Безплатно връщане 60 дни",
    "Pagamento alla consegna  e Spedizione Rapida": "Плащане при доставка и бърза доставка",
    
    "Lucidatrice Rotorbitale": "Ротационно-орбитална полираща машина",
    "1 Disco per Lucidatura": "1 Диск за полиране",
    "1 Disco per Inceratura": "1 Диск за нанасяне на вакса",
    "1 Disco per Rimuovere Macchie e Graffi": "1 Диск за премахване на петна и драскотини",
    "1 Disco Universale": "1 Универсален диск",
    "Due batterie da 18V": "Две батерии по 18V",
    "Caricabatterie": "Зарядно устройство",
    "Kit cambio dischi": "Комплект за смяна на дискове",
    "Guanti da Lavoro": "Работни ръкавици",
    "Valigetta Professionale": "Професионален куфар",
    "Garanzia Ricambi 4 Anni": "Гаранция за части 4 години",
    "Consegna Rapida Assicurata": "Осигурена бърза доставка",
    "Reso Gratuito 60 giorni": "Безплатно връщане 60 дни"
}

# Pre-computation to handle potential JSON escaping issues (spaces, newlines)
# We will use keys exactly as they appear in the Python string definition, 
# relying on Python's JSON library to handle escaping when we load the file.

def translate_elements(elements):
    for element in elements:
        if "settings" in element:
            settings = element["settings"]
            
            # Check Title
            if "title" in settings:
                txt = settings["title"]
                if txt in TRANSLATIONS:
                    settings["title"] = TRANSLATIONS[txt]
                else:
                    # Fallback for approximate matches logic if strict constraint allows
                    # But for now strict mapping based on file inspection.
                    # Handle "18V  " trailing space issue
                    if txt.strip() in TRANSLATIONS:
                         # This might destroy formatting if we replace with stripped, so be careful.
                         pass
                    
                    # Manual fixes if exact match fails?
                    # "Lavora perfettamente ... da 18V  " -> Has trailing spaces in JSON
                    if txt == "Lavora perfettamente Auto, Moto, Barche, Mobili, Piastrelle, Marmo, Legno e tanto altro grazie al Potente Motore Brushless da 3000 Watt con 6 Livelli di Velocità e Doppia Batteria da 18V  ":
                        settings["title"] = TRANSLATIONS[txt]

            # Check Editor
            if "editor" in settings:
                txt = settings["editor"]
                # Attempt direct match
                if txt in TRANSLATIONS:
                    settings["editor"] = TRANSLATIONS[txt]

            # Check Inner Text (Progress Bar)
            if "inner_text" in settings:
                txt = settings["inner_text"]
                if txt in TRANSLATIONS:
                    settings["inner_text"] = TRANSLATIONS[txt]

            # Check Icon List
            if "icon_list" in settings:
                for item in settings["icon_list"]:
                    if "text" in item:
                        txt = item["text"]
                        if txt in TRANSLATIONS:
                            item["text"] = TRANSLATIONS[txt]
                        elif txt.strip() in TRANSLATIONS:
                             item["text"] = TRANSLATIONS[txt.strip()] # Careful with this
        
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
