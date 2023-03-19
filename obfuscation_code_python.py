import random as r
class A:
    def __init__(self, x):
        self.a = x
    def b(self, y):
        z = self.a + y
        return z

def c(d, e):
    f = d * e
    return f

g = A(r.randint(1, 10))
h = r.randint(1, 10)
i = g.b(h)
j = c(h, i)

print(j)

def a(b):
    c = 0
    for d in range(len(b)):
        c += ord(b[d])
    return c

def e(f):
    g = ''
    for h in range(len(f)):
        i = ord(f[h]) + 1
        g += chr(i)
    return g

j = input('Entrez un mot de passe : ')
if a(j) == 3214:
    print('Accès autorisé')
else:
    print('Accès refusé')