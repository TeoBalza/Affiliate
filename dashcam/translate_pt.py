import json
import copy

def translate_to_pt():
    input_file = '/Users/matteo/Documents/GitHub/forno/dashcam/dashcam-it.json'
    output_file = '/Users/matteo/Documents/GitHub/forno/dashcam/dashcam-pt.json'

    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Dictionary of translations
    # Key: partial unique string or ID to identify, Value: tuple (type, translation_func)
    
    # Prices
    PRICE_DISCOUNT = "57€"
    PRICE_FULL = "130€"
    
    def repl_prices(text):
        # Specific replacements for prices
        text = text.replace("59€", PRICE_DISCOUNT)
        text = text.replace("€229", PRICE_FULL)
        text = text.replace("229€", PRICE_FULL) 
        return text

    # Translation Mappings
    translations = {
        "663c8371": {"title": "SmartCam®"},
        "1da1b9b2": {"title": "A inovadora Câmara para Automóveis Com GPS que Regista e Localiza o seu Carro para evitar Acidentes, Roubos e Fraudes de Seguros"},
        "137c051e": {"title": "Controlo Remoto com Notificações no seu telemóvel em caso de roubos ou movimentos suspeitos.\nCâmara 4K Frontal e Traseira para uma visão a 360°, com gravação contínua mesmo à noite.\nInstalação rápida sem Mecânico"},
        "67a5dc66": {"inner_text": "ÚLTIMAS CÂMARAS DISPONÍVEIS"},
		"a0e4117": {"title": "1 SmartCam®<br>+ Memória de 512 GB<br>+ Kit de Instalação Rápida<br>+ Devolução Gratuita<br> POR APENAS " + PRICE_DISCOUNT},
        "4c2cbd67": {"title": "em vez de " + PRICE_FULL},
        "2aec8124": {"title": "GARANTIA ESTENDIDA 4 ANOS"},
        "4ca914b8": {"title": "Preencha o formulário para encomendar"},
        "64dafcfa": {
             # form button usually in settings but structured differently in lists or internal queries. 
             # Checking the JSON, button text might be in 'button_text' or similar if not default.
             # Actually this is a contact form 7 widget. The form content itself is likely handled by WP plugin, 
             # but the widget might have title/button styles. 
             # Looking at the source, it seems to resort to defaults or external shortcodes.
             # We will leave technical IDs alone.
        },
        "1abea8bd": {"title": "MONITORIZE CONSTANTEMENTE TUDO O QUE ACONTECE DENTRO E FORA DO SEU CARRO"},
        "5d33d980": {"editor": """<p>SmartCam® regista Vídeo e Áudio 24h por dia dentro e fora do seu Carro.</p><p>A Câmara&nbsp;SmartCam® captura tudo o que acontece ao seu veículo, mesmo quando está desligado, enviando alertas para o telemóvel em caso de perigo, embates, acidentes ou movimentos suspeitos.</p><p>Graças ao Cartão de Memória incluído de 512GB, a câmara regista sem interrupções até 30 dias, fornecendo Vídeo e Áudio para o proteger de Fraudes de Seguros e Indemnizações falsas.</p><p>Além disso, sempre que quiser poderá descarregar facilmente os vídeos e áudios num PC ou no telemóvel e retomar normalmente as gravações.</p>"""},
        "27668d02": {"editor": """<p>A Câmara Dupla Integrada a 360°, cobre todo o veículo com possibilidade de zoom para detetar detalhes, matrículas ou rostos.</p><p>A tecnologia 4K, com objetiva de infravermelhos, garante uma visão nítida e precisa mesmo à noite e a longa distância.</p><p>A câmara Frontal e Traseira pode ser controlada remotamente diretamente do seu Telemóvel com a aplicação gratuita apropriada.</p>"""},
        "47a97986": {"editor": """<p>A revolucionária Câmara&nbsp;SmartCam® é a única no mercado a ter GPS incorporado que funciona sem Internet ou Bluetooth.</p><p>Graças aos Cartões Satélite incorporados, uma vez ligada,&nbsp;SmartCam® liga-se automaticamente à Rede de Satélites e localiza 24h o seu carro e as deslocações.</p><p>Além disso, poderá seguir e ver a posição do seu Carro diretamente no Telemóvel graças à App gratuita incluída.</p>"""},
         "403f0e53": {"editor": """<p>Instalar a SmartCam® é realmente muito simples, e não precisará de ajuda ou de ir à Oficina.</p><p>Basta aplicar a câmara no seu para-brisas, graças às ventosas extra-fixantes, ligar a SmartCam® ao isqueiro com o cabo de alimentação de 5 metros incluído e a gravação iniciará automaticamente.</p>"""},
         "cc0f53b": {"editor": """<p>SmartCam®, quando ligada ao isqueiro, recarrega automaticamente, de modo a garantir-lhe uma gravação contínua com o carro desligado até 3 dias.</p><p>A função de poupança de bateria permite-lhe não consumir a bateria do seu carro, evitando que se descarregue.</p>"""},
         "22d2c611": {"title": "1 SmartCam®<br>+ Memória de 512 GB<br>+ Kit de Instalação Rápida<br>+ Devolução Gratuita<br> POR APENAS " + PRICE_DISCOUNT},
         "72cd6e4d": {"title": "em vez de " + PRICE_FULL},
         "17e447e1": {"title": "Preencha o formulário para encomendar"},
         "68b217a8": {"title": "Se encomendar hoje terá de oferta: <br><br>Cabo de alimentação 5 metros<br>+ Suporte Ventosa Para-brisas<br>+ Memória 512 GB<br>+ Devolução Gratuita"},
         "4cac95be": {"icon_list": [
             {"old_text": "CONTRO INCIDENTI E FRODI ASSICURATIVE", "text": "CONTRA ACIDENTES E FRAUDES DE SEGUROS"},
             {"old_text": "DOPPIA TELECAMERA 4K", "text": "CÂMARA DUPLA 4K"},
             {"old_text": "WIFI-GPS", "text": "WIFI-GPS"},
             {"old_text": "SCHEDA 512 GB", "text": "CARTÃO 512 GB"},
             {"old_text": "BATTERIA A LUNGA DURATA", "text": "BATERIA DE LONGA DURAÇÃO"},
             {"old_text": "INTALLAZIONE RAPIDA", "text": "INSTALAÇÃO RÁPIDA"},
             {"old_text": "Facile da utilizzare", "text": "Fácil de utilizar"},
             {"old_text": "Soddisfatti o Rimborsati", "text": "Satisfeito ou Reembolsado"}
         ]},
         "5e72a626": {"title": "Além disso, encomendando hoje terá de oferta também a Extensão de Garantia Grátis válida por 4 Anos"},
         "725285d9": {"icon_list": [
             {"old_text": "1 Telecamera SmartCam®", "text": "1 Câmara SmartCam®"},
             {"old_text": "Cavo di Alimentazione da 5 metri", "text": "Cabo de Alimentação de 5 metros"},
             {"old_text": "Scheda di memoria 512 GB", "text": "Cartão de memória 512 GB"},
             {"old_text": "Kit di Installazione Rapida", "text": "Kit de Instalação Rápida"},
             {"old_text": "Estensione Garanzia Gratis 4 Anni", "text": "Extensão de Garantia Grátis 4 Anos"},
             {"old_text": "Pagamento sicuro in contanti alla consegna", "text": "Pagamento seguro em dinheiro na entrega"},
             {"old_text": "Spedizione veloce", "text": "Envio rápido"},
             {"old_text": "Formula soddisfatti o rimborsati", "text": "Fórmula satisfeito ou reembolsado"}
         ]},
         "607cb160": {"title": "PREENCHA O FORMULÁRIO ABAIXO PARA ENCOMENDAR SmartCam® POR APENAS " + PRICE_DISCOUNT},
         "6ccac8b0": {"editor": """<p style=\"margin-bottom: 0.9rem; caret-color: #333333; color: #333333; font-size: 12px; text-align: center; text-size-adjust: auto;\"><span style=\"font-size: 10px;\">Este site não faz parte do site do Facebook ou da Facebook Inc. Além disso, este site NÃO é endossado pelo Facebook de forma alguma. Facebook é uma marca comercial da Facebook, Inc</span></p>"""},
         "969aafd": {"editor": """<p>© 2023 Todos os direitos reservados.</p>"""},
         "2eebc162": {"editor": """<p>PRIVACIDADE<span style=\"color: var( --e-global-color-text ); font-weight: var( --e-global-typography-text-font-weight );\">&nbsp;</span>&nbsp;CONTACTOS</p>"""}
    }

    def process_elements(elements):
        for el in elements:
            el_id = el.get('id')
            
            # Check for direct ID match
            if el_id in translations:
                mapping = translations[el_id]
                settings = el.get('settings', {})
                
                # Handle Title
                if 'title' in mapping and 'title' in settings:
                    settings['title'] = mapping['title']
                
                # Handle Editor (HTML content)
                if 'editor' in mapping and 'editor' in settings:
                    settings['editor'] = mapping['editor']
                    
                # Handle Inner Text (Progress bar)
                if 'inner_text' in mapping and 'inner_text' in settings:
                    settings['inner_text'] = mapping['inner_text']
                    
                # Handle Icon List
                if 'icon_list' in mapping and 'icon_list' in settings:
                    original_list = settings['icon_list']
                    map_list = mapping['icon_list']
                    # We iterate through the original list and try to find a match in our mapping
                    for item in original_list:
                        item_text = item.get('text')
                        # find matching translation
                        for m in map_list:
                            if m['old_text'] == item_text:
                                item['text'] = m['text']
                                break
            
            # Recursively process children
            if 'elements' in el:
                process_elements(el['elements'])

    # Start processing from root
    content = data.get('content', [])
    process_elements(content)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False) # separators=(',', ':') can be used if minified, but usually Elementor exports are readable-ish
    
    print(f"Translation complete. Saved to {output_file}")

if __name__ == "__main__":
    translate_to_pt()
