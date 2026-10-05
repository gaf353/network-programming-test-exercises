import math

a,b,c=3,4,5
result=a/b+c
print(1/1+result)

a,b,c=1,1,-6
x1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
x2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
print(x1,x2)

r=5
area=math.pi*r**2
print(area)

beta,g=2.0,3.2
print(beta*math.exp(-g))

x, mu, p = 0, 1.5, 2.0
val = (1/math.sqrt(2*math.pi*p)) * math.exp((x-mu)**2 / (2*p**2))
print(val)








