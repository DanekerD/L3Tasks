def int_func():
        for word in input("Type spaced latin lowercase words:\n").split():
            chars = 0
            for char in word:
                if 97 <= ord(char) <= 122:
                    chars += 1
            print(word.title()) if chars == len(word) else f"{word} - Oops! Only lowercase latin letters!"


int_func()

