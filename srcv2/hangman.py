from random import choice
import hangman_data
from Checkers import Workers

global hangman_show_word
global try_counts
global word
global length
global guessed_letters
global guessed_word
print("Давай сыграем в игру Виселица. Твоей задачей будет отгадать слово, которое я загадал")
max_try_count = len(hangman_data.HANGMAN) - 1


def main():
    global hangman_show_word
    global try_counts
    global word
    global length
    global guessed_letters
    global guessed_word
    guessed_word = choice(hangman_data.WORDS)
    word = guessed_word.lower()
    length = len(guessed_word)
    hangman_show_word = length * "_"
    guessed_letters = []
    try_counts = 0


def wanna_play():
    player_answer = input(hangman_data.rerun_game).lower()
    while player_answer not in hangman_data.answer:
        player_answer = input(hangman_data.rerun_game).lower()
    if player_answer in hangman_data.pos_answer:
        main()
        hangman()
    else:
        print("Возвращайся, когда захочешь сыграть")
        exit()


def hangman():
    global try_counts
    global hangman_show_word
    global word
    global guessed_letters
    global length
    global guessed_word
    global max_try_count
    player_letter = input("Слово " + hangman_show_word + "\nВведи букву русского алфавита: \n")
    if Workers.check(player_letter) or not Workers.check_ru(player_letter):
        print("Этот символ не подходит, напиши букву расского алфавита\n")
        hangman()

    elif player_letter.lower() in word:
        guessed_letters.extend([player_letter])
        print(guessed_letters)
        [word, hangman_show_word] = Workers.hangman_replace(player_letter, word, hangman_show_word)
        print("Да, эта буква есть в слове!\n")
        if word == length * "_":
            print("Ты угадал слово")
            wanna_play()
            hangman()
        hangman()

    elif player_letter in guessed_letters:
        print("Эта буква уже была. Введи другую\n")
        hangman()

    else:
        try_counts += 1
        if try_counts == max_try_count:
            print(hangman_data.HANGMAN[try_counts] + "\n" + "Ты не угадал слово\n" + "Правильное слово: " + guessed_word)
            wanna_play()

        else:
            print(hangman_data.HANGMAN[try_counts] + "\n" + "Ты не угадал слово\n" + str(max_try_count - try_counts) +
                  " Попыток не осталось\n")
            guessed_letters.extend([player_letter])
            hangman()


main()

hangman()
