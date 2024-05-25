'''
dic = {'china' : 143, 'india' : 136, 'USA' : 32, 'pakistan' : 21}
a = input("enter the country to add")
if a in dic:
    pass
else:
    b = int(input("enter population"))
    dic[a] = b
print(dic)
c = input("Enter country to remove")
dic.pop(c)
print(dic)
d = input("enter country to enquire")
print(dic[d])
'''
dicti = {'info' : [600, 630, 620], 'ril' : [1430, 1490, 1567], 'mtl' : [234,180,160]}
op = input("enter your choice")
if op.lower() == 'print':
    print("info ==> ", dicti['info'], "==> avg: ")
