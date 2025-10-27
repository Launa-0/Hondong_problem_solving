T = input().strip()
L = len(T)

idx = 0       # T에서 지금 맞춰야 할 위치
n = 0         # 현재 숫자(최종적으로 답)

while idx < L:
    n += 1
    for ch in str(n): #n을 문자열로 바꿔서 비교
        if idx < L and ch == T[idx]: 
            idx += 1 #현재 자릿수 ch가 배열 T의 문자와 같다면 매칭성공 ->  인덱스 증가시키기
            if idx == L: #전부 맞추면 루프 탈출
                break

print(n)
