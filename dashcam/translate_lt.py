import json

# Input string from the read file
original_path = '/Users/matteo/Documents/GitHub/forno/dashcam/dashcam-it.json'
output_path = '/Users/matteo/Documents/GitHub/forno/dashcam/dashcam-lt.json'

with open(original_path, 'r') as f:
    data = json.load(f)

# Define translation map
def translate_text(text):
    translations = {
        "SmartCam®": "SmartCam®",
        "L'innovativa Telecamera per Auto Con GPS che Registra e Localizza la tua Auto per evitare Incidenti, Furti e Frodi Assicurative": "Inovatyvi automobilinė kamera su GPS, kuri įrašo ir nustato jūsų automobilio vietą, kad išvengtumėte avarijų, vagysčių ir draudimo sukčiavimo",
        "Controllo Remoto con Notifiche sul tuo telefono in casi di furti o movimenti sospetti.\nTelecamera 4K Anteriore e Posteriore per una visione a 360°, con registrazione continua anche di notte.\nInstallazione rapida senza Meccanico": "Nuotolinis valdymas su pranešimais į telefoną vagystės ar įtartino judėjimo atveju.\n4K priekinė ir galinė kamera 360° vaizdui su nuolatiniu įrašymu net naktį.\nGreitas montavimas be mechaniko",
        "ULTIME CAM DISPONIBILI": "LIKUSIOS PASKUTINĖS KAMEROS",
        "1 SmartCam®<br>+ Memoria da 512 GB<br>+ Kit Installazione rapida<br>+ Reso Gratuito<br> A SOLI 59€": "1 SmartCam®<br>+ 512 GB atmintis<br>+ Greito montavimo rinkinys<br>+ Nemokamas grąžinimas<br> TIK 59 €",
        "invece di €229": "vietoj 130 €",
        "GARANZIA ESTESA 4 ANNI": "4 METŲ PRATĘSTA GARANTIJA",
        "Compila il modulo per ordinare": "Užpildykite formą norėdami užsisakyti",
        "MONITORA COSTANTEMENTE TUTTO QUELLO CHE SUCCEDE DENTRO E FUORI LA TUA AUTO": "NUOLAT STEBĖKITE VISKĄ, KAS VYKSTA JŪSŲ AUTOMOBILIO VIDUJE IR IŠORĖJE",
        "<p>SmartCam® registra Video e Audio 24h su 24h dentro e fuori la tua Auto.</p><p>La Telecamera SmartCam® cattura tutto ciò che succede al tuo veicolo, anche quando è spento, mandandoti avvisi sul telefono in caso di pericolo, urti, incidenti o movimenti sospetti.</p><p>Grazie alla Scheda di Memoria inclusa da 512GB , la telecamera registra senza interruzioni fino a 30 giorni, fornendoti Video e Audio per proteggerti da Frodi Assicurative e Risarcimenti fasulli.</p><p>Inoltre, ogni volta che vorrai potrai scaricare facilmente i video e gli audio su un Pc o Sul telefono e riprendere normalmente le registrazioni.</p>": "<p>SmartCam® įrašo vaizdą ir garsą 24 valandas per parą jūsų automobilio viduje ir išorėje.</p><p>SmartCam® kamera fiksuoja viską, kas vyksta su jūsų transporto priemone, net kai ji išjungta, siųsdama įspėjimus į telefoną pavojaus, smūgių, avarijų ar įtartinų judesių atveju.</p><p>Dėl pridedamos 512 GB atminties kortelės, kamera nenutrūkstamai įrašo iki 30 dienų, pateikdama vaizdo ir garso įrašus, kad apsaugotų jus nuo draudimo sukčiavimo ir neteisingų reikalavimų atlyginti žalą.</p><p>Be to, bet kada galite lengvai atsisiųsti vaizdo ir garso įrašus į kompiuterį ar telefoną ir toliau tęsti įrašymą.</p>",
        "<p>La doppia Telecamera Integrata a 360°, copre l’intero veicolo con possibilità di zoom per rilevare dettagli, targhe o volti.</p><p>La tecnologia 4K, con obiettivo ad infrarossi, ti garantisce una visione nitida e precisa anche di notte e a lunga distanza.</p><p>La telecamera Anteriore e Posteriore, può essere telecomandata direttamente dal tuo Telefono con l’apposita App gratuita.</p>": "<p>Integruota dviguba 360° kamera apima visą transporto priemonę su galimybe priartinti, kad užfiksuotumėte detales, valstybinius numerius ar veidus.</p><p>4K technologija su infraraudonųjų spindulių objektyvu užtikrina ryškų ir tikslų vaizdą net naktį ir dideliu atstumu.</p><p>Priekinė ir galinė kamera gali būti valdoma tiesiogiai iš jūsų telefono naudojant nemokamą programėlę.</p>",
        "<p>La rivoluzionaria Telecamera SmartCam® è l’unica in commercio ad avere il GPS incorporato che funziona senza Internet o Bluetooth.</p><p>Grazie alla Schede Satellite incorporate, una volta collegata, SmartCam® si aggancia automaticamente alla Rete Satellitare e localizza H24 la tua auto e gli spostamenti.</p><p>Inoltre, potrai seguire e vedere la posizione della tua Auto direttamente sul Telefono grazie all’App gratuita inclusa.</p>": "<p>Revoliucinė SmartCam® kamera yra vienintelė rinkoje, turinti integruotą GPS, kuris veikia be interneto ar „Bluetooth“.</p><p>Dėl integruotų palydovinių kortelių, prijungus, SmartCam® automatiškai prisijungia prie palydovinio tinklo ir 24/7 nustato jūsų automobilio vietą bei judėjimą.</p><p>Be to, galėsite stebėti ir matyti savo automobilio vietą tiesiogiai telefone naudodami pridedamą nemokamą programėlę.</p>",
        "<p>Installare SmartCam® è davvero molto semplice, e non avrai bisogno di aiuto o di andare in Officina.</p><p>Ti basterà applicare la telecamera sul tuo parabrezza, grazie alle ventose extra-fissanti, collegare SmartCam® all’accendi sigari con il cavo di alimentazione da 5 metri incluso e la registrazione partirà in automatico.</p>": "<p>SmartCam® įdiegti labai paprasta, jums nereikės pagalbos ar važiuoti į dirbtuves.</p><p>Tiesiog pritvirtinkite kamerą prie priekinio stiklo naudodami ypač stiprius siurbtukus, prijunkite SmartCam® prie cigarečių degiklio naudodami pridedamą 5 metrų maitinimo laidą, ir įrašymas prasidės automatiškai.</p>",
        "<p>SmartCam® quando collegata all’accendi sigari, si ricarica automaticamente, in modo da garantirti una registrazioni continua con auto spenta fino a 3 giorni.</p><p>La funzione risparmio batteria, ti permette di non consumare la batteria della tua auto, evitando che si scarichi.</p>": "<p>Prijungus prie cigarečių degiklio, SmartCam® automatiškai įsikrauna, užtikrindama nepertraukiamą įrašymą net esant išjungtam automobiliui iki 3 dienų.</p><p>Baterijos taupymo funkcija leidžia nenaudoti automobilio akumuliatoriaus, apsaugodama jį nuo išsikrovimo.</p>",
        "Se ordini oggi avrai in omaggio: <br><br>Cavo di alimentazione 5 metri<br>+ Supporto Ventosa Parabrezza<br>+ Memoria 512 GB<br>+ Reso Gratuito": "Užsisakę šiandien, dovanų gausite: <br><br>5 metrų maitinimo laidą<br>+ Priekinio stiklo siurbtuko laikiklį<br>+ 512 GB atmintį<br>+ Nemokamą grąžinimą",
        "CONTRO INCIDENTI E FRODI ASSICURATIVE": "PRIEŠ AVARIJAS IR DRAUDIMO SUKČIAVIMĄ",
        "DOPPIA TELECAMERA 4K": "DVIGUBA 4K KAMERA",
        "WIFI-GPS": "WIFI-GPS",
        "SCHEDA 512 GB": "512 GB KORTELĖ",
        "BATTERIA A LUNGA DURATA": "ILGAI VEIKIANTI BATERIJA",
        "INTALLAZIONE RAPIDA": "GREITAS MONTAVIMAS",
        "Facile da utilizzare": "Lengva naudoti",
        "Soddisfatti o Rimborsati": "Pinigų grąžinimo garantija",
        "Inoltre, ordinando oggi avrai in omaggio anche l'Estensione di Garanzia Gratis valida 4 Anni": "Be to, užsisakę šiandien, dovanų gausite nemokamą 4 metų pratęstą garantiją",
        "1 Telecamera SmartCam®": "1 SmartCam® kamera",
        "Cavo di Alimentazione da 5 metri": "5 metrų maitinimo laidas",
        "Scheda di memoria 512 GB": "512 GB atminties kortelė",
        "Kit di Installazione Rapida": "Greito montavimo rinkinys",
        "Estensione Garanzia Gratis 4 Anni": "Nemokama 4 metų pratęsta garantija",
        "Pagamento sicuro in contanti alla consegna": "Saugus apmokėjimas grynaisiais pristatymo metu",
        "Spedizione veloce": "Greitas pristatymas",
        "Formula soddisfatti o rimborsati": "Pinigų grąžinimo garantija",
        "OMPILA IL MODULO IN BASSO PER ORDINARE SmartCam® A SOLI €59": "UŽPILDYKITE ŽEMIAU ESANČIĄ FORMĄ IR UŽSISAKYKITE SmartCam® TIK UŽ 59 €",
        "<p style=\"margin-bottom: 0.9rem; caret-color: #333333; color: #333333; font-size: 12px; text-align: center; text-size-adjust: auto;\"><span style=\"font-size: 10px;\">This site is not a part of the Facebook website or Facebook Inc. Additionally, this site is NOT endorsed by Facebook in any way. Facebook is a trademark of Facebook, Inc</span></p>": "<p style=\"margin-bottom: 0.9rem; caret-color: #333333; color: #333333; font-size: 12px; text-align: center; text-size-adjust: auto;\"><span style=\"font-size: 10px;\">Ši svetainė nėra „Facebook“ ar „Facebook Inc.“ dalis. Be to, ši svetainė JOKIU BŪDU nėra remiama „Facebook“. „Facebook“ yra „Facebook, Inc.“ prekės ženklas.</span></p>",
        "<p>© 2023 Tutti i diritti riservati.</p>": "<p>© 2023 Visos teisės saugomos.</p>",
        "<p>PRIVACY<span style=\"color: var( --e-global-color-text ); font-weight: var( --e-global-typography-text-font-weight );\"> </span> CONTATTI</p>": "<p>PRIVATUMAS<span style=\"color: var( --e-global-color-text ); font-weight: var( --e-global-typography-text-font-weight );\"> </span> KONTAKTAI</p>"
    }
    
    if text in translations:
        return translations[text]
    return text

def recursively_translate(node):
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "title" or key == "editor" or key == "inner_text":
                if isinstance(value, str):
                   node[key] = translate_text(value)
            elif key == "icon_list": 
                for item in value:
                     if "text" in item:
                        item["text"] = translate_text(item["text"])
            
            recursively_translate(value)
    elif isinstance(node, list):
        for item in node:
            recursively_translate(item)

recursively_translate(data)

with open(output_path, 'w') as f:
    json.dump(data, f, separators=(',', ':'), ensure_ascii=False)

print("Translation complete.")
