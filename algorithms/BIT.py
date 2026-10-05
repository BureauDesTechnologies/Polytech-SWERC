def query(bit, index):
    """
    We assume that the index is 0-based.
    Returns the sum over [0, index].
    """
    tot = 0
    index += 1
    while index > 0:
        tot += bit[index]
        index -= index & (-index)
    return tot


def update(bit, index, delta):
    """
    We assume that the index is 0-based.
    Updates ``bit`` at ``index``, by adding ``delta`` to it.
    """
    index += 1
    while index < len(bit):
        bit[index] += delta
        index += index & (-index)

def range_query(bit, i1, i2):
    """
    Range query on interval [i1, i2].
    We assume that the indices are 0-based.
    """
    return query(bit, i2) - query(bit, i1 - 1)