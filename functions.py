from random import randint
def answer_is_valid(value):
    while value not in "да, нет":
        print("Некорректное значение")
        value = input("Напиши да или нет  ")
    return value


def game_is_valid(value):
    while value not in "отгадывать, загадывать":
        print("Некорректное значение")
        value = input("Ты хочешь отгадывать или загадывать? Напиши здесь -->  ")
    return value

def question_is_valid(value):
    while value not in "больше, меньше, да":
        print("Некорректное значение")
        value = input("Напиши  больше, меньше или да-->  ")
    return value

def num_is_valid(value):
    while not value.isdigit():
        print("Некорректное значение")
        value = input("111Введи число -->  ")
    while int(value) < 1 or int(value) > 100:
        print("Некорректное значение")
        value = input("222Введи число -->  ")
    return int(value)

def checking_number(name):
    rand_num = randint(1, 100)
    num = num_is_valid(input("Введи число -->  "))
    while num != rand_num:
        if rand_num < num:
            print('Слишком много, попробуй еще раз')
            num = num_is_valid(input("Введи число -->  "))
        elif rand_num > num:
            print('Слишком мало, попробуй еще раз')
            num = num_is_valid(input("Введи число -->  "))
    return f'{name}, ты угадал, поздравляю! Спасибо за игру))'

def guess_number(name):
    print(f"{name}, загадай число в диапазоне от 1 до 100")
    left = 1
    right = 100
    print("Я буду писать число, если твое число меньше, чем то, которое я написал, то напиши \"меньше\"\
если оно больше - то напиши \"больше\" а если я угадал, то напиши \"да\"")
    midle = (left + right) // 2
    question = question_is_valid(input(f"Твое число {midle}, я прав? -->  ").lower())
    while question != "да":
        if question == "больше":
            left = midle + 1
            midle = (left + right) // 2
            question = question_is_valid(input(f"Твое число {midle}, я прав? -->  ").lower())
        elif question == "меньше":
            right = midle - 1
            midle = (left + right) // 2
            question = question_is_valid(input(f"Твое число {midle}, я прав? -->  ").lower())
    return f"УРА!!! {name}, спасибо за игру))"

def play(name):
    print("Я могу загадать число от 1 до 100, которое ты никогда не сможешь отгадать\nА еще я смогу отгадать \
число, которое ты загадаешь")
    game = game_is_valid(input("Ты хочешь отгадывать или загадывать? Напиши здесь -->  "))
    if game.lower() == "отгадывать":
        return checking_number(name)
    if game.lower() == "загадывать":
        return guess_number(name)