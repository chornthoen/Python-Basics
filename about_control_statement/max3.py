a = int(input("enter a:"))
b = int(input("enter b:"))
c = int(input("enter c:"))
if a > b:
    max = a
if b > a:
    max = b
if max < c:
    max = c
print(max)
