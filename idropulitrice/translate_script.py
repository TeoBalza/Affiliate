import json
import re

input_file = 'idropulitrice-it.json'
output_file = 'idropulitrice-gr.json'

def translate_text(text):
    # Dictionary of exact matches (stripping checks might be needed)
    translations = {
        "Pagamento sicuro alla consegna": "Ασφαλής πληρωμή με αντικαταβολή",
        "La Professionale Idropulitrice Industriale Senza Fili ad Alta Pressione Da 260 Bar che Elimina lo Sporco da Auto, Moto, Bici, Pavimenti, Terrazzo e Piastrelle In Una Sola Passata E Senza Sprechi d’Acqua": "Το Επαγγελματικό Ασύρματο Βιομηχανικό Πλυστικό Υψηλής Πίεσης 260 Bar που Εξαφανίζει τη Βρωμιά από Αυτοκίνητα, Μοτοσυκλέτες, Ποδήλατα, Δάπεδα, Βεράντες και Πλακάκια Με Ένα Μόνο Πέρασμα Και Χωρίς Σπατάλη Νερού",
        "Pulisce ed Elimina sporcizia ed impurità in metà del tempo grazie agli ugelli regolabili in ottone a 6 modalità di pressione.": "Καθαρίζει και Εξαλείφει βρωμιά και ακαθαρσίες στο μισό χρόνο χάρη στα ρυθμιζόμενα ορείχαλκα ακροφύσια με 6 λειτουργίες πίεσης.",
        "OFFERTA DEL MESE": "ΠΡΟΣΦΟΡΑ ΤΟΥ ΜΗΝΑ",
        "Compila il modulo per ordinare": "Συμπληρώστε τη φόρμα για παραγγελία",
        "Dimentica scomodi tubi di irrigazione, getti irregolari e macchie ostinate!\n\n\n\n\n\n\n": "Ξεχάστε τα άβολα λάστιχα ποτίσματος, τις ακανόνιστες ριπές και τους επίμονους λεκεδες!",
        "Dimentica scomodi tubi di irrigazione, getti irregolari e macchie ostinate!": "Ξεχάστε τα άβολα λάστιχα ποτίσματος, τις ακανόνιστες ριπές και τους επίμονους λεκεδες!",
        "invece di €319": "αντί για €160",
        "namesto €319": "αντί για €160",
        "Manuale di istruzioni in italiano": "Εγχειρίδιο οδηγιών",
        "4 anni di estensione di Garanzia OMAGGIO": "4 χρόνια επέκταση Εγγύησης ΔΩΡΟ",
        "Spedizione rapida 24 ore e pagamento alla consegna": "Γρήγορη αποστολή 24 ωρών και πληρωμή με αντικαταβολή",
        "Reso Gratuito": "Δωρεάν Επιστροφή",
        "© 2023 Tutti i diritti riservati.": "© 2023 Με την επιφύλαξη παντός δικαιώματος.",
        "PRIVACY&nbsp;&nbsp;CONTATTI": "ΠΟΛΙΤΙΚΗ ΑΠΟΡΡΗΤΟΥ&nbsp;&nbsp;ΕΠΙΚΟΙΝΩΝΙΑ", # Handling non-breaking spaces if any
        "PRIVACY\u00a0\u00a0CONTATTI": "ΠΟΛΙΤΙΚΗ ΑΠΟΡΡΗΤΟΥ\u00a0\u00a0ΕΠΙΚΟΙΝΩΝΙΑ",
    }
    
    # Check exact match
    if text in translations:
        return translations[text]
    
    # Partial/Regex replacements for complex strings
    
    # Main Product Box
    if "Idropulitrice Industriale" in text and "A SOLI 69€" in text:
        text = text.replace("Idropulitrice Industriale", "Βιομηχανικό Πλυστικό")
        text = text.replace("+ Tubo alta pressione 12mt", "+ Σωλήνας υψηλής πίεσης 12μ")
        text = text.replace("+ Ugelli Regolabili", "+ Ρυθμιζόμενα Ακροφύσια")
        text = text.replace("+ 2 Batterie 21V 5Ah", "+ 2 Μπαταρίες 21V 5Ah")
        text = text.replace("+ Caricabatterie", "+ Φορτιστής")
        text = text.replace("+ Garanzia Ricambi 4 anni", "+ Εγγύηση Ανταλλακτικών 4 χρόνια")
        text = text.replace("A SOLI 69€", "ΜΟΝΟ 79€")
        return text

    # Text Block 1
    if "L'idropulitrice è dotata di un motore senza spazzole" in text:
        text = text.replace("L'idropulitrice è dotata di un motore senza spazzole con pompa di aspirazione in grado di generare una pressione di 260 bar.", "Το πλυστικό διαθέτει κινητήρα χωρίς ψύκτρες με αντλία αναρρόφησης ικανή να παράγει πίεση 260 bar.")
        text = text.replace("Aspira con forza l’acqua e concentra il flusso in pochissimi millimetri quadrati tramite l’ugello in ottone regolabile a 6 modalità, perfetto per qualsiasi utilizzo, sia a bassa che ad alta pressione.", "Αναρροφά δυνατά το νερό και συγκεντρώνει τη ροή σε ελάχιστα τετραγωνικά χιλιοστά μέσω του ρυθμιζόμενου ορείχαλκου ακροφυσίου 6 λειτουργιών, ιδανικό για κάθε χρήση, τόσο σε χαμηλή όσο και σε υψηλή πίεση.")
        return text

    # Text Block 2
    if "Può essere utilizzata anche senza collegarla al rubinetto" in text:
        text = text.replace("Può essere utilizzata anche senza collegarla al rubinetto, grazie alla tecnologia a pescaggio tramite il tubo con filtro incluso nella confezione.", "Μπορεί να χρησιμοποιηθεί και χωρίς σύνδεση στη βρύση, χάρη στην τεχνολογία άντλησης μέσω του σωλήνα με φίλτρο που περιλαμβάνεται στη συσκευασία.")
        text = text.replace("Ti basta inserire il tubo in un secchio d’acqua, un pozzo o una fontana, l’acqua verrà filtrata ed entrerà in circolo nel sistema di erogazione ad alta pressione.", "Απλά βάλτε το σωλήνα σε έναν κουβά με νερό, ένα πηγάδι ή μια βρύση, το νερό θα φιλτραριστεί και θα μπει στο σύστημα παροχής υψηλής πίεσης.")
        text = text.replace("Inoltre la confezione include 2 adattatori universali per collegarlo a qualsiasi pompa da giardino e rubinetto, dentro e fuori casa.", "Επιπλέον, η συσκευασία περιλαμβάνει 2 αντάπτορες γενικής χρήσης για σύνδεση σε οποιαδήποτε αντλία κήπου και βρύση, μέσα και έξω από το σπίτι.")
        return text

    # Text Block 3
    if "Con la potentissima idropulitrice puoi utilizzare detergenti" in text:
        text = text.replace("Con la potentissima idropulitrice puoi utilizzare detergenti e sgrassanti durante la pulizia grazie all’attacco con contenitore incluso nella confezione.", "Με το πανίσχυρο πλυστικό μπορείτε να χρησιμοποιήσετε απορρυπαντικά και λιποκαθαριστικά κατά τον καθαρισμό χάρη στο εξάρτημα με δοχείο που περιλαμβάνεται στη συσκευασία.")
        text = text.replace("Usa l'idropulitrice per disincrostare e pulire a fondo:", "Χρησιμοποιήστε το πλυστικό για να αφαιρέσετε κρούστες και να καθαρίσετε βαθιά:")
        text = text.replace("auto, bici, moto, vialetti, fughe di piastrelle, box doccia, pavimenti, pareti, staccionate, tende da sole, tapparelle ed elimina efficacemente muffa, muschio e resine in un colpo solo.", "αυτοκίνητα, ποδήλατα, μοτοσυκλέτες, διαδρόμους, αρμούς πλακιδίων, καμπίνες ντους, δάπεδα, τοίχους, φράχτες, τέντες, ρολά και να εξαλείψετε αποτελεσματικά μούχλα, βρύα και ρητίνες με μια κίνηση.")
        return text

    # Text Block 4
    if "E’ dotata di due batterie 21V 5000mAh" in text:
        text = text.replace("E’ dotata di due batterie 21V 5000mAh con un autonomia di ben 8 ore di lavorazione continua. L’auto-sovraccarico e la protezione dalla temperatura offrono una durata della batteria molto più lunga.", "Διαθέτει δύο μπαταρίες 21V 5000mAh με αυτονομία 8 ωρών συνεχούς εργασίας. Η προστασία από υπερφόρτωση και θερμοκρασία προσφέρουν πολύ μεγαλύτερη διάρκεια ζωής της μπαταρίας.")
        return text
    
    # Offer Box
    if "Se ordini oggi, riceverai GRATIS" in text:
        text = text.replace("Se ordini oggi, riceverai GRATIS:", "Αν παραγγείλετε σήμερα, θα λάβετε ΔΩΡΕΑΝ:")
        text = text.replace("6 Ugelli regolabili", "6 Ρυθμιζόμενα Ακροφύσια")
        text = text.replace("+ Tubo alta pressione 12mt", "+ Σωλήνας υψηλής πίεσης 12μ")
        text = text.replace("+ Contenitore per sgrassatori e detergenti", "+ Δοχείο για λιποκαθαριστικά και απορρυπαντικά")
        text = text.replace("+ Garanzia RICAMBI 5 anni", "+ Εγγύηση ΑΝΤΑΛΛΑΚΤΙΚΩΝ 5 χρόνια")
        return text
    
    # Bottom Order
    if "Compila il modulo per ordinare la potente idropulitrice con accessori a soli" in text:
        # Regex to handle price safely if needed, but string replace is fine if exact
        text = text.replace("Compila il modulo per ordinare la potente idropulitrice con accessori a soli € 69", "Συμπληρώστε τη φόρμα για να παραγγείλετε το ισχυρό πλυστικό με αξεσουάρ μόνο με € 79")
        return text
    
    # Disclaimer
    if "This site is not a part of the Facebook website" in text:
        # Translating disclaimer as well
        text = text.replace("This site is not a part of the Facebook website or Facebook Inc. Additionally, this site is NOT endorsed by Facebook in any way. Facebook is a trademark of Facebook, Inc", "Αυτός ο ιστότοπος δεν αποτελεί μέρος του ιστότοπου του Facebook ή της Facebook Inc. Επιπλέον, αυτός ο ιστότοπος ΔΕΝ υποστηρίζεται από το Facebook με κανέναν τρόπο. Το Facebook είναι εμπορικό σήμα της Facebook, Inc")
        return text

    # Copyright
    if "Tutti i diritti riservati" in text:
        text = text.replace("Tutti i diritti riservati.", "Με την επιφύλαξη παντός δικαιώματος.")
        return text

    # Handle Privacy/Contacts with nbsp
    if "PRIVACY" in text and "CONTATTI" in text:
        text = text.replace("PRIVACY", "ΠΟΛΙΤΙΚΗ ΑΠΟΡΡΗΤΟΥ")
        text = text.replace("CONTATTI", "ΕΠΙΚΟΙΝΩΝΙΑ")
        return text
        
    return text

