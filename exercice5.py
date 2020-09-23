def afficherMatrice(M):
    for i in range(len(M)):
        ligne = ['{}'.format(x) for x in M[i]]
        print(ligne, '\t')
    print('\n')


def matriceZero(nbLignes, nbColonnes):
    A = []

    #TODO: Remplir la matrice A de 0, selon les dimensions données

    return A



def multiplierMatrices(A, B):

    #TODO: Si les matrices ne peuvent pas etre multipliées, affecter à C une matrice nulle [nbLignesA x nbColonnesB]
    C =



    #TODO: Sinon faire la multiplication et mettre dans C le résultat
    C =

    return C


if __name__ == '__main__':
    A = ([[1, 2], [1, 5]])
    B = ([[1, 2], [1, 6], [3, 8]])
    C = ([[1], [6]])
    afficherMatrice(multiplierMatrices(A, B))
    afficherMatrice(multiplierMatrices(B, A))
    afficherMatrice(multiplierMatrices(A, C))
    afficherMatrice(multiplierMatrices(B, C))