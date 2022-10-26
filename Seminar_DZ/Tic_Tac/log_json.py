
import json
from game import *

def logger():
    with open("data_file.json", "w", encoding='utf-8') as write_file:
        json.dump(data, write_file)
