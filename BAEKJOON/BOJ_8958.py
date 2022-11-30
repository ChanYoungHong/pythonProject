
# quizCnt = input()
# totalScore = 0
# cnt = 0
#
# QuizArray = ['O, O, O, O, O, O, O, O, O, O, O, O, O, O, O']
#

# b = "OOOOOOOOOO"
#
# print(a[1:4])
# print(a[2:8])
#
# for i in range(len(a)):
#     if a[i] == a[i+1]:
#         totalScore += 1
#         cnt += 1

# 답변 보고 내가 생각한 것과 합친 답

# 받는 개수
n = int(input())

for _ in range(n):
    a = list(input())
    score = 0
    sum_score = 0  # 새로운 ox리스트를 입력 받으면 점수 합계를 리셋한다.
    for i in range(len(a)):
        if a[i] == 'O':
            score += 1  # 'O'가 연속되면 점수가 1점씩 커진다.
            sum_score += score  # sum_score = sum_score + score
        else:
            score = 0
    print(sum_score)