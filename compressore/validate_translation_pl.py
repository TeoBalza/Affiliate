import json

def get_structure_keys(data, keys_list, path=""):
    if isinstance(data, dict):
        for key in sorted(data.keys()):
            new_path = f"{path}.{key}" if path else key
            keys_list.append(new_path)
            get_structure_keys(data[key], keys_list, new_path)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            new_path = f"{path}[{i}]"
            get_structure_keys(item, keys_list, new_path)

def main():
    try:
        with open('compressore-hu.json', 'r', encoding='utf-8') as f:
            src = json.load(f)
        with open('compressore-pl.json', 'r', encoding='utf-8') as f:
            dst = json.load(f)
    except FileNotFoundError as e:
        print(f"ERROR: Files not found: {e}")
        exit(1)

    # 1. Structure Check
    src_keys = []
    dst_keys = []
    get_structure_keys(src, src_keys)
    get_structure_keys(dst, dst_keys)

    if src_keys != dst_keys:
        print("ERROR: JSON structure mismatch!")
        # Optional: Print diff if needed
        # print("Diff:", set(src_keys) ^ set(dst_keys))
        exit(1)
    else:
        print("SUCCESS: JSON structure matches.")

    # 2. Price and Currency Check
    with open('compressore-pl.json', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Prices: 219, 450. Currency: zł
    errors = []
    if "219" not in content: errors.append("Missing 219")
    if "450" not in content: errors.append("Missing 450")
    if "zł" not in content: errors.append("Missing zł")
    
    if errors:
        print("ERROR: Price or currency validation failed!")
        for err in errors:
            print(f"- {err}")
        exit(1)
    else:
        print("SUCCESS: Prices and currency found.")

    print("Validation passed.")

if __name__ == "__main__":
    main()
