# import decimal
from fractions import Fraction


def echelon(mat):
    # mat = [[0, 3, 0, -1], [5, 2, -8, 8], [-4, 5, 9, -9]]

    pi = 0
    pj = 0
    columns = len(mat[pi])
    rows = len(mat)
    # mat = [[decimal.Decimal(x) for x in row] for row in mat]
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
        try:
            mat[pi] = [Fraction(i, mat[pi][pi]) for i in mat[pi]]
        except ZeroDivisionError as e:
            print(e)
        # turn everything under pivot to 0
        for x in range(1, rows):
            if pi + x < rows:
                if mat[pi + x][pj] == 0:
                    continue
                else:
                    multiplier = mat[pi + x][pj]
                    mat[pi + x] = [mat[pi + x][i] - Fraction(mat[pi][i], Fraction(1, multiplier)) for i in
                                   range(columns)]

        pi += 1
        pj += 1
        # print (mat, f"\n")
        if pi >= rows or pj >= columns:
            return mat  # returned mat

    return mat


# decimal.setcontext(decimal.Context(prec=3))
mat = [[-4, -2, 2, 0], [-2, 3, -3, -8], [1, -4, 4, 9]]
temp = echelon(mat)

def rref(mat):

    rows = len(mat)
    cols = len(mat[0])

    check = False
    for i in mat[-1]:
        if i != 0:
            check = True
            break
        

    if check:
        pi = -1
        pj = -2
        
    else:
        pi = -2
        pj = -2
    
    while pi >= -rows:
        i = 1
        while i <= rows:
            try:
                if mat[pi-i][pj] != 0:
                    multiplier = mat[pi-i][pj]
                    mat[pi-i][-1] = mat[pi-i][-1] - (multiplier * mat[pi][-1])
                    mat[pi-i][pj] = 0
                i += 1
            except IndexError as e:
                break
        pi -= 1
        pj -= 1

        
        
        
        return mat 
            




    
    
    
temp = rref(temp)
print(f"{temp[0]}\n{temp[1]}\n{temp[2]}")
