
def calculate_area(b, h):
    return (1/2)*b*h
print(calculate_area(2,8))

def calculate_area(b, h, s):
    if s == 'triangle':
        return (1/2)*b*h
    elif s == 'rectangle':
        return b*h
print(calculate_area(2,8, 'triangle'))
print(calculate_area(2,8, 'rectangle'))

def print_pattern(n):
    for i in range(n):
        print("*"*(i+1))
print_pattern(int(input()))