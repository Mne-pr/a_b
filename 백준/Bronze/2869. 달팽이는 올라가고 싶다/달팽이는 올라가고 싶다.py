up,down,end = map(int, input().split())

dayup = (up-down)

# 먼저 마지막에 내려가는 경우를 미리 고려함
end = end - down

# 몫 : 올라간 날, 나머지 : 그만큼 올라가고 남은 거리
day = end//dayup
end = end% dayup

# 나머지가 0인 경우, 다 올라오고 내려왔더니 0이니까 도착했었다
if end == 0:
    print(day)
# 나머지가 0 이상인 경우, 다 올라오고 내려왔더니 그래도 올라가야 하더라. 근데 하루만 더 가면 됨
else:
    print(day+1)