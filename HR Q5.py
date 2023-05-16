

def matrix_diagonals(n):
    right_diag=0
    left_diag=0
    n=len(matrix)

    for i in range (n):
        right_diag+=matrix[i][i]
        left_diag+=matrix[i][n-i-1]


    return abs(right_diag-left_diag)

n=int(input())
matrix=[]
for i in range(n):
    row=list(map(int,input().split()))
    matrix.append(row)
print(matrix_diagonals(matrix))