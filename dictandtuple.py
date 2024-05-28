
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

def avg(i):
    sum = 0
    for n in i:
        sum += n
    return sum/len(i)
dicti = {'info' : [600, 630, 620], 'ril' : [1430, 1490, 1567], 'mtl' : [234,180,160]}
op = input("enter your choice")
if op.lower() == 'print':
    print("info ==> ", dicti['info'], "==> avg: ", avg(dicti['info']), "\n", "ril ==> ", dicti['ril'], "==> avg: ", avg(dicti['ril']), "\n", "mtl ==> ", dicti['mtl'], "==> avg: ", avg(dicti['mtl']))
elif op.lower() == 'add':
    n = input("enter the stock ticker")
    a = eval(input("enter the price"))
    dicti[n] = a
    print(dicti)

def circle_calc(r):
    ar = 3.14*(r**2)
    cr = 2*3.14*r
    d = r*2
    return ar, cr, d

print(circle_calc(10))