#include <stdlib.h>

//
// Algorithme glouton :
// ----------------------------
//

/**
 * @param montant Le montant à rendre
 * @param valeurs Les valeurs des pièces (triées par ordre décroissant)
 * @param nb_valeurs Le nombre de types de pièces
 * @return Tableau d'entiers (allocation dynamique) représentant les pièces utilisées,
 *         ou NULL si impossible
 */
int* rendre_monnaie(int montant, int valeurs[], int nb_valeurs)
{
    int reste = montant;

    // On alloue un tableau avec une taille maximale (montant pièces de valeur 1)
    int *solution = malloc(montant * sizeof(int));

    int k = 0; // compteur du nombre de pièces utilisées

    for (int i = 0; i < nb_valeurs; i++) {
        int v = valeurs[i];
        int q = reste / v;

        for (int j = 0; j < q; j++) {
            solution[k++] = v;
        }

        reste -= q * v;
    }

    if (reste != 0) {
        free(solution);
        return NULL; // impossible par stratégie gloutonne
    }

    return solution;
}

// Vous aurez peut-être remarqué que la fonction `rendre_monnaie` renvoie un simple pointeur.
// C'est un problème que nous laissons au lecteur le plaisir de résoudre.