# Icon List individual items
icon_translations = {
    "Idropulitrice Professionale Industriale": "Επαγγελματικό Βιομηχανικό Πλυστικό",
    "2 Batterie 21V 5Ah": "2 Μπαταρίες 21V 5Ah",
    "Caricabatterie ultra-rapido": "Υπερ-γρήγορος φορτιστής",
    "Tubo per alta pressione da 12 metri": "Σωλήνας υψηλής πίεσης 12 μέτρων",
    "Filtro per uso a pescaggio acqua": "Φίλτρο για άντληση νερού",
    "Ugello regolabile 6 modalità": "Ρυθμιζόμενο ακροφύσιο 6 λειτουργιών",
    "Ugello bassa pressione": "Ακροφύσιο χαμηλής πίεσης",
    "Ugello alta pressione": "Ακροφύσιο υψηλής πίεσης",
    "Contenitore per sgrassatori e detergenti": "Δοχείο για λιποκαθαριστικά και απορρυπαντικά",
    "Adattatore universale regolabile per rubinetti e tubi da giardino": "Ρυθμιζόμενος αντάπτορας γενικής χρήσης για βρύσες και λάστιχα κήπου",
    "Valigetta rigida per il trasporto": "Σκληρή βαλίτσα μεταφοράς",
    "Manuale di istruzioni in italiano": "Εγχειρίδιο οδηγιών",
    "4 anni di estensione di Garanzia OMAGGIO": "4 χρόνια επέκταση Εγγύησης ΔΩΡΟ",
    "Spedizione rapida 24 ore e pagamento alla consegna": "Γρήγορη αποστολή 24 ωρών και πληρωμή με αντικαταβολή",
    "Reso Gratuito": "Δωρεάν Επιστροφή"
}

def traverse(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(value, str):
                # Check for keys that typically hold user-visible text
                if key in ['title', 'editor', 'inner_text']:
                    obj[key] = translate_text(value)
                elif key == 'text' and 'icon_list' in str(obj): # Heuristic for icon list items
                     pass # handled below
            
            # Specific handling for icon lists which are lists of dicts
            if key == 'icon_list' and isinstance(value, list):
                for item in value:
                    if 'text' in item:
                        if item['text'] in icon_translations:
                            item['text'] = icon_translations[item['text']]
                        else:
                            # Fallback or check if it needs translation
                             item['text'] = translate_text(item['text'])
            
            traverse(value)
    elif isinstance(obj, list):
        for item in obj:
            traverse(item)

# Load JSON
with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Traverse and translate
traverse(data)

# Save JSON
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False) # Elementor JSONs often don't want pretty print to save space, but ensure_ascii=False is crucial for Greek.
    # Note: original file was compacted (one line). I will not use indent to match style, but json.dump usually creates a single line if indent is not specified.

print("Translation completed.")
