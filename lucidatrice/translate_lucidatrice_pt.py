import json
import re

# File paths
INPUT_FILE = '/Users/matteo/Documents/GitHub/forno/lucidatrice/lucidatrice-it.json'
OUTPUT_FILE = '/Users/matteo/Documents/GitHub/forno/lucidatrice/lucidatrice-pt.json'

# Translation Map (Italian -> Portuguese)
TRANSLATIONS = {
    # Main Headlines & Text
    "SVENDITA TOTALE": "LIQUIDAÇÃO TOTAL",
    "La Potente Lucidatrice Roto-Orbitale e Angolare con Motore Brushless a Doppia Azione che Lucida, Incera e Rimuove Graffi, Macchie e Aloni da ogni tipo di superficie in sicurezza e senza fatica": "A Potente Polidora Roto-Orbital e Angular com Motor Brushless de Dupla Ação que Pule, Encera e Remove Riscos, Manchas e Auras de qualquer tipo de superfície com segurança e sem esforço",
    "Lavora perfettamente Auto, Moto, Barche, Mobili, Piastrelle, Marmo, Legno e tanto altro grazie al Potente Motore Brushless da 3000 Watt con 6 Livelli di Velocità e Doppia Batteria da 18V  ": "Funciona perfeitamente em Carros, Motos, Barcos, Móveis, Azulejos, Mármore, Madeira e muito mais graças ao Potente Motor Brushless de 3000 Watts com 6 Níveis de Velocidade e Bateria Dupla de 18V  ",
    
    "OFFERTA TUTTO INCLUSO": "OFERTA TUDO INCLUÍDO",
    "GARANZIA RICAMBI 4 ANNI": "GARANTIA DE PEÇAS 4 ANOS",
    "Compila il modulo per ordinare": "Preencha o formulário para encomendar",
    "Lavori professionali e fai da te con la Potente Lucidatrice Roto-orbitale 180mm": "Trabalhos profissionais e de bricolage com a Potente Polidora Roto-orbital 180mm",
    "Scheda Tecnica Lucidatrice Rotorbitale:": "Ficha Técnica Polidora Rotorbital:",
    "Cosa riceverai a casa?": "O que receberá em casa?",
    "OFFERTA TUTTO INCLUSO a soli € 79": "OFERTA TUDO INCLUÍDO por apenas 75 €",
    
    # HTML Content (Text Editors) - Exact String Matching
    "<p>Risultati straordinari grazie al potente Motore Brushless da 19.000 Giri/Min e 3000W.&nbsp;</p>\n<p>Con 2 Filtri D'aria e 6 diverse regolazioni di velocità&nbsp;il motore non si surriscalda mai anche dopo molte ore di utilizzo</p>\n<p>Con un peso di soli 800g è realizzata interamente in Acciaio Inox e Alluminio, con impugnatura ergonomica, è leggera, facile da maneggiare e non affatica mani e braccia</p>": 
    "<p>Resultados extraordinários graças ao potente Motor Brushless de 19.000 RPM e 3000W.&nbsp;</p>\n<p>Com 2 Filtros de Ar e 6 regulações de velocidade diferentes&nbsp;o motor nunca sobreaquece mesmo após muitas horas de uso</p>\n<p>Com um peso de apenas 800g, é fabricada inteiramente em Aço Inox e Alumínio, com pega ergonómica, é leve, fácil de manusear e não cansa mãos e braços</p>",

    "<p>La Potente Lucidatrice Rotorbitale è perfetta per lucidare e rimettere a nuovo Auto, Moto o Barche</p><p>Inoltre, grazie all'orbita fino a 180 mm e ai 4 Dischi inclusi rimuove graffi e macchie da Legno, Marmo, Piastrelle, Pavimenti e tanto altro</p>":
    "<p>A Potente Polidora Rotorbital é perfeita para polir e renovar Carros, Motos ou Barcos</p><p>Além disso, graças à órbita até 180 mm e aos 4 Discos incluídos, remove riscos e manchas de Madeira, Mármore, Azulejos, Pavimentos e muito mais</p>",

    "<p>La Lucidatrice è super silenziosa e 100% Sicura da utilizzare</p><p>Infatti è dotata di un guscio protettivo che ti ripara da schegge, polvere e detriti</p><p>Grazie alla doppia impugnatura, non affatica braccia e schiena durante l'utilizzo</p>":
    "<p>A Polidora é super silenciosa e 100% Segura de utilizar</p><p>De facto, está equipada com uma proteção que o protege de lascas, pó e detritos</p><p>Graças à pega dupla, não cansa braços e costas durante a utilização</p>",

    "<p>Le due batteria da 18V  garantiscono ben 6 ore di lavoro continuo alla massima potenza</p><p>Inoltre, la nuova lucidatrice riconosce il tipo di lavoro che stai eseguendo e calibra in maniera automatica velocità e potenza in modo da garantirti le massime prestazioni</p>":
    "<p>As duas baterias de 18V  garantem 6 horas de trabalho contínuo na potência máxima</p><p>Além disso, a nova polidora reconhece o tipo de trabalho que está a executar e calibra automaticamente velocidade e potência para garantir o máximo desempenho</p>",

    "<p style=\"margin-bottom: 0.9rem; caret-color: #333333; color: #333333; font-size: 12px; text-align: center; text-size-adjust: auto;\"><span style=\"font-size: 10px;\">This site is not a part of the Facebook website or Facebook Inc. Additionally, this site is NOT endorsed by Facebook in any way. Facebook is a trademark of Facebook, Inc</span></p>":
    "<p style=\"margin-bottom: 0.9rem; caret-color: #333333; color: #333333; font-size: 12px; text-align: center; text-size-adjust: auto;\"><span style=\"font-size: 10px;\">Este site não faz parte do site do Facebook ou da Facebook Inc. Além disso, este site NÃO é endossado pelo Facebook de forma alguma. Facebook é uma marca comercial da Facebook, Inc</span></p>",

    "<p>\u00a9 2023 Tutti i diritti riservati.</p>":
    "<p>\u00a9 2023 Todos os direitos reservados.</p>",

    "<p>PRIVACY<span style=\"color: var( --e-global-color-text ); font-weight: var( --e-global-typography-text-font-weight );\">\u00a0</span>\u00a0CONTATTI</p>":
    "<p>PRIVACIDADE<span style=\"color: var( --e-global-color-text ); font-weight: var( --e-global-typography-text-font-weight );\">\u00a0</span>\u00a0CONTACTOS</p>",

    # Complex Pricing Blocks with HTML
    "Lucidatrice Roto-Orbitale<br>+ 1 Disco per Smerigliatura<br>+ 1 Disco per Lucidatura<br>+ 1 Disco per Inceratura<br>+ 1 Disco Graffi e Macchie<br>+ 1 Disco Universale<br> + 2 Batterie 18V<br>+ Caricabatterie<br>+ Valigetta e Kit Accessori<br>A SOLI 79\u20ac":
    "Polidora Roto-Orbital<br>+ 1 Disco de Lixar<br>+ 1 Disco de Polir<br>+ 1 Disco de Encerar<br>+ 1 Disco Riscos e Manchas<br>+ 1 Disco Universal<br> + 2 Baterias 18V<br>+ Carregador<br>+ Mala e Kit Acessórios<br>POR APENAS 75 €",

    "Lucidatrice Rotorbitale<br>+ 1 Disco per Lucidatura<br>+ 1 Disco per Inceratura<br>+ 1 Disco graffi e macchie<br>+ 1 Disco Universale<br> + 2 Batterie 18V<br>+ Caricabatterie<br>+ Valigetta e Accessori<br>+ Ricambi per 4 Anni<br>A SOLI 79\u20ac":
    "Polidora Rotorbital<br>+ 1 Disco de Polir<br>+ 1 Disco de Encerar<br>+ 1 Disco Riscos e Manchas<br>+ 1 Disco Universal<br> + 2 Baterias 18V<br>+ Carregador<br>+ Mala e Acessórios<br>+ Peças por 4 Anos<br>POR APENAS 75 €",

    "invece di \u20ac395": "em vez de 150 €",

    # Icon Lists
    "Orbita fino a 180mm": "Órbita até 180mm",
    "Perfetta per: Lucidare, Incerare, Rimuovere Graffi, Segni e Macchie, Riportare a nuovo superfici": "Perfeita para: Polir, Encerar, Remover Riscos, Marcas e Manchas, Renovar superfícies",
    "Motore Brushless 1900W": "Motor Brushless 1900W",
    "19.000 Giri/Min": "19.000 RPM",
    "Doppia Batteria 18V": "Bateria Dupla 18V",
    "Per Auto, Moto, Barche, Legno, Piastrelle, Pavimenti e tanto altro": "Para Carros, Motos, Barcos, Madeira, Azulejos, Pavimentos e muito mais",
    "4 Dischi Intercambiabili ": "4 Discos Intercambiáveis ",
    "6 Ore di lavoro alla massima potenza": "6 Horas de trabalho na potência máxima",
    "Impugnatura ergonomica anti fatica": "Pega ergonómica anti-fadiga",
    "Pesa solo 800 grammi": "Pesa apenas 800 gramas",
    "100% Sicura e Affidabile": "100% Segura e Fiável",
    "Qualit\u00e0 Premium": "Qualidade Premium",
    "Garanzia e Ricambi per 4 Anni ": "Garantia e Peças por 4 Anos ",
    "Reso Gratuito 60 giorni": "Devolução Gratuita 60 dias",
    "Pagamento alla consegna  e Spedizione Rapida": "Pagamento na entrega e Envio Rápido",

    "Lucidatrice Rotorbitale": "Polidora Rotorbital",
    "1 Disco per Lucidatura": "1 Disco de Polir",
    "1 Disco per Inceratura": "1 Disco de Encerar",
    "1 Disco per Rimuovere Macchie e Graffi": "1 Disco para Remover Manchas e Riscos",
    "1 Disco Universale": "1 Disco Universal",
    "Due batterie da 18V": "Duas baterias de 18V",
    "Caricabatterie": "Carregador",
    "Kit cambio dischi": "Kit troca de discos",
    "Guanti da Lavoro": "Luvas de Trabalho",
    "Valigetta Professionale": "Mala Profissional",
    "Garanzia Ricambi 4 Anni": "Garantia Peças 4 Anos",
    "Consegna Rapida Assicurata": "Entrega Rápida Segurada",
    "Reso Gratuito 60 giorni": "Devolução Gratuita 60 dias"
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
                    # Strip logic for case with trailing spaces
                    settings["title"] = TRANSLATIONS[txt.strip()]
            
            # Check Editor
            if "editor" in settings:
                txt = settings["editor"]
                if txt in TRANSLATIONS:
                    settings["editor"] = TRANSLATIONS[txt]

            # Check Inner Text
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
    try:
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: {INPUT_FILE} not found.")
        return

    if "content" in data:
        translate_elements(data["content"])
    
    print(f"Saving to {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, separators=(',', ':'))
    
    print("Done.")

if __name__ == "__main__":
    main()
