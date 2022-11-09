# Создайте программу для игры в ""Крестики-нолики"" # при помощи виртуального окружения 
# и PIP( можно любую задачу, главное файл с библиотекой чтобы был в формате тхт).

import random
import os
import time

def clear():
	os.system('cls')

def symbol(n):
    if n == 1: return '◯' 
    elif n == 2: return '✖'

def showGame(movesList, player_sign_choice):
    nums = list(range(1, 10))
    for i in range(0, 9):
        if movesList[i] == 1: nums[i] = symbol(1)
        elif movesList[i] == 2: nums[i] = symbol(2)
        else: nums[i] = i + 1
    
    clear()
    print("\t\t   ------------------------------------")
    print("\t\t\t    КРЕСТИКИ -- НОЛИКИ")
    print("\t\t   ------------------------------------")
    print("\t\t\t   ____________________")
    print("\t\t\t  |      |      |      | ")
    print("\t\t\t  |  {}   |  {}   |  {}   |".format(nums[0], nums[1], nums[2]))
    print("\t\t\t  |______|______|______|")
    print("\t\t\t  |      |      |      | ")
    print("\t\t\t  |  {}   |  {}   |  {}   |".format(nums[3], nums[4], nums[5]))
    print("\t\t\t  |______|______|______|")
    print("\t\t\t  |      |      |      | ")
    print("\t\t\t  |  {}   |  {}   |  {}   |".format(nums[6], nums[7], nums[8]))
    print("\t\t\t  |______|______|______|")
    print("\t\t   ------------------------------------")
    print("\t\t\t     Вы играете за {}".format(symbol(player_sign_choice)))
    print("\t\t   ------------------------------------")
    print()

def playerChoise():
    player_sign_choice = 0
    clear()
    while player_sign_choice > 2 or player_sign_choice < 1:
        try:
            print("\t\t   ------------------------------------")
            print("\t\t\t    КРЕСТИКИ -- НОЛИКИ")
            print("\t\t   ------------------------------------")
            print("\t\t\t      1 - ◯     2 - ✖")
            player_sign_choice = int(input("Нажмите '1', если хотите играть 'ноликом', или '2', если хотите играть 'крестиком' "))
        except ValueError:
            clear()
            print("\t\t\t Некорректный ввод. Введите число.")
            time.sleep(1)
        if 0 < player_sign_choice < 3:
            if player_sign_choice == 2:
                bot_sign_choice = 1
            else:
                bot_sign_choice = 2
            rand = random.randrange(0, 2)
            # print("\t\t Первый ходит - {} ".format(symbol(2)))
            return player_sign_choice, bot_sign_choice, bool(rand)
        else:
            clear()
            print("\t\t\t Введите число от 1 до 2.")
            time.sleep(0.5)

def mover(player_sign_choice, movesList):
    valid = False
    while not valid:
        try:
            move = int(input("\t\t\t       Ваш ход? = "))
        except:
            print("\t\t\t    Вы ввели не число!")
            continue
        if 0 < move < 10:
            if (movesList[move - 1] == 0):
                movesList[move - 1] = player_sign_choice
                valid = True
            else:
                print ("Эта клетка уже занята")
        else:
            print("\t\tНекорректный ввод. Введите число от 1 до 9.")

def check(movesList):
    coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for i in coord:
        if movesList[i[0]] == movesList[i[1]] == movesList[i[2]] and movesList[i[0]] != 0:
            return movesList[i[0]]
    return False

def win(movesList, s):
    res = False
    for i in range(9):
        if movesList[i] == 0:
            movesList[i] = s
            if check(movesList) == s: res = i
            movesList[i] = 0
    return res

def computer_move(movesList, bot_sign_choice, player_sign_choice):
    time.sleep(0.3)
    move = -1
    if win(movesList, bot_sign_choice):
        move = win(movesList, bot_sign_choice)
    elif win(movesList, player_sign_choice):
        move = win(movesList, player_sign_choice)
    else:
        while move == -1:
            x = random.randrange(9)
            if movesList[x] == 0:
                move = x
    movesList[move] = bot_sign_choice

def game():

    movesList = [0 for i in range(1, 10)]
    player_sign_choice, bot_sign_choice, playerMove = playerChoise()
    play = True
    count = 0
    showGame(movesList, player_sign_choice)

    while count < 9:
        if playerMove:
            mover(player_sign_choice, movesList)
            showGame(movesList, player_sign_choice)
            playerMove = False
        else:
            computer_move(movesList, bot_sign_choice, player_sign_choice)
            showGame(movesList, player_sign_choice)
            playerMove = True
        if check(movesList): break
        count += 1
        
    if check(movesList):
        if check(movesList) == player_sign_choice:
            showGame(movesList, player_sign_choice)
            print("\t\t\t       Вы выиграли!")
            print("")
        else:	
            showGame(movesList, player_sign_choice)
            print("\t\t     Вы проиграли! Попробуйте еще раз")
            print("")
    if count == 9: 
        showGame(movesList, player_sign_choice)
        print("\t\t\t\t  Ничья!")
        print("")
game()