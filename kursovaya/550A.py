# Дана строка s. Требуется определить, существуют ли в данной строке s две непересекающиеся подстроки "AB" и "BA"
# (подстроки могут идти в любом порядке).
# Стоимость: 1500 (https://codeforces.com/problemset/problem/550/A)

s = input()

a = s.count("AB")
b = s.count("BA")
c = s.count("ABA")
d = s.count("BAB")

e = c + d

if (a > 0 and b > 0) and a + b - e >= 2:
    print("YES")
else:
    print("NO")