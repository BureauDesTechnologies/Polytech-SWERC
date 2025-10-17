from dataclasses import dataclass

@dataclass
class Pos:
    """Classe représentant une position sur le plateau"""
    x: int
    y: int


def position_reine_est_valide(pos: Pos, disposition: list[Pos], nb_reines: int) -> bool:
    """
    Vérifie si la position d'une reine est valide.

    Args:
        pos: La position à vérifier
        disposition: La disposition des autres reines sur le plateau
        nb_reines: Le nombre de reines sur le plateau

    Returns:
        True si la position est valide, False sinon
    """
    for i in range(nb_reines):
        x = disposition[i].x
        y = disposition[i].y

        if (
            y == pos.y                      # même colonne
            or (x - y) == (pos.x - pos.y)   # même diagonale /
            or (x + y) == (pos.x + pos.y)   # même diagonale \
            # il n'y a jamais plusieurs reines sur la même ligne donc pas besoin de le vérifier
        ):
            return False

    return True


def poser_n_reines(N: int) -> list[Pos]:
    """
    Algorithme de backtracking pour résoudre le problème des N reines.

    Args:
        N: Le nombre de reines à placer sur le plateau NxN

    Returns:
        Une liste de positions (solution trouvée) ou None si aucune solution
    """
    if N == 0:
        return []

    solution = [None] * N # Création d'une liste de N éléments

    ligne = 0
    col = 0

    while ligne >= 0:
        trouve = False

        # Essayer de placer une reine sur la ligne courante
        while col < N and not trouve:
            candidate = Pos(ligne, col)

            if position_reine_est_valide(candidate, solution, ligne):
                solution[ligne] = candidate
                trouve = True
            else:
                col += 1

        if trouve:
            if ligne == N - 1:
                # Solution complète trouvée
                return solution

            # Passer à la ligne suivante
            ligne += 1
            col = 0
        else:
            # Backtrack si aucune colonne n'est valide
            ligne -= 1
            if ligne >= 0:
                col = solution[ligne].y + 1

    raise RuntimeError("Impossible de trouver une solution")
