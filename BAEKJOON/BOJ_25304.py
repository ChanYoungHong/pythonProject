
# 총 예상된 총 금액
TotalMoney = int(input())
# 계산한 물품 수량
TotalCnt = int(input())

# 실제 총 금액
CheckMoney = 0

for i in range(TotalCnt):
    n,k = map(int, input().split())
    CheckMoney += n*k

if TotalMoney == CheckMoney:
    print("Yes")
else:
    print("No")