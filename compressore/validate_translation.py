import json
# import deepdiff # Removed because not installed

def get_structure_keys(data, keys_list, path=""):
    if isinstance(data, dict):
        for key in sorted(data.keys()):
            new_path = f"{path}.{key}" if path else key
            keys_list.append(new_path)
            get_structure_keys(data[key], keys_list, new_path)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            # For lists, we don't strictly enforce length if the content is just text, 
            # but here we expect identical structure, including list lengths, 
            # as we only modified string values.
            new_path = f"{path}[{i}]"
            # keys_list.append(new_path) # Too noisy for lists?
            get_structure_keys(item, keys_list, new_path)

def main():
    with open('compressore-hu.json', 'r', encoding='utf-8') as f:
        src = json.load(f)
    with open('compressore-cz.json', 'r', encoding='utf-8') as f:
        dst = json.load(f)

    # 1. Structure Check
    src_keys = []
    dst_keys = []
    get_structure_keys(src, src_keys)
    get_structure_keys(dst, dst_keys)

    if src_keys != dst_keys:
        print("ERROR: JSON structure mismatch!")
        print("Diff:", set(src_keys) ^ set(dst_keys))
        exit(1)
    else:
        print("SUCCESS: JSON structure matches.")

    # 2. Price Check
    with open('compressore-cz.json', 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "1248" in content and "2600" in content and "Kč" in content:
        print("SUCCESS: Prices and currency found.")
    else:
        print("ERROR: Prices or currency missing!")
        if "1248" not in content: print("- Missing 1248")
        if "2600" not in content: print("- Missing 2600")
        if "Kč" not in content: print("- Missing Kč")
        exit(1)

    print("Validation passed.")

if __name__ == "__main__":
    main()
