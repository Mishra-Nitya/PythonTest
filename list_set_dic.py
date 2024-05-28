integer = [0, 1, 2, 3, 4]
binary = ["0", "1", "10", "11", "100"]
binary_dict = {}
for i in range(len(integer)):
    binary_dict[integer[i]] = binary[i]
print(binary_dict)

lst = [1,-2,-5,15,-6,12]
additive_inverse = []
for i in lst:
    additive_inverse.append(-1*i)
print(additive_inverse)

integer = [1, -1, 2, -2, 3, -3]
s = {integer[1]**2}
for i in integer:
    s.add(i**2)
print(s)
