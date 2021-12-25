n = int(input())
while(n > 0):
    n -= 1
    s = 0
    r = int(input())
    num = list(map(int, input().split()))
    if len(num) == r:
        for i in range(1, len(num)):
            for j in range(0, i):
                if(num[j] <= num[i]):
                    s += 1
        print(s)

'''problem depiction
   前面一個數字是否小，計算總量次數
'''
