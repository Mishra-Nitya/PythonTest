
l = [2200, 2350, 2600, 2130, 2190]
print(l[0] - l[1]) if l[0]>l[1] else print(l[1] - l[0])
print(l[0] + l[1] + l[2])
print(2000 in l)
l.append(1980)
print(l)
l[3] = l[3] - 200
print(l)

heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

print(len(heros))
heros.append('black panther')
print(heros)
heros.pop()
heros.insert(4,'black panther')
print(heros)
heros[1:3] = ['doctor strange']
heros.sort()
print(heros)
