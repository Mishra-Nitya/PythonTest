
india = ['mumbai', 'banglore', 'chennai', 'delhi']
pakistan = ['lahore', 'karachi', 'islamabad']
bangladesh = ['dhaka', 'khulna', 'rangpur']

a = input("enter a city")
if a in india:
    print("india")
elif a in pakistan:
    print("pakistan")
elif a in bangladesh:
    print("bangladesh")
else:
    print("enter a valid city")

a = input("enter first city")
b = input("enter second city")
if a in india and b in india:
    print("both cities are in india")
elif a in pakistan and b in pakistan:
    print("both cities are in pakistan")
elif a in bangladesh and b in bangladesh:
    print("both cities are in bangladesh")
else:
    print("they don't belong in the same country")

sl = float(input("enter your sugar level"))
if sl in range(80,101):
    print("normal")
elif sl >100:
    print("high")
else:
    print("low")