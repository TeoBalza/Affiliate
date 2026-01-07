import json
import re

# File paths
INPUT_FILE = '/Users/matteo/Documents/GitHub/forno/lucidatrice/lucidatrice-it.json'
OUTPUT_FILE = '/Users/matteo/Documents/GitHub/forno/lucidatrice/lucidatrice-es.json'

# Translation Map (Italian -> Spanish)
TRANSLATIONS = {
    "SVENDITA TOTALE": "LIQUIDACIÓN TOTAL",
    "La Potente Lucidatrice Roto-Orbitale e Angolare con Motore Brushless a Doppia Azione che Lucida, Incera e Rimuove Graffi, Macchie e Aloni da ogni tipo di superficie in sicurezza e senza fatica": "La Potente Pulidora Roto-Orbital y Angular con Motor Brushless de Doble Acción que Pule, Encera y Elimina Arañazos, Manchas y Halos de todo tipo de superficies de forma segura y sin esfuerzo",
    "Lavora perfettamente Auto, Moto, Barche, Mobili, Piastrelle, Marmo, Legno e tanto altro grazie al Potente Motore Brushless da 3000 Watt con 6 Livelli di Velocità e Doppia Batteria da 18V  ": "Funciona perfectamente en Coches, Motos, Barcos, Muebles, Azulejos, Mármol, Madera y mucho más gracias al Potente Motor Brushless de 3000 Vatios con 6 Niveles de Velocidad y Doble Batería de 18V  ",
    
    "OFFERTA TUTTO INCLUSO": "OFERTA TODO INCLUIDO",
    "GARANZIA RICAMBI 4 ANNI": "GARANTÍA DE REPUESTOS 4 AÑOS",
    "Compila il modulo per ordinare": "Rellena el formulario para pedir",
    "Lavori professionali e fai da te con la Potente Lucidatrice Roto-orbitale 180mm": "Trabajos profesionales y de bricolaje con la Potente Pulidora Roto-orbital 180mm",
    "Scheda Tecnica Lucidatrice Rotorbitale:": "Ficha Técnica Pulidora Roto-orbital:",
    "Cosa riceverai a casa?": "¿Qué recibirás en casa?",
    
    "<p>Risultati straordinari grazie al potente Motore Brushless da 19.000 Giri/Min e 3000W.&nbsp;</p>\n<p>Con 2 Filtri D'aria e 6 diverse regolazioni di velocità&nbsp;il motore non si surriscalda mai anche dopo molte ore di utilizzo</p>\n<p>Con un peso di soli 800g è realizzata interamente in Acciaio Inox e Alluminio, con impugnatura ergonomica, è leggera, facile da maneggiare e non affatica mani e braccia</p>": 
    "<p>Resultados extraordinarios gracias al potente Motor Brushless de 19.000 RPM y 3000W.&nbsp;</p>\n<p>Con 2 Filtros de Aire y 6 ajustes de velocidad diferentes&nbsp;el motor nunca se sobrecalienta incluso después de muchas horas de uso</p>\n<p>Con un peso de solo 800g está realizada completamente en Acero Inoxidable y Aluminio, con empuñadura ergonómica, es ligera, fácil de manejar y no cansa manos y brazos</p>",
    
    "<p>La Potente Lucidatrice Rotorbitale è perfetta per lucidare e rimettere a nuovo Auto, Moto o Barche</p><p>Inoltre, grazie all'orbita fino a 180 mm e ai 4 Discos inclusi rimuove graffi e macchie da Legno, Marmo, Piastrelle, Pavimenti e tanto altro</p>":
    "<p>La Potente Pulidora Roto-orbital es perfecta para pulir y renovar Coches, Motos o Barcos</p><p>Además, gracias a la órbita de hasta 180 mm y a los 4 Discos incluidos elimina arañazos y manchas de Madera, Mármol, Azulejos, Suelos y mucho más</p>",
    
    "<p>La Lucidatrice è super silenziosa e 100% Sicura da utilizzare</p><p>Infatti è dotata di un guscio protettivo che ti ripara da schegge, polvere e detriti</p><p>Grazie alla doppia impugnatura, non affatica braccia e schiena durante l'utilizzo</p>":
    "<p>La Pulidora es súper silenciosa y 100% Segura de usar</p><p>De hecho está dotada de una carcasa protectora que te protege de astillas, polvo y escombros</p><p>Gracias a la doble empuñadura, no cansa brazos y espalda durante el uso</p>",
    
    "<p>Le due batteria da 18V  garantiscono ben 6 ore di lavoro continuo alla massima potenza</p><p>Inoltre, la nuova lucidatrice riconosce il tipo di lavoro che stai eseguendo e calibra in maniera automatica velocità e potenza in modo da garantirti le massime prestazioni</p>":
    "<p>Las dos baterías de 18V garantizan 6 horas de trabajo continuo a la máxima potencia</p><p>Además, la nueva pulidora reconoce el tipo de trabajo que estás realizando y calibra de manera automática velocidad y potencia para garantizarte las máximas prestaciones</p>",
    
    "<p style=\"margin-bottom: 0.9rem; caret-color: #333333; color: #333333; font-size: 12px; text-align: center; text-size-adjust: auto;\"><span style=\"font-size: 10px;\">This site is not a part of the Facebook website or Facebook Inc. Additionally, this site is NOT endorsed by Facebook in any way. Facebook is a trademark of Facebook, Inc</span></p>":
    "<p style=\"margin-bottom: 0.9rem; caret-color: #333333; color: #333333; font-size: 12px; text-align: center; text-size-adjust: auto;\"><span style=\"font-size: 10px;\">Este sitio no es parte del sitio web de Facebook o Facebook Inc. Además, este sitio NO está respaldado por Facebook de ninguna manera. Facebook es una marca registrada de Facebook, Inc</span></p>",
    
    "<p>\u00a9 2023 Tutti i diritti riservati.</p>":
    "<p>\u00a9 2023 Todos los derechos reservados.</p>",
    
    "<p>PRIVACY<span style=\"color: var( --e-global-color-text ); font-weight: var( --e-global-typography-text-font-weight );\"> </span> CONTATTI</p>":
    "<p>PRIVACIDAD<span style=\"color: var( --e-global-color-text ); font-weight: var( --e-global-typography-text-font-weight );\"> </span> CONTACTO</p>",
    
    "Lucidatrice Roto-Orbitale<br>+ 1 Disco per Smerigliatura<br>+ 1 Disco per Lucidatura<br>+ 1 Disco per Inceratura<br>+ 1 Disco Graffi e Macchie<br>+ 1 Disco Universale<br> + 2 Batterie 18V<br>+ Caricabatterie<br>+ Valigetta e Kit Accessori<br>A SOLI 79\u20ac":
    "Pulidora Roto-Orbital<br>+ 1 Disco de Lijado<br>+ 1 Disco de Pulido<br>+ 1 Disco de Encerado<br>+ 1 Disco para Arañazos y Manchas<br>+ 1 Disco Universal<br> + 2 Baterías 18V<br>+ Cargador<br>+ Maletín y Kit de Accesorios<br>POR SOLO 75\u20ac",
    
    "Lucidatrice Rotorbitale<br>+ 1 Disco per Lucidatura<br>+ 1 Disco per Inceratura<br>+ 1 Disco graffi e macchie<br>+ 1 Disco Universale<br> + 2 Batterie 18V<br>+ Caricabatterie<br>+ Valigetta e Accessori<br>+ Ricambi per 4 Anni<br>A SOLI 79\u20ac":
    "Pulidora Roto-Orbital<br>+ 1 Disco de Pulido<br>+ 1 Disco de Encerado<br>+ 1 Disco para arañazos y manchas<br>+ 1 Disco Universal<br> + 2 Baterías 18V<br>+ Cargador<br>+ Maletín y Accesorios<br>+ Repuestos por 4 Años<br>POR SOLO 75\u20ac",
    
    "OFFERTA TUTTO INCLUSO a soli \u20ac 79": "OFERTA TODO INCLUIDO por solo 75\u20ac",
    
    "invece di \u20ac395": "en lugar de 150\u20ac",
    
    "Orbita fino a 180mm": "Órbita hasta 180mm",
    "Perfetta per: Lucidare, Incerare, Rimuovere Graffi, Segni e Macchie, Riportare a nuovo superfici": "Perfecta para: Pulir, Encerar, Eliminar Arañazos, Marcas y Manchas, Restaurar superficies",
    "Motore Brushless 1900W": "Motor Brushless 1900W",
    "19.000 Giri/Min": "19.000 RPM",
    "Doppia Batteria 18V": "Doble Batería 18V",
    "Per Auto, Moto, Barche, Legno, Piastrelle, Pavimenti e tanto altro": "Para Coches, Motos, Barcos, Madera, Azulejos, Suelos y mucho más",
    "4 Dischi Intercambiabili ": "4 Discos Intercambiables ",
    "6 Ore di lavoro alla massima potenza": "6 Horas de trabajo a la máxima potencia",
    "Impugnatura ergonomica anti fatica": "Empuñadura ergonómica anti fatiga",
    "Pesa solo 800 grammi": "Pesa solo 800 gramos",
    "100% Sicura e Affidabile": "100% Segura y Fiable",
    "Qualit\u00e0 Premium": "Calidad Premium",
    "Garanzia e Ricambi per 4 Anni ": "Garantía y Repuestos por 4 Años ",
    "Reso Gratuito 60 giorni": "Devolución Gratuita 60 días",
    "Pagamento alla consegna  e Spedizione Rapida": "Pago a la entrega y Envío Rápido",
    
    "Lucidatrice Rotorbitale": "Pulidora Roto-Orbital",
    "1 Disco per Lucidatura": "1 Disco de Pulido",
    "1 Disco per Inceratura": "1 Disco de Encerado",
    "1 Disco per Rimuovere Macchie e Graffi": "1 Disco para Eliminar Manchas y Arañazos",
    "1 Disco Universale": "1 Disco Universal",
    "Due batterie da 18V": "Dos baterías de 18V",
    "Caricabatterie": "Cargador",
    "Kit cambio dischi": "Kit cambio de discos",
    "Guanti da Lavoro": "Guantes de Trabajo",
    "Valigetta Professionale": "Maletín Profesional",
    "Garanzia Ricambi 4 Anni": "Garantía Repuestos 4 Años",
    "Consegna Rapida Assicurata": "Entrega Rápida Asegurada",
    "Reso Gratuito 60 giorni": "Devolución Gratuita 60 días"
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
                else:
                    if txt == "Lavora perfettamente Auto, Moto, Barche, Mobili, Piastrelle, Marmo, Legno e tanto altro grazie al Potente Motore Brushless da 3000 Watt con 6 Livelli di Velocità e Doppia Batteria da 18V  ":
                        settings["title"] = TRANSLATIONS[txt]

            # Check Editor
            if "editor" in settings:
                txt = settings["editor"]
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
                             item["text"] = TRANSLATIONS[txt.strip()] 
        
        if "elements" in element:
            translate_elements(element["elements"])

def main():
    print(f"Reading {INPUT_FILE}...")
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if "content" in data:
        translate_elements(data["content"])
    
    print(f"Saving to {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, separators=(',', ':'))

    print("Done.")

if __name__ == "__main__":
    main()
