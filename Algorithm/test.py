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

"""
[문제2] 
조건:
- "긴급", "보통", "낮음" 의 우선 순위를 가진다.
- 동일한 우선 순위 작업의 경우, 소요시간이 작은 것을 우선으로 한다.
- 동일한 소요시간의 작업인 경우, 먼저 들어온 작업을 우선한다.
- SORT 함수 사용금지 ( 알고리즘 직접 구현 )
(개발 언어 선택은 자유 C,C++,PHP,python,Javascript,JAVA 등)
"""
workList = [
    { '긴급도' : '낮음', '소요시간' : 1, '작업내용' : 'A.로그인 화면 오타 수정' },
    { '긴급도' : '긴급', '소요시간' : 3, '작업내용' : 'B.OTP 사용자 로그인 안됨' },
    { '긴급도' : '보통', '소요시간' : 1, '작업내용' : 'C.권한 안내 문구 수정' },
    { '긴급도' : '낮음', '소요시간' : 2, '작업내용' : 'D.로딩중 표시 아이콘 변경' },
    { '긴급도' : '긴급', '소요시간' : 3, '작업내용' : 'E.메일의 본문이 표시되지 않는 문제' },
    { '긴급도' : '보통', '소요시간' : 1, '작업내용' : 'F.첨부파일 사이즈 표시 오류 수정' },
    { '긴급도' : '긴급', '소요시간' : 2, '작업내용' : 'G.메일 전송시 첨부파일 누락됨' },
    { '긴급도' : '보통', '소요시간' : 3, '작업내용' : 'H.1:1 문의 기능 구현' },
    { '긴급도' : '낮음', '소요시간' : 1, '작업내용' : 'I.제품 로고 변경' },
    { '긴급도' : '보통', '소요시간' : 3, '작업내용' : 'J.안읽음 카운트 오류 문제' },
    { '긴급도' : '낮음', '소요시간' : 1, '작업내용' : 'K.폰트 색상 변경' },
    { '긴급도' : '긴급', '소요시간' : 2, '작업내용' : 'L.전체 메일함 동기화 안되는 문제' }
]

tmp= {}
sortedWorkList1 = []
sortedWorkList2 = []
sortedWorkList3 = []
for i in range(len(workList)):
    if workList[i].get('긴급도') == '긴급':
        sortedWorkList1.append(workList[i])
        for j in range(len(sortedWorkList1)):
            for k in range(len(sortedWorkList1)):
                if sortedWorkList1[j].get('소요시간') < sortedWorkList1[k].get('소요시간'):
                    sortedWorkList1[j], sortedWorkList1[k] = sortedWorkList1[k], sortedWorkList1[j]
    if workList[i].get('긴급도') == '보통':
        sortedWorkList2.append(workList[i])
        for j in range(len(sortedWorkList2)):
            for k in range(len(sortedWorkList2)):
                if sortedWorkList2[j].get('소요시간') < sortedWorkList2[k].get('소요시간'):
                    sortedWorkList2[j], sortedWorkList2[k] = sortedWorkList2[k], sortedWorkList2[j]
    if workList[i].get('긴급도') == '낮음':
        sortedWorkList3.append(workList[i])
        for j in range(len(sortedWorkList3)):
            for k in range(len(sortedWorkList3)):
                if sortedWorkList3[j].get('소요시간') < sortedWorkList3[k].get('소요시간'):
                    sortedWorkList3[j], sortedWorkList3[k] = sortedWorkList3[k], sortedWorkList3[j]
                if sortedWorkList3[j].get('소요시간') == sortedWorkList3[k].get('소요시간'):
                    if sortedWorkList3[j].get('작업내용').split('.')[0] < sortedWorkList3[k].get('작업내용').split('.')[0]:
                        sortedWorkList3[j], sortedWorkList3[k] = sortedWorkList3[k], sortedWorkList3[j]

sortedWorkList = sortedWorkList1 + sortedWorkList2 + sortedWorkList3
for i in range(len(sortedWorkList)):
    print(sortedWorkList[i].values())