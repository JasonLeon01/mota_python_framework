import json

def load_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        json_data = file.read()
    return json.loads(json_data)
