# Функция экспорта данных

def read_all_file1():
    with open('Seminar_DZ\phone_directory1.csv', 'r') as file:
        for line in file:
            print(line)

def read_all_file2():
    with open('Seminar_DZ\phone_directory2.csv', 'r') as file:
        for line in file:
            print(line)