def rrea(mat):
    # mat = [[0, 3, 0, -1], [5, 2, -8, 8], [-4, 5, 9, -9]]
    mat = [[0, 2, -8, 8], [-4, 5, 9, -9], [1, -2, 1, 0]]

    pi = 0
    pj = 0
    columns = len(mat[pi])
    rows = len(mat)

    while True:
        flag = False
        for i in range(len(mat)):
            if mat[i][pj] == 0:
                flag = True
                continue
            elif flag is True:
                # swap current row with pivot row
                mat[i], mat[pi] = mat[pi], mat[i]
                break
            else:
                break

        # scale the pivot to one:
        mat[pi] = [i / mat[pi][pi] for i in mat[pi]]

        # turn everything under pivot to 0
        for x in range(1, rows):
            if pi + x < rows:
                if mat[pi + x][pj] == 0:
                    continue
                else:
                    multiplier = mat[pi + x][pj]
                    mat[pi + x] = [mat[pi][i] * multiplier - mat[pi + x][i] for i in range(columns)]

        pi += 1
        pj += 1

        if pi >= rows or pj >= columns:
            return mat




    # for x in range(pj, columns):
    #     if mat[pi][x] == 0:
    #         continue
    #     else:
    #         break

    # n = 0
    # for swapped in range(len(mat)):
    #     flag = False
    #     for i, x in enumerate(mat):
    #
    #         if (mat[i][n] == 0):
    #             flag = True
    #             continue
    #         elif flag is True:
    #
    #             # swap row i with row 1
    #             mat[i], mat[swapped] = mat[swapped], mat[i]
    #             mat[swapped] = [i / mat[swapped][swapped] for i in mat[swapped]]
    #
    #             break
    #
    #     for i, v in enumerate(mat):
    #         if i+1 < len(mat):
    #             if mat[i+1][swapped] == 0:
    #                 continue
    #             else:
    #                 multiper = mat[i+1][swapped]
    #                 # turn non zero values under the pivot ito zeros:
    #                 mat[i+1] = [((x*multiper) - mat[i+1][ind]) for ind, x in enumerate(mat[0])]
    #     n += 1
    #
    return mat


print(rrea(0))
