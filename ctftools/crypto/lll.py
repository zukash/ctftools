from sage.all import *


def subset_sum_problem(S, t, verbose=False):
    """
    # ref. https://kmyk.github.io/blog/writeups/ctf-2015-plaidctf-2015-lazy/
    # ref. https://qiita.com/kusano_k/items/5509bff6e426e5043591
    """
    n = len(S)
    M = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        M[i][i] = 2
        M[i][-1] = S[i] * n
        M[-1][i] = 1
    M[-1][-1] = t * n

    res = matrix(M).LLL()

    if verbose:
        return res
    else:
        res = res[0][:-1]
        assert all(x in [-1, 1] for x in res)
        # -1 -> 1, 1 -> 0
        return [(1 - x) // 2 for x in res]
