import random


def square_generator():
    for length in range(200, 10001):
        for width in range(500, 100001):
            yield length * width


NOTES = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']


def note_list_generator(n, rows):
    for _ in range(rows):
        yield [random.choice(NOTES) for _ in range(n)]


def common_coins(f, g):

    fs = set(f)
    gs = set(g)

    common = fs & gs

    return list(filter(lambda x: x % 2 == 0, common))
