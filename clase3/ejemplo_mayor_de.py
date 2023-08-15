a = 10
b = 20
c = 30

mayor = a

if b > mayor:
    mayor = b

if c > mayor:
    mayor = c

print(mayor)


mayor = max(a, b, c)
print(mayor)
