# Print hello
print('Hello World!')
boole = bool(1)
print(type(12.0))
print(boole)
print("0123456".find('1'))


d = "ABCDEFG"
print("find: " + str(d.find("D")))
pattern = "D"
sep = d.split(pattern)
print(sep)
sepp = d[0:3]
print(sepp)

e = '01234567'
print(e[::2])
print("\\")


f = "You are wrong"
f = f.lower()
print(f)


g = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb \
Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"

print(g.find("snow"))

re = "."

gr = g.replace(",", re)
print(gr)

name = 'Lizz'
print(name[0:2])

B=["a","b","c"]
print(B[1:])