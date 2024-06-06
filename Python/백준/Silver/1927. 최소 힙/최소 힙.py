import sys
input = sys.stdin.readline

def main():
    x = int(input())
    h = [0]
    res = []
    
    for _ in range(x):
        inp = int(input())

        if inp == 0:
            if len(h) == 1:
                res.append(0)
            else:
                res.append(h[1])
                # 마지막 노드를 첫 노드로 저장하고 자식노드와 비교하며 교체
                h[1] = h[-1]; h.pop()
                hl = 1
                while True:
                    # 교체할 자식노드 있는지 확인
                    if hl*2+1 < len(h):
                        hl2 = hl*2 if h[hl*2] < h[hl*2+1] else hl*2+1
                    elif hl*2 < len(h):
                        hl2 = hl*2
                    else:
                        break
                        
                    if h[hl2] >= h[hl]:
                        break
                            
                    h[hl], h[hl2] = h[hl2], h[hl]
                    hl = hl2
        
        else:
            # 마지막 노드에 추가하고 부모노드와 비교하며 교체
            h.append(inp)
            hl = len(h) - 1
            while hl > 1:
                hl2 = hl//2
                if h[hl] < h[hl2]:
                    h[hl], h[hl2] = h[hl2], h[hl]
                else:
                    break
                hl = hl2

    for item in res:
        print(item)
    
if __name__ == "__main__": 
    main()