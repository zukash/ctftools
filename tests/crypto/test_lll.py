from ctftools.crypto import lll


def test_subset_sum_problem():
    S = [123456789, 234567890, 345678901, 456789012, 567890123]
    t = S[1] + S[3] + S[4]
    I = lll.subset_sum_problem(S, t)
    assert I == [0, 1, 0, 1, 1]
