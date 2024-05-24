
result = ['heads', 'tails', 'tails', 'heads', 'tails', 'heads', 'heads', 'tails', 'tails', 'tails']
count = 0
for i in result:
    if i == 'heads':
        count += 1
print(count)
for i in range(1,10):
    if i%2 == 0:
        continue
    print(i**2)

expense_list = [2340, 2500, 2100, 3100, 2980]
month_list = ['jan', 'feb', 'mar', 'apr', 'may']
exp = int(input("enter expence"))
m = -1
for i in range(len(expense_list)):
    if exp == expense_list[i]:
        m = i
        break
if m != -1:
    print(f'{exp} was found in {month_list[m]}')
else:
    print(exp, "not found")

i = 0
exit = 0
while i < 5:
    comm = input("are you tired?")
    if comm == 'yes':
        print("you didn't finish the race")
        exit = 1
        break
    i += 1
if exit == 0:
    print("congratulations")

for i in range(1,6):
    print("*"*i, end = '\n')
