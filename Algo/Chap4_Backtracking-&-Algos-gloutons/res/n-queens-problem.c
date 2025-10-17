#include <stdbool.h>
#include <stdlib.h>

// Structure représentant une position sur le plateau
typedef struct {
    int x;
    int y;
} Pos;

/**
 * @param pos La position à vérifier
 * @param disposition La disposition des autres reines sur le plateau
 * @param nb_reines Le nombre de reine sur le plateau
 * @return Si la position de la reine est valide
 */
bool position_reine_est_valide(Pos pos, Pos disposition[], unsigned int nb_reines)
{
    for (unsigned int i = 0; i < nb_reines; i++) {
        int x = disposition[i].x;
        int y = disposition[i].y;

        if (
            y == pos.y                      // même colonne
            || (x - y) == (pos.x - pos.y)   // même diagonale /
            || (x + y) == (pos.x + pos.y)   // même diagonale \
            // il n'y a jamais plsrs reines sur la même lignes donc pas besoin de le vérifier
        ) {
            return false;
        }
    }
    return true;
}

//
// Algorithme de backtracking :
// ----------------------------
//

/**
 * @param N Le nombre de reine à placer sur le plateau NxN
 * @return Un tableau de positions (solution trouvée) ou NULL si aucune solution
 */
Pos* poser_n_reines(unsigned int N)
{
    if (N == 0) return NULL;

    Pos* solution = malloc(N * sizeof(Pos));

    int ligne = 0;
    int col = 0;

    while (ligne >= 0) {
        bool trouve = false;

        // Essayer de placer une reine sur la ligne courante
        while (col < N && !trouve) {
            Pos candidate = {ligne, col};

            if (position_reine_est_valide(candidate, solution, ligne)) {
                solution[ligne] = candidate;
                trouve = true;
            } else {
                col++;
            }
        }

        if (trouve) {
            if (ligne == N - 1) {
                // Solution complète trouvée
                return solution;
            }

            // Passer à la ligne suivante
            ligne++;
            col = 0;
        } else {
            // Backtrack si aucune colonne n'est valide
            ligne--;
            if (ligne >= 0) {
                col = solution[ligne].y + 1;
            }
        }
    }

    free(solution);
    return NULL; // impossible
}
