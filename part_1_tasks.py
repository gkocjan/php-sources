from string import ascii_lowercase


def print_chars_in_new_line():
    for current_char in ascii_lowercase:
        print current_char


def print_every_second_char():
    for current_char in ascii_lowercase[::2]:
        print current_char

def check_palindrom(word):
    print 'Word "{}" is palindrom? {}!!'.format(
        word,
        'YES :)' if  word == word[::-1] else 'NO :('
    )


def filter_alphabet_chars(word):
    def check_char(current_char):
        return current_char.lower() in ascii_lowercase

    print filter(check_char, word)


def filter_by_words_lenght(sentense, max_len):
    def check_len(word):
        return len(word) <= max_len

    print ' '.join(
        filter(check_len, sentense.split(' '))
    )

if __name__ == '__main__':
    print_chars_in_new_line()
    print_every_second_char()
    check_palindrom('anna')
    check_palindrom('kasia')
    filter_alphabet_chars('Print only.. ! // alphabet ## chars')
    filter_by_words_lenght('This it veryyyyy looooong test', 4)
