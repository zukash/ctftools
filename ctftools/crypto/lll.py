from sage.all import *


def subset_sum_problem(S, t, verbose=False):
    """
    ref. https://kmyk.github.io/blog/writeups/ctf-2015-plaidctf-2015-lazy/
    ref. https://qiita.com/kusano_k/items/5509bff6e426e5043591
    """
    n = len(S)
    XX = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        XX[i][i] = 2
        XX[i][-1] = S[i] * n
        XX[-1][i] = 1
    XX[-1][-1] = t * n

    YY = matrix(XX).LLL()

    if verbose:
        return YY
    else:
        for Y in YY:
            Y = Y[:-1]
            if all(y in [-1, 1] for y in Y):
                # -1 -> 1, 1 -> 0
                return [(1 - x) // 2 for x in Y]
        return None
