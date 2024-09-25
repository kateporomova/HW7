a = input('Input A: ')
b = input('Input B: ')
c = input('Input C: ')

try:
    a = int(a)
    b = int(b)
    c = int(c)

    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (- b + d ** (0.5))/(2 * a)
        x2 = (- b - d ** (0.5))/(2 * a)
        x = [x1, x2]
        print(f"The solution of your equation is:\nx1 = {x1:.2f}\nx2 = {x2:.2f}") 
    elif d == 0:
        x = - b / (2 * a)
        print(f"There is only one solution for x: {x:.2f}")
    elif d < 0:
        print('No solution')
except:
    print('Please enter correct values')