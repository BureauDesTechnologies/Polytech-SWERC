def rendre_monnaie(montant: int, valeurs: list[int]) -> list[int]:
    """
    Algorithme glouton pour rendre la monnaie.

    Args:
        montant: Le montant à rendre
        valeurs: Les valeurs des pièces (triées par ordre décroissant)

    Returns:
        Liste d'entiers représentant les pièces utilisées,
        ou None si impossible
    """
    reste = montant
    solution = []

    for v in valeurs:
        q = reste // v  # Nombre de pièces de valeur v

        for _ in range(q):
            solution.append(v)

        reste -= q * v

    if reste != 0:
        raise RuntimeError("Impossible de trouver une solution par stratégie gloutonne")

    return solution
