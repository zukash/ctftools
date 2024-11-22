from sage.all import *


def small_roots_mod_p(f, x_bit, n_bit, p_bit):
    # ref. https://doc.sagemath.org/html/en/reference/polynomial_rings/sage/rings/polynomial/polynomial_modn_dense_ntl.html#sage.rings.polynomial.polynomial_modn_dense_ntl.small_roots
    f = f.monic()
    # p >= n**beta
    # FIXME: パラメータの調整
    beta = (p_bit / n_bit) * 0.8
    # FIXME: epsilon の活用
    return f.small_roots(X=2**x_bit, beta=beta)
