def my_var():
    a =  42
    b = "42"
    c = "quarante-deux"
    d = 42.0
    e = True
    f = [42]
    g = {42: 42}
    h = (42,)
    i = set()

    print(a, "has a type", type(a))
    print(b, "has a type", type(b))
    print(c, "has a type", type(c))
    print(d, "has a type", type(d))
    print(e, "has a type", type(e))
    print(f, "has a type", type(f))
    print(g, "has a type", type(g))
    print(h, "has a type", type(h))
    print(i, "has a type", type(i))

if __name__ == '__main__':
    my_var()