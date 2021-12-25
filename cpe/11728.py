Case = 1
while True:
    S = int(input())
    if S == 0:
        break
    print(f"Case {Case}: ", end="")
    Case += 1
    if S == 1:
        print(1)
        continue
    if S == 0:
        break

    ans = {}
    # sums不超過1000
    for i in range(1, 1001):
        sums = 1
        for j in range(2, i+1):
            if (i % j == 0):
                sums += j
        # 建表
        if (sums < 1001):
            ans[sums] = i

    maxa = 0
    for key, value in ans.items():
        if key == S:
            maxa = max(maxa, value)
            print(maxa)
    if maxa == 0:
        print(-1)
    # print(ans)
'''problem depiction
   輸入的數字，因素和最大的數字和，否則找尋不到為-1
'''
