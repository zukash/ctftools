from sage.all import *
from itertools import product


def bit_extension_search(F, e):
    """
    F: list of functions
    e: number of bits
    """
    n = F[0].__code__.co_argcount
    XX = [tuple(0 for _ in range(n))]
    for k in range(e):
        f_all = lambda X: all(Zmod(1 << (k + 1))(f(*X)) == 0 for f in F)
        # extend and filter
        XX = [
            nX
            for X in XX
            for B in product([0, 1], repeat=n)
            if f_all(nX := tuple(x | (b << k) for x, b in zip(X, B)))
        ]
    return XX
