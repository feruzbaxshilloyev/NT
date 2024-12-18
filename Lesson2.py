'''
def masala30(n, k):
    a, r = 1, []
    while a != k + 1:
        b, c= 1, []
        while b != n + 1:
            t = int(input(f"{a}-to'plamning {b}-elementini kiriting: "))
            c.append(t)
            b += 1
        r.append(sum(c))
        a += 1
    return r

print(masala30(2, 2))



def masala31(n, k):
    a, r = 1, 0
    while a != k + 1:
        b, c= 1, []
        while b != n + 1:
            t = int(input(f"{a}-to'plamning {b}-elementini kiriting: "))
            c.append(t)
            b += 1
        if 2 in c:
            r += 1
        a += 1
    return r

print(masala31(2, 2))



def masala32(n, k):
    a, r = 1, []
    while a != k + 1:
        b, c= 1, []
        while b != n + 1:
            t = int(input(f"{a}-to'plamning {b}-elementini kiriting: "))
            c.append(t)
            b += 1
        if 2 not in c:
            r.append(0)
        else:
            r.append(c.index(2))
        a += 1
    return r

print(masala32(2, 2))



def masala33(n, k):
    a, r = 1, []
    while a != k + 1:
        b, c= 1, []
        while b != n + 1:
            t = int(input(f"{a}-to'plamning {b}-elementini kiriting: "))
            c.append(t)
            b += 1
        if 2 not in c:
            r.append(0)
        else:
            r.append(len(c) - c[::-1].index(2) - 1)
        a += 1
    return r

print(masala33(2, 2))




def masala34(n, k):
    a, r = 1, []
    while a != k + 1:
        b, c= 1, []
        while b != n + 1:
            t = int(input(f"{a}-to'plamning {b}-elementini kiriting: "))
            c.append(t)
            b += 1
        if 2 not in c:
            r.append(0)
        else:
            r.append(sum(c))
        a += 1
    return r

print(masala34(2, 2))



def masala35(k):
    r, a= [], 1
    while a != k + 1:
        d, b, c = True, 1, []
        while d:
            t = int(input(f"{a}-to'plamning {b}-elementini kiriting: "))
            c.append(t)
            b += 1
            if t == 0:
                d = False
        r.append(len(c))
        a += 1
    return r

print(masala35(3))



def masala36(k):
    r, a= 0, 1
    while a != k + 1:
        d, b, c = True, 1, []
        while d:
            t = int(input(f"{a}-to'plamning {b}-elementini kiriting: "))
            c.append(t)
            b += 1
            if t == 0:
                d = False
        y = sorted(c)
        if c == y:
            r += 1
        a += 1
    return r

print(masala36(3))



def masala37(k):
    r, a= 0, 1
    while a != k + 1:
        d, b, c = True, 1, []
        while d:
            t = int(input(f"{a}-to'plamning {b}-elementini kiriting: "))
            c.append(t)
            b += 1
            if t == 0:
                d = False
        c.pop()
        y = sorted(c)
        if c == y or c == y[::-1]:
            r += 1
        a += 1
    return r

print(masala37(3))
'''


def masala38(k):
    r, a= [], 1
    while a != k + 1:
        d, b, c = True, 1, []
        while d:
            t = int(input(f"{a}-to'plamning {b}-elementini kiriting: "))
            c.append(t)
            b += 1
            if t == 0:
                d = False
        c.pop()
        y = sorted(c)
        if c == y:
            r.append(1)
        elif c == y[::-1]:
            r.append(-1)
        else:
            r.append(0)
        a += 1
    return r

print(masala38(3))