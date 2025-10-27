T = input().strip()
L = len(T)

idx = 0       # T에서 지금 맞춰야 할 위치
n = 0         # 현재 숫자(최종적으로 답)

while idx < L:
    n += 1
    for ch in str(n):
        if idx < L and ch == T[idx]:
            idx += 1
            if idx == L:
                break

print(n)
