
def checker(f):
    def helper(x):
        if type(x) == int and x > 0:
            return f(x)
        else:
            raise Exception("arguement is not a non negtive integer")
    return helper

@checker
def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)

try:
    print(fact(1.0256))
except Exception as e:
    print("error")
