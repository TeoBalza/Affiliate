import json
import sys

ORIGINAL_FILE = '/Users/matteo/Documents/GitHub/forno/compressore/compressore-hu.json'
TRANSLATED_FILE = '/Users/matteo/Documents/GitHub/forno/compressore/compressore-sk.json'

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def compare_structure(obj1, obj2, path=""):
    if type(obj1) != type(obj2):
        print(f"Type mismatch at {path}: {type(obj1)} vs {type(obj2)}")
        return False
    
    if isinstance(obj1, dict):
        if set(obj1.keys()) != set(obj2.keys()):
            print(f"Key mismatch at {path}: {set(obj1.keys())} vs {set(obj2.keys())}")
            return False
        for key in obj1:
            if not compare_structure(obj1[key], obj2[key], path + f".{key}"):
                return False
    elif isinstance(obj1, list):
        if len(obj1) != len(obj2):
            print(f"List length mismatch at {path}: {len(obj1)} vs {len(obj2)}")
            return False
        for i in range(len(obj1)):
            if not compare_structure(obj1[i], obj2[i], path + f"[{i}]"):
                return False
    return True

def validate_content(data):
    # Check for specific expected Slovak strings
    content_str = json.dumps(data, ensure_ascii=False)
    
    required_strings = [
        "NOVÝ, VÝNIMOČNÝ AirForce One 2025",
        "Profesionálny vzduchový kompresor",
        "49 €",
        "100 €", 
        "Vyplňte formulár pre objednávku",
        "OCHRANA SÚKROMIA | KONTAKT"
    ]
    
    missing = []
    for s in required_strings:
        if s not in content_str:
            missing.append(s)
            
    if missing:
        print(f"Missing translated strings: {missing}")
        return False
        
    # Check for presence of Hungarian strings that should have been removed
    forbidden_strings = [
        "AZ ÚJ, KIVÉTELES AirForce One 2025",
        "A Professzionális Légkompresszor",
        "CSAK 19999 Ft",
        "74663 Ft helyett"
    ]
    
    present_forbidden = []
    for s in forbidden_strings:
        if s in content_str:
            present_forbidden.append(s)
            
    if present_forbidden:
        print(f"Forbidden strings still present: {present_forbidden}")
        return False
        
    return True

def main():
    try:
        orig = load_json(ORIGINAL_FILE)
        trans = load_json(TRANSLATED_FILE)
        
        print("Validating structure...")
        if not compare_structure(orig, trans):
            print("Structure validation FAILED")
            sys.exit(1)
        print("Structure validation PASSED")
        
        print("Validating content...")
        if not validate_content(trans):
            print("Content validation FAILED")
            sys.exit(1)
        print("Content validation PASSED")
        
    except Exception as e:
        print(f"Validation error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
