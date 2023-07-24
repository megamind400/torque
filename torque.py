#import decimal

def echelon(mat):
    # mat = [[0, 3, 0, -1], [5, 2, -8, 8], [-4, 5, 9, -9]]
    

    pi = 0
    pj = 0
    columns = len(mat[pi])
    rows = len(mat)
    #mat = [[decimal.Decimal(x) for x in row] for row in mat]
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
                    mat[pi + x] = [ mat[pi + x][i] - (mat[pi][i] * multiplier)  for i in range(columns)]

        pi += 1
        pj += 1

        if pi >= rows or pj >= columns:
            return mat #returned mat

    return mat


decimal.setcontext(decimal.Context(prec=3))
mat = [[-3, 2, 3, -11], [1, 2, -1, 9], [2, -4, -4, 8]]
temp = echelon(mat)


def rref(mat):
    '''
    parameter:
        mat: must be echelon form

    return:
        mat: reduced row echelon form of the matrix
    '''
    [1,2,3,4]
    [0,1,4,6]
    []


print(f"{temp[0]}\n{temp[1]}\n{temp[2]}")


