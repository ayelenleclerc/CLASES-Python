a = 7
b = 1
c = 3

# if a > b:
#     print(a)
# else:
#     print(b)


if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)


if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > a:
        if b > c:
            print(b)
        else:
            print(c)
    else:
        print(b)
