from app.logic import (
    square_generator,
    note_list_generator,
    common_coins
)

def test_square_generator():

    gen = square_generator()

    first = next(gen)

    assert first == 200 * 500


def test_notes():

    gen = note_list_generator(5, 3)

    data = list(gen)

    assert len(data) == 3
    assert len(data[0]) == 5


def test_common_coins():

    f = [1, 2, 3, 4, 6]
    g = [2, 4, 5, 6, 7]

    result = common_coins(f, g)

    assert sorted(result) == [2, 4, 6]
