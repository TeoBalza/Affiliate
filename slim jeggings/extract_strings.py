import json
import os

KEYWORDS = ['title', 'editor', 'text', 'inner_text', 'placeholder', 'button_text', 'heading_title']

def extract_strings(data, strings_set):
    if isinstance(data, dict):
        for k, v in data.items():
            if k in KEYWORDS and isinstance(v, str) and v.strip():
                strings_set.add(v)
            extract_strings(v, strings_set)
    elif isinstance(data, list):
        for item in data:
            extract_strings(item, strings_set)

def main():
    input_path = 'slim-jeggings-it.json'
    output_path = 'source_strings.json'
    
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found.")
        return

    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    strings_set = set()
    extract_strings(data, strings_set)

    # Convert to list and sort for stable output
    strings_list = sorted(list(strings_set))
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(strings_list, f, indent=4, ensure_ascii=False)
    
    print(f"Extracted {len(strings_list)} unique strings to {output_path}")

if __name__ == "__main__":
    main()
