import json
import os
import sys

def get_structure_skeleton(data):
    if isinstance(data, dict):
        return {k: get_structure_skeleton(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [get_structure_skeleton(item) for item in data]
    else:
        return "VALUE"

def compare_structures(data1, data2, path=""):
    if type(data1) != type(data2):
        print(f"Type mismatch at {path}: {type(data1)} vs {type(data2)}")
        return False
    
    if isinstance(data1, dict):
        keys1 = set(data1.keys())
        keys2 = set(data2.keys())
        if keys1 != keys2:
            print(f"Key mismatch at {path}: {keys1.symmetric_difference(keys2)}")
            return False
        for k in keys1:
            if not compare_structures(data1[k], data2[k], path + f".{k}"):
                return False
    elif isinstance(data1, list):
        if len(data1) != len(data2):
            print(f"List length mismatch at {path}: {len(data1)} vs {len(data2)}")
            return False
        for i, (item1, item2) in enumerate(zip(data1, data2)):
            if not compare_structures(item1, item2, path + f"[{i}]"):
                return False
    
    return True

def main():
    file1 = 'slim-jeggings-it.json'
    file2 = 'slim-jeggings-si.json'
    
    with open(file1, 'r', encoding='utf-8') as f:
        data1 = json.load(f)
    with open(file2, 'r', encoding='utf-8') as f:
        data2 = json.load(f)

    if compare_structures(data1, data2):
        print("Validation Successful: JSON structures are identical.")
    else:
        print("Validation Failed: JSON structures differ.")

if __name__ == "__main__":
    main()
