# gradient_descent.py
x_old = 0 #value doesn't matter. abs(x_new - x_old) must be > alpha
x_new = 6
alpha = .01
precision = .00001

def df(x):
    y = 4*x**3-9*x**2
    return y
while abs(x_new-x_old)>precision:
    x_old = x_new
    x_new += -alpha*df(x_old)

print("The local minimum occurs at %f" %x_new)
