  ###############
 ### Warm-up ###
###############

from pylab import *
import matplotlib.pyplot as mplot

cd C:\\E350\empiricalproject\warmup

# 1.1 - Interpolation
x=arange(-2*pi,2*pi,.001)
y=sin(x)
mplot.plot(x,y)
mplot.xlabel("x")
mplot.ylabel("y")
mplot.title("interpolation")
mplot.savefig("interpolation.png")
mplot.close("all")

#plot(x,y)
#xlabel('x-axis')
#ylabel('y-axis')
#title(r'$y=sin(x)$')
#show() 

# 1.2 - Riemann sum?

# 1.3 - definition

# 1.4 - general function for trapezoid integration

# y=f(x)
# a is the lower bound
# b is the upper bound
# n is the number of partitions

a = float(input('a='))
b = float (input('b='))
if a > b:
print('a is the lower bound. b is the upper bound.')
n=float(input'n=')

# partition
dx=(b-a)/n

# Compute height (h) 

h=
delta_x = ((x2-x1)/1000)
j = abs ((x2-x1)/delta_x)
i = int (j)
print('i =', i)
# initialize
n=0
A= 0.0
x = x1
# Begin Numerical Integration
while n < i:
delta_A = x**2 * delta_x
x = x + delta_x
A = A + delta_A
n = n+1
print('Area Under the Curve =', A)