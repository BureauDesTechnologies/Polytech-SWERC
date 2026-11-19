def manacher(s):
    """Time: O(n), Space: O(n)"""
    t = '#' + '#'.join(s) + '#'
    n = len(t)
    p = [0] * n
    c = r = 0
    for i in range(n):
        if i < r:
            p[i] = min(r - i, p[2 * c - i])
        while i - p[i] - 1 >= 0 and i + p[i] + 1 < n and t[i - p[i] - 1] == t[i + p[i] + 1]:
            p[i] += 1
        if i + p[i] > r:
            c, r = i, i + p[i]
    return p


def z_array(s):
    """
    Constructs the Z-array of a string in O(n).
    """

    n = len(s)
    z = [0] * n
    l = r = 0

    if n:
        z[0] = n

    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])

        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1

        if i + z[i] > r:
            l, r = i, i + z[i]

    return z