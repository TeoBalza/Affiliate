import json
import os
import sys

# We target the same keys as extraction to be safe, though value matching is primary.
KEYWORDS = ['title', 'editor', 'text', 'inner_text', 'placeholder', 'button_text', 'heading_title']

def apply_translations(data, translations_map):
    count = 0
    if isinstance(data, dict):
        for k, v in data.items():
            if k in KEYWORDS and isinstance(v, str) and v in translations_map:
                data[k] = translations_map[v]
                count += 1
            else:
                count += apply_translations(v, translations_map)
    elif isinstance(data, list):
        for item in data:
            count += apply_translations(item, translations_map)
    return count

def main():
    input_path = 'slim-jeggings-it.json'
    strings_path = 'translated_strings.json'
    output_path = 'slim-jeggings-si.json'
    
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found.")
        return
    if not os.path.exists(strings_path):
        print(f"Error: {strings_path} not found.")
        return

    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    with open(strings_path, 'r', encoding='utf-8') as f:
        translations = json.load(f)

    print(f"Loaded {len(translations)} translations.")

    replaced_count = apply_translations(data, translations)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=None, separators=(',', ':')) 
        # Elementor exports often use compact JSON (separators=(',', ':')). 
        # But actually, the input file had "content": [...] appearing somewhat formatted? 
        # Let's check the input format more closely. 
        # The view_file output showed everything in one line? 
        # "1: {"content":[{"id":"77eaebbd","settings":..."
        # Yes, it is minified. separators=(',', ':') produces minified JSON.

    print(f"Applied {replaced_count} translations.")
    print(f"Saved to {output_path}")

if __name__ == "__main__":
    main()
