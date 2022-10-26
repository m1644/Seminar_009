
import random
import ex

greeting = ('Здравствуйте! Вас приветствует игра "2021 конфета!" '
            'Основные правила игры: '
            'Договариваемся сколько будет конфет на кону, '
            'за один ход мы можем взять не более определённого количества, '
            'о котором мы договоримся тоже. Победитель забирает ВСЁ) '
            'Погнали...!')

messages = ['Ваша очередь брать конфеты', 'возьмите конфеты', 
            'сколько конфет возьмёте?', 'берите, пожалуйста', 'Ваш ход']

def play_game(data, m, players, messages):
    count = 0
    if data%10 == 1 and 9 > data > 10: letter = 'а'
    elif 1 < data%10 < 5 and 9 > data > 10: letter = 'ы'
    else: letter = ''
    while data > 0:
        print(f'{players[count%2]}, {random.choice(messages)}')
        move = int(input())
        if move > data or move > m:
            print(f'Вы взяли много, можно взять не более {m} конфет{letter}, у нас всего {data} конфет{letter}!')
            attempt = 3
            while attempt > 0:
                if data >= move <= m:
                    break
                print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                move = int(input())
                attempt -=1
            else: 
                return print(f'Очень жаль, Вы истратили 3 попытки( Game over!')
        data = data - move
        if data > 0: print(f'Осталось {data} конфет{letter}')
        else: print('Конфеты закончились.')
        count +=1
    return players[not count%2]

print(greeting)

player1 = input('Давайте знакомится:)\nИгрок №1, как Вас зовут?\n')
player2 = input('Игрок №2, и Вы представьтесь, пожалуйста\n')
players = [player1, player2]

data = ex.get_data()["initial"]

#data = int(input('Сколько конфет на кону? '))
m = int(input('Сколько максимально будем брать конфет за один ход? '))
winer = play_game(data, m, players, messages)

if not winer:
    print('У нас нет победителя.')
else: print(f'Поздравляю! Победил {winer}! Ему достаются все конфеты!')

#data = ex.get_push_data()
