from random import randint
from functions import *
print("Привет друг!!\nКак тебя зовут?")
name = input("Введи свое имя  ")
print(f"{name}, хочешь поиграть со мной в игру \"Числовая угадайка\"")
answer = answer_is_valid(input("Напиши да или нет  "))
while answer.lower() == "да":
    print(play(name))
    print("Хочешь сыграть еще?")
    answer = answer_is_valid(input("Напиши да или нет  "))
print("Возвращайся, я буду ждать))")


