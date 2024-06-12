from intervals import overlapping_intervals


def test_overlapping_intervals():
    assert overlapping_intervals((1, 5), (3, 6))
    assert not overlapping_intervals((2, 5), (7, 10))
    assert not overlapping_intervals((6, 5), (7, 10))
    assert not overlapping_intervals((2, 5), (7, 3))
    assert not overlapping_intervals((8, 5), (7, 1))
    assert overlapping_intervals((2, 7), (7, 10))