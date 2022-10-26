import json

def get_data():
    with open("data_file.json", "r", encoding='utf-8') as f:    # открыли файл с данными
        text = json.load(f) # поместили всё в переменную
        return text

'''
def get_push_data():
    with open("data_file.json", "w", encoding='utf-8') as f:
        json.dump("initial", f)
'''       
