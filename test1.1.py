a,b=input("Enter two numbers:").split()

a=int(a)
b=int(b)
print(f'{a} + {b}={a+b}')
print(f'{a} - {b}={a-b}')
print(f'{a} * {b}={a*b}')
print(f'{a} / {b}={a/b}')

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

print('{} + {}={}'.format(a,b,a+b))
print('{} - {}={}'.format(a,b,a-b))
print('{} * {}={}'.format(a,b,a*b))
print('{} / {}={}'.format(a,b,a/b))