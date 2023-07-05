def rrea(mat):
    mat = [[0, 3, 0, -1], [5, 2, -8, 8], [-4, 5, 9, -9]]
    n = 0

    for swapped in range(len(mat)):
        flag = False
        for i, x in enumerate(mat):

            if (mat[i][n] == 0):
                flag = True
                continue
            elif flag is True:

                # swap row i with row 1
                mat[i], mat[swapped] = mat[swapped], mat[i]
                mat[swapped] = [i / mat[swapped][swapped] for i in mat[swapped]]

                break

        for i, v in enumerate(mat):
            if i+1 < len(mat):
                if mat[i+1][swapped] == 0:
                    continue
                else:
                    multiper = mat[i+1][swapped]
                    # turn non zero values under the pivot ito zeros:
                    mat[i+1] = [((x*multiper) - mat[i+1][ind]) for ind, x in enumerate(mat[0])]


    return mat


rrea(0)
