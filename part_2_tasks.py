from string import ascii_lowercase


def generate_ascii_list():
    return [x for x in ascii_lowercase]


def generate_ascii_codes_map():
    return {x: ord(x) for x in ascii_lowercase}


def filter_word_list(words_list):
    return [x for x in words_list if len(x) < 5]


if __name__ == '__main__':
    print generate_ascii_list()
    print generate_ascii_codes_map()
    print filter_word_list(['ala', 'maaaaaaaaa', 'kota'])