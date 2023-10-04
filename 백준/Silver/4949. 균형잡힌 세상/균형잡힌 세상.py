lis = []

# 입력
while(True):
    inp = list(input())
    if (len(inp) == 1 and inp[0] == '.'):
        break
    lis.append(inp)
  
for i in lis:
    # 괄호만 추출, 카운터에 등록
    templis = []
    counter = { '(':0, ')':0, '[':0, ']':0 }
    for char in i:
        if (char == "(" or char == "[" or char == ")" or char == "]"):
            templis.append(char)
            counter[char] += 1
    
    # 괄호가 없는 경우
    if (len(templis) == 0):
        print("yes")
        continue
        
    # 괄호의 쌍이 맞지 않는 경우
    if (counter['('] != counter[')']) or (counter['['] != counter[']']):
        print("no")
        continue
    
    # 순서가 적절한지 검토
    # () [] 묶음을 반복해서 제거하면 될 거 같은데?
    while(True):
        detect,cur = 0,0
        while(cur < len(templis) - 1):
            if (templis[cur] == '(' and templis[cur+1] == ')'):
                detect += 1
                del templis[cur+1]
                del templis[cur]
            elif (templis[cur] == '[' and templis[cur+1] == ']'):
                detect += 1
                del templis[cur+1]
                del templis[cur]
            else:
                cur += 1
            #print(cur, detect, templis)
        if (detect == 0):
            break
            
    if (len(templis) == 0):
        print('yes')
    else:
        print('no')