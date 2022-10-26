from hangman_data import ru_alphabet


class Workers:
    def check_ru(letter):
        return bool(ru_alphabet.intersection(set(letter)))

    def check(letter):
        if len(letter) != 1:
            return True
        if not letter.isalpha():
            return True
        return False

    def hangman_replace(char, string, hangman_word):
        while char.lower() in string:
            letter_pos = string.find(char)
            string = string.replace(char, "_", 1)
            hangman_word = hangman_word[:letter_pos] + char + hangman_word[letter_pos + 1:]
        return [string, hangman_word]
