#strip() trong Python là hàm dùng để xóa khoảng trắng (whitespace)
# hoặc ký tự chỉ định ở đầu và cuối chuỗi.
#Trong Python, ''.join(...) là cách nhanh và
# chuẩn nhất để ghép các phần tử của một iterable (list, tuple, v.v.) thành một chuỗi.
s = input().strip()
n = len(s)

def char_max(ch):
    t = ''.join(ch if c == '0' else c for c in s)

    t2 = t + t
    best = cur = 0
    for c in t2:
        if c == ch:
            cur += 1
            best = max(best, cur)
        else:
            cur = 0

    return best
ans = 0
for ch in "abcd":
    ans = max(char_max(ch), ans)

print(ans)