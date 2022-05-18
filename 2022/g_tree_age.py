n = int(input())
a = list(map(str, input().split()))

for i in range(len(a)):
  if a[i] == "zero":
    a[i] = 0
  if a[i] == "one":
    a[i] = 1
  if a[i] == "two":
    a[i] = 2
  if a[i] == "three":
    a[i] = 3
  if a[i] == "four":
    a[i] = 4
  if a[i] == "five":
    a[i] = 5
  if a[i] == "six":
    a[i] = 6
  if a[i] == "seven":
    a[i] = 7
  if a[i] == "eight":
    a[i] = 8
  if a[i] == "nine":
    a[i] = 9

b = ''
for j in a:
  b = int(str(b) + str(j))

b = int(b)*365*24*60
c = b % (10**9 + 7)

print(c)
