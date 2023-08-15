a, b, c = 10, 20, 5
print(a, b, c)
# 1.
maximo = a
medio = b
minimo = c

if b > maximo:
    maximo = b
    medio = a
    minimo = c

if c > maximo:
    maximo = c
    medio = b
    minimo = a

if minimo > medio:
    medio, minimo = minimo, medio

print(maximo, medio, minimo)

# 2
maximo = max(a, b, c)
minimo = min(a, b, c)


print(maximo, minimo)
