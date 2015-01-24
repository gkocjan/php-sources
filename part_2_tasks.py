from string import ascii_lowercase


def generate_ascii_list():
    return [x for x in ascii_lowercase]


def generate_ascii_codes_map():
    return {x: ord(x) for x in ascii_lowercase}


def filter_word_list(words_list):
    return [x for x in words_list if len(x) < 5]


def generate_squers(limit=50):
    return [x*x for x in range(1, limit+1)]

def generate_squers_map(limit=50):
    return map(lambda x: x*x, range(1, limit+1))

if __name__ == '__main__':
    print generate_ascii_list()
    print generate_ascii_codes_map()
    print filter_word_list(['ala', 'maaaaaaaaa', 'kota'])
    
    print generate_squers()
    print generate_squers_map()
    