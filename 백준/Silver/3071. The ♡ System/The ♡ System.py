# 3071 The ♡ System
import math

lis = [3**i for i in range(20)]
check = 0
mi = 0

res = ''
reslist = []

for _ in range(int(input())):
    mi = 0
    res = ''
    check = 0
    
    inp = int(input())
    if inp == 0:
        reslist.append('0')
        continue
    absinp = abs(inp)

    while(lis[mi] < absinp):
        mi += 1

    # lis = 3에 대한 리스트
    # m = mi를 구하기 위한 임시값
    # mi = 입력값과 비교할 만한 값을 가르키는 포인터
    
    while(mi >= 0):
        # 일단 현재 수(inp)가 음수인지 양수인지 확인
        # 음수라면 inp = inp + lis[mi]
        # 양수라면 inp = inp - lis[mi]
        tempinp = inp
        if (inp > 0):
            inp = inp - lis[mi]
        else:
            inp = inp + lis[mi]

        # 그 다음에 그 inp의 절댓값이 lis[mi]/2 보다 큰지 확인 - 크면 무조건 0
        # 작다면 inp가 음수인지 양수인지 확인 - 음수라면 -1, 양수라면 1
        # 다음단계 - inp가 음수인지 양수인지 확인, inp와 lis[mi-1]과의 비교
        if (abs(inp) > lis[mi]//2):
            inp = tempinp
            if (check != 0):
                res += '0'
            check = 1
        else:
            if(tempinp > 0):
                check = 1
                res += '1'
            else:
                check = 1
                res += '-'
        mi -= 1
    reslist.append(res)

for i in reslist:
    print(i)