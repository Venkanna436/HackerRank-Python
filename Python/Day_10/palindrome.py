s = input()
n = len(s)
ans = 0

for i in range(n):
    for j in range(i, n):
        x = s[i:j+1]
        if x == x[::-1] and len(set(x)) <= 2:
            ans += 1
print(ans)