from .point import Point


def multiply(p, n, N, A, P):
    """
    Fast way to multily point and scalar in elliptic curves

    :param p: First Point to mutiply
    :param n: Scalar to mutiply
    :param N: Order of the elliptic curve
    :param P: Prime number in the module of the equation Y^2 = X^3 + A*X + B (mod p)
    :param A: Coefficient of the first-order term of the equation Y^2 = X^3 + A*X + B (mod p)
    :return: Point that represents the sum of First and Second Point
    """
    return fromJacobian(jacobianMultiply(toJacobian(p), n, N, A, P), P)


def add(p, q, A, P):
    """
    Fast way to add two points in elliptic curves

    :param p: First Point you want to add
    :param q: Second Point you want to add
    :param P: Prime number in the module of the equation Y^2 = X^3 + A*X + B (mod p)
    :param A: Coefficient of the first-order term of the equation Y^2 = X^3 + A*X + B (mod p)
    :return: Point that represents the sum of First and Second Point
    """
    return fromJacobian(jacobianAdd(toJacobian(p), toJacobian(q), A, P), P)


def inv(x, n):
    """
    Extended Euclidean Algorithm. It's the 'division' in elliptic curves

    :param x: Divisor
    :param n: Mod for division
    :return: Value representing the division
    """
    if x == 0:
        return 0
    lm, hm = 1, 0
    low, high = x % n, n
    while low > 1:
        r = high//low
        nm, new = hm-lm*r, high-low*r
        lm, low, hm, high = nm, new, lm, low
    return lm % n


def toJacobian(p):
    """
    Convert point to Jacobian coordinates

    :param p: First Point you want to add
    :return: Point in Jacobian coordinates
    """
    return Point(p.x, p.y, 1)


def fromJacobian(p, P):
    """
    Convert point back from Jacobian coordinates

    :param p: First Point you want to add
    :param P: Prime number in the module of the equation Y^2 = X^3 + A*X + B (mod p)
    :return: Point in default coordinates
    """
    z = inv(p.z, P)
    return Point((p.x * z ** 2) % P, (p.y * z ** 3) % P)


def jacobianDouble(p, A, P):
    """
    Double a point in elliptic curves

    :param p: Point you want to double
    :param P: Prime number in the module of the equation Y^2 = X^3 + A*X + B (mod p)
    :param A: Coefficient of the first-order term of the equation Y^2 = X^3 + A*X + B (mod p)
    :return: Point that represents the sum of First and Second Point
    """
    if not p.y:
        return Point(0, 0, 0)
    ysq = (p.y ** 2) % P
    S = (4 * p.x * ysq) % P
    M = (3 * p.x ** 2 + A * p.z ** 4) % P
    nx = (M**2 - 2 * S) % P
    ny = (M * (S - nx) - 8 * ysq ** 2) % P
    nz = (2 * p.y * p.z) % P
    return Point(nx, ny, nz)


def jacobianAdd(p, q, A, P):
    """
    Add two points in elliptic curves

    :param p: First Point you want to add
    :param q: Second Point you want to add
    :param P: Prime number in the module of the equation Y^2 = X^3 + A*X + B (mod p)
    :param A: Coefficient of the first-order term of the equation Y^2 = X^3 + A*X + B (mod p)
    :return: Point that represents the sum of First and Second Point
    """
    if not p.y:
        return Point(q.x, q.y, q.z)
    if not q.y:
        return Point(p.x, p.y, p.z)
    U1 = (p.x * q.z ** 2) % P
    U2 = (q.x * p.z ** 2) % P
    S1 = (p.y * q.z ** 3) % P
    S2 = (q.y * p.z ** 3) % P
    if U1 == U2:
        if S1 != S2:
            return Point(0, 0, 1)
        return jacobianDouble(p, A, P)
    H = U2 - U1
    R = S2 - S1
    H2 = (H * H) % P
    H3 = (H * H2) % P
    U1H2 = (U1 * H2) % P
    nx = (R ** 2 - H3 - 2 * U1H2) % P
    ny = (R * (U1H2 - nx) - S1 * H3) % P
    nz = (H * p.z * q.z) % P
    return Point(nx, ny, nz)


def jacobianMultiply(p, n, N, A, P):
    """
    Multily point and scalar in elliptic curves

    :param p: First Point to mutiply
    :param n: Scalar to mutiply
    :param N: Order of the elliptic curve
    :param P: Prime number in the module of the equation Y^2 = X^3 + A*X + B (mod p)
    :param A: Coefficient of the first-order term of the equation Y^2 = X^3 + A*X + B (mod p)
    :return: Point that represents the sum of First and Second Point
    """
    if p.y == 0 or n == 0:
        return Point(0, 0, 1)
    if n == 1:
        return p
    if n < 0 or n >= N:
        return jacobianMultiply(p, n % N, N, A, P)
    if (n % 2) == 0:
        return jacobianDouble(jacobianMultiply(p, n // 2, N, A, P), A, P)
    if (n % 2) == 1:
        return jacobianAdd(jacobianDouble(jacobianMultiply(p, n // 2, N, A, P), A, P), p, A, P)
