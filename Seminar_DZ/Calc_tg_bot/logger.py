# Логирование в файл

from datetime import datetime

def log_to_file(a, b, operation, result):
    with open('log.csv', 'a') as file:
        file.write(f'{datetime.today()}; {a}; {operation}; {b}; {result}; \n')
