a, b = (1, 2)

print(a)
print(b)

#if you don't want to use a variable you can just use an underscore -

c, _ = (3, 4)

print(c)
# print(d)

e, f, *g = (1,2,3,4,5)
print(e)
print(f)
print(g)

h, i, *_ = (6,7,8,9,10)
print(h)
print(i)

j, k, _, *m, n = (1,2,3,4,5,6,7)
print(j)
print(k)
print(m)
print(n)

# 1
# 2
# [4, 5, 6]
# 7
