import json
import sys

original_path = '/Users/matteo/Documents/GitHub/forno/dashcam/dashcam-it.json'
translated_path = '/Users/matteo/Documents/GitHub/forno/dashcam/dashcam-pt.json'

with open(original_path, 'r') as f:
    orig_data = json.load(f)

with open(translated_path, 'r') as f:
    trans_data = json.load(f)

def get_keys(node, path=""):
    keys = []
    if isinstance(node, dict):
        for k, v in node.items():
            current_path = f"{path}.{k}" if path else k
            keys.append(current_path)
            keys.extend(get_keys(v, current_path))
    elif isinstance(node, list):
        for i, item in enumerate(node):
            current_path = f"{path}[{i}]"
            keys.extend(get_keys(item, current_path))
    return keys

orig_keys = set(get_keys(orig_data))
trans_keys = set(get_keys(trans_data))

if orig_keys == trans_keys:
    print("Structure validation PASSED: Keys match exactly.")
else:
    print("Structure validation FAILED.")
    diff = orig_keys.symmetric_difference(trans_keys)
    print(f"Differences: {diff}")
    sys.exit(1)

# Check for price and specific translations
content_str = json.dumps(trans_data, ensure_ascii=False)
if "57€" in content_str and "130€" in content_str:
    print("Price validation PASSED.")
else:
    print("Price validation FAILED: '57€' or '130€' not found.")
    # Check what is there
    if "57" in content_str: print("Found 57")
    if "130" in content_str: print("Found 130")

