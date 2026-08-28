year = 2034
print("Leap year" if year % 4 == 0
      else "Not Leap Year")

n = 25
print(n % 5 == 0)

n = 125
print(100 <= abs(n) <= 999)

for i in range(1, 11):
    print(i)

for i in range(10, 0, -1):
    print(i)

for i in range(2, 21, 2):
    print(i)

for i in range(1, 20, 2):
    print(i)

n = 10
print(sum(range(1, n+1)))

n = 5
for i in range(1, 11):
    print(n * i)

n = 5
f = 1
for i in range(1, n+1):
    f *= i
    print(f)

n = 12345
print(sum(range(1, n+1)))

n = 12345
print(sum(map(int, str(n))))

n = 12345
print(str(n)[::-1])

n = "121"
print(n == n[::-1])

n = 17
print(n > 1 and
      all(n % i for i in range(2, int(n**0.5)+1)))

for n in range(2, 51):
    if n > 1 and all(n % i for i in range(2, int(n**0.5)+1)):
        print(n)

a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b

n = 153
digits = str(n)
print(sum(int(d)**len(digits)for d in digits) == n)

n = 28
print(sum(i for i in range(1, n)if n % i == 0) == n)

n = 24
print([i for i in range(1, n+1)if n % i == 0])

import math
a, b = 12, 18
print(math.lcm(a,b))

import math
a, b = 12, 18
print(math.gcd(a,b))