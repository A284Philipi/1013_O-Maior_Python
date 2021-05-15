a, b, c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)
if a > b:
    if a > c:
        maior = a
    else:
        maior = c
else:
    if b > c:
        maior = b
    else:
        maior = c
print("{} eh o maior".format(maior))