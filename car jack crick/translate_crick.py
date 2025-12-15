import json
import copy

# Load original file
with open('crick.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Create deep copy
translated_data = copy.deepcopy(data)

# Translation map (ID -> modifications)
# We will iterate through elements and apply changes based on ID matches to be safe.
# Or better, we define a dictionary of ID -> string replacements if simple, 
# but some require internal HTML replacement.

def replace_text(element, new_title=None, new_editor=None, new_icon_list=None):
    if new_title is not None and 'settings' in element and 'title' in element['settings']:
        element['settings']['title'] = new_title
    
    if new_editor is not None and 'settings' in element and 'editor' in element['settings']:
        # We need to be careful with HTML tags in editor.
        # For this task, strict replacement of specific text blocks is requested.
        # However, the user said "Traduci SOLO testi visibili". 
        # I will replace the text content.
        element['settings']['editor'] = new_editor

    if new_icon_list is not None and 'settings' in element and 'icon_list' in element['settings']:
        for i, item in enumerate(element['settings']['icon_list']):
            if i < len(new_icon_list):
                item['text'] = new_icon_list[i]

def translate_recursive(elements):
    for el in elements:
        el_id = el.get('id')
        
        if el_id == '757b49c5': # Heading
            replace_text(el, new_title="Spedizione assicurata e pagamento alla consegna")
            
        elif el_id == '76a22200': # Heading
            replace_text(el, new_title="Il cric idraulico professionale a basso profilo e doppio pistone che solleva auto, moto, SUV, furgoni e camper fino a 4.000kg senza sforzo")
            
        elif el_id == '358f16c7': # Heading
            replace_text(el, new_title="Utilizzato in officine, cantieri e fabbriche, è compatibile con veicoli di ogni marca e modello e garantisce un sollevamento facile, stabile e senza sforzo da 70mm a 600mm")
            
        elif el_id == '641ed634': # Progress Bar (inner_text)
            if 'settings' in el and 'inner_text' in el['settings']:
                el['settings']['inner_text'] = "OFFERTA SPECIALE"
                
        elif el_id == '2b5f2494': # Heading
            replace_text(el, new_title="ProLifter® Cric Idraulico Professionale<br>+ Asta di sollevamento idraulica<br>+ Tamponi in gomma<br>+ Ruote di ricambio<br>+ Garanzia 20 anni<br>SOLO A 99€")
            
        elif el_id == '46854f12': # Heading
            replace_text(el, new_title="invece di 200€")
            
        elif el_id == '66680b0f': # Heading
            replace_text(el, new_title="GARANZIA COMPLETA 20 ANNI")
            
        elif el_id == '352bc1c1': # Heading
            replace_text(el, new_title="Compila il modulo sottostante per ordinare")
            
        elif el_id == '6d4b94e7': # Form (button text usually? No, it's a shortcode form, but let's check settings)
            # It's an eael-contact-form-7. Usually text is in WP CF7, not here. 
            # But checking settings... nothing visible to translate in JSON except maybe placeholders if customizable?
            # "typography_placeholder_typography" is there. 
            # No visible text found to translate in the specific element settings shown in original file.
            pass
            
        elif el_id == '4b2b15dd': # Heading
            replace_text(el, new_title="Solleva con sicurezza, velocità e senza sforzo tutti i tipi di auto, moto, SUV, furgoni e camper fino a 4.000 kg")
            
        elif el_id == '739bb27f': # Text Editor
             # HTML content needs keeping tags
            content = """<p data-start="0" data-end="199"><span style="text-decoration: underline;">Doppio pistone idraulico<br /></span></p><p data-start="0" data-end="199">L'innovativo sistema di sollevamento basso a doppio pistone idraulico ti permette di sollevare fino a 4.000 kg in pochi secondi e senza sforzo<br data-start="211" data-end="214" />La struttura e il manico del ProLifter® sono realizzati interamente in acciaio rinforzato, garantendo un supporto stabile e affidabile<br data-start="356" data-end="359" />Inoltre, è facile da manovrare e trasportare grazie alle ruote in gomma bidirezionali e al peso di soli 15 kg</p>"""
            replace_text(el, new_editor=content)
            
        elif el_id == '5a94d2c7': # Text Editor
            content = """<p data-start="53" data-end="449"><span style="text-decoration: underline;">Per ogni veicolo</span></p><p data-start="53" data-end="449">Il ProLifter® è ideale per il sollevamento di qualsiasi veicolo come auto, moto, SUV, furgoni e camper di tutte le marche e modelli<br data-start="228" data-end="231" />Il profilo basso ti permette di sollevare anche veicoli molto bassi con un'altezza minima di 70mm<br data-start="325" data-end="328" />Inoltre, il tampone in gomma dal diametro di 100mm garantisce un sollevamento rapido, sicuro e stabile fino a un'altezza massima di 600mm</p>"""
            replace_text(el, new_editor=content)

        elif el_id == '7bc0518f': # Text Editor
            content = """<p data-start="0" data-end="170"><span style="text-decoration: underline;">Garantito per 20 anni</span></p><p data-start="0" data-end="170">Il ProLifter® è un prodotto garantito al 100% per oltre 20 anni<br data-start="160" data-end="163" />Basta collegare il manico e premere per sollevare progressivamente<br data-start="232" data-end="235" />Il sistema di abbassamento a leva è regolabile, leggero e fluido<br data-start="300" data-end="303" />Tutti i componenti sono sigillati con sistema anti-perdita e non richiede manutenzione come spurgo o aggiunta di olio</p>"""
            replace_text(el, new_editor=content)

        elif el_id == '5ecce321': # Text Editor with weird Article wrapper
            # We preserve the wrapper.
            content = """<article class="text-token-text-primary w-full" dir="auto" data-testid="conversation-turn-22" data-scroll-anchor="true"><div class="text-base my-auto mx-auto py-5 [--thread-content-margin:--spacing(4)] @[37rem]:[--thread-content-margin:--spacing(6)] @[72rem]:[--thread-content-margin:--spacing(16)] px-(--thread-content-margin)"><div class="[--thread-content-max-width:32rem] @[34rem]:[--thread-content-max-width:40rem] @[64rem]:[--thread-content-max-width:48rem] mx-auto flex max-w-(--thread-content-max-width) flex-1 text-base gap-4 md:gap-5 lg:gap-6 group/turn-messages focus-visible:outline-hidden" tabindex="-1"><div class="group/conversation-turn relative flex w-full min-w-0 flex-col agent-turn"><div class="relative flex-col gap-1 md:gap-3"><div class="flex max-w-full flex-col grow"><div class="min-h-8 text-message relative flex w-full flex-col items-end gap-2 text-start break-words whitespace-normal [.text-message+&amp;]:mt-5" dir="auto" data-message-author-role="assistant" data-message-id="b931a073-8876-46e4-8df6-ba006f97113b" data-message-model-slug="gpt-4o"><div class="flex w-full flex-col gap-1 empty:hidden first:pt-[3px]"><div class="markdown prose dark:prose-invert w-full break-words light"><p data-start="0" data-end="190" data-is-last-node="" data-is-only-node=""><span style="text-decoration: underline;">Per ogni applicazione</span></p><p data-start="0" data-end="190" data-is-last-node="" data-is-only-node="">Usalo per cambiare gomme, freni e controllare lo stato di manutenzione di ogni veicolo<br data-start="189" data-end="192" />Il ProLifter® è ideale sia per uso amatoriale che professionale<br data-start="273" data-end="276" />Il kit in offerta include cric con sistema di sollevamento, una valigetta per il trasporto, tampone di ricambio e manico antiscivolo</p></div></div></div></div></div></div></div></div></article>"""
            replace_text(el, new_editor=content)

        elif el_id == '460750a5': # Heading
            replace_text(el, new_title="ProLifter® Cric Idraulico Professionale<br>+ Asta di sollevamento idraulica<br>+ Tamponi in gomma<br>+ Ruote di ricambio<br>+ Garanzia 20 anni<br>SOLO A 99€")

        elif el_id == '665d5d8': # Heading
            replace_text(el, new_title="invece di 200€")

        elif el_id == '6312129f': # Heading
            replace_text(el, new_title="Compila il modulo sottostante per ordinare")

        elif el_id == '2fa238d3': # Heading
            replace_text(el, new_title="Se ordini oggi, ricevi gratis:<br><br>+ Tampone di ricambio<br>+ Valigetta professionale<br>+ Manuale di istruzioni<br>+ 20 anni di estensione garanzia OMAGGIO<br>+ Garanzia soddisfatti o rimborsati 60 giorni<br>+ Spedizione rapida in 24 ore con pagamento alla consegna")

        elif el_id == '435e0d0c': # Icon List
            items = [
                "CAPACITÀ 4.000 KG: Grazie al doppio pistone idraulico può sollevare facilmente fino a 4 tonnellate senza sforzo e si adatta all'uso su tutti i veicoli come auto, moto, SUV, furgoni e camper",
                "PROFILO BASSO E SOLLEVAMENTO FINO A 600MM: Grazie al profilo basso puoi sollevare anche auto sportive molto basse da 70mm e sollevare fino all'altezza massima di 600mm per qualsiasi lavoro di controllo e manutenzione con comodità",
                "SOLLEVAMENTO RAPIDO: Il manico antiscivolo allungabile migliora la presa e potenzia l'azione di leva per un sollevamento facile e veloce senza sforzo",
                "SICURO E RESISTENTE: La costruzione in acciaio rinforzato con sistema di bloccaggio garantisce una tenuta stabile senza rischio di cedimento, per una sicurezza senza precedenti del veicolo e dell'operatore",
                "TAMPONE PROTETTIVO: Il tampone protettivo di diametro 100mm garantisce una presa antiscivolo stabile e protegge i veicoli dai graffi",
                "MANUTENZIONE ZERO: La costruzione sigillata con olio di alta qualità non necessita di spurgo iniziale, cambio olio o rabbocchi. Arriva pronto all'uso e garantisce oltre 20 anni di funzionamento",
                "SODDISFATTI O RIMBORSATI 60 GIORNI: Se non sei soddisfatto e il nostro prodotto non risponde alle tue aspettative, puoi restituirlo entro 60 giorni completamente gratis"
            ]
            replace_text(el, new_icon_list=items)

        elif el_id == '76243fb0': # Heading
            replace_text(el, new_title="Inoltre, se ordini oggi riceverai in omaggio l'estensione della garanzia per 20 anni")

        elif el_id == '1366fb4c': # Icon List
             items = [
                "Cric Idraulico Professionale ProLifter®",
                "Tampone di ricambio",
                "Valigetta professionale",
                "Manuale di istruzioni",
                "20 anni di estensione garanzia OMAGGIO",
                "Garanzia soddisfatti o rimborsati 60 giorni",
                "Spedizione rapida in 24 ore con pagamento alla consegna"
            ]
             replace_text(el, new_icon_list=items)
             
        elif el_id == '3c0b904': # Heading
             replace_text(el, new_title="Compila ora il modulo con i tuoi dati per ordinare il cric idraulico industriale professionale con accessori e garanzia inclusi, solo a 99€")

        elif el_id == '6b08354a': # Text Editor (Disclaimer)
             content = """<p style="margin-bottom: 0.9rem; caret-color: #333333; color: #333333; font-size: 12px; text-align: center; text-size-adjust: auto;"><span style="font-size: 10px;">Questo sito non fa parte del sito Facebook o Facebook Inc. Inoltre, questo sito NON è approvato da Facebook in alcun modo. Facebook è un marchio registrato di Facebook, Inc</span></p>"""
             replace_text(el, new_editor=content)
        
        # Recurse
        if 'elements' in el:
            translate_recursive(el['elements'])

# Start recursion
# The structure usually has a top level 'content' list.
if 'content' in translated_data:
    translate_recursive(translated_data['content'])

# Save
with open('crick-it.json', 'w', encoding='utf-8') as f:
    json.dump(translated_data, f, ensure_ascii=False) # Elementor often prefers no spaces to save size but default is ok. 
    # Actually, allow separators to be compact to match typical minified style if original was,
    # but original had keys quoted etc. `json.dump` is fine.

print("Done generating crick-it.json")

# Verification
def get_keys(obj):
    keys = set()
    if isinstance(obj, dict):
        for k in obj:
            keys.add(k)
            keys.update(get_keys(obj[k]))
    elif isinstance(obj, list):
        for item in obj:
            keys.update(get_keys(item))
    return keys

# Compare keys
orig_keys = get_keys(data)
new_keys = get_keys(translated_data)

if orig_keys == new_keys:
    print("Structure validation passed: Keys match.")
else:
    print("Structure validation FAILED: Keys mismatch.")
    diff = orig_keys.symmetric_difference(new_keys)
    print(diff)

