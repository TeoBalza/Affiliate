import json
import re

def extract_strings(data, keys_to_extract, strings):
    if isinstance(data, dict):
        for key, value in data.items():
            if key in keys_to_extract and isinstance(value, str) and value.strip():
                strings.add(value)
            
            # Recursive call
            extract_strings(value, keys_to_extract, strings)
    elif isinstance(data, list):
        for item in data:
            extract_strings(item, keys_to_extract, strings)

def main():
    with open('compressore-hu.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    keys = {'title', 'editor', 'text', 'inner_text', 'placeholder', 'button_text', 'link_text', 'previous_text', 'next_text'}
    found_strings = set()
    
    extract_strings(data, keys, found_strings)
    
    print("--- START STRINGS ---")
    for s in sorted(found_strings):
        print(s)
    print("--- END STRINGS ---")

if __name__ == "__main__":
    main()
