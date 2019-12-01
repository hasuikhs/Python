"""
1부터 16까지 2차원 배열이 있다
해당 배열을 밖에 배열은 반시계 방향으로 한칸씩
안쪽 배열은 시계방향으로 한칸씩
[2차원 배열]
1   2  3  4
5   6  7  8
9  10 11 12
13 14 15 16

[출력 결과]
2  3  4  8
1 10  6 12
5 11  7 16
9 13 14 15 
"""
from pprint import pprint

# 기존 행렬
matrix = [[0]*4 for i in range(4)]
cnt = 0
for i in range(4):
    for j in range(4):
        cnt += 1
        matrix[i][j] = cnt

pprint(matrix, width=20)

# 회전 행렬
rotatedMatrix = [[0]*4 for i in range(4)]
for i in range(4):
    for j in range(3):
        if i == 0:
            rotatedMatrix[i][j] = matrix[i][j+1]
        if i == 3:
            rotatedMatrix[i][j+1] = matrix[i][j]
        if i == 1:
            if j == 1:
                rotatedMatrix[i][j] = matrix[i+1][j]
            elif j == 2:
                rotatedMatrix[i][j] = matrix[i][j-1]
        if i == 2:
            if j == 1:
                rotatedMatrix[i][j] = matrix[i][j+1]
            elif j == 2:
                rotatedMatrix[i][j] = matrix[i-1][j]
for i in range(3):
    for j in range(4):
        if j == 0:
            rotatedMatrix[i+1][j] = matrix[i][j]
        if j == 3:
            rotatedMatrix[i][j] = matrix[i+1][j]
        
pprint(rotatedMatrix, width=20) 

