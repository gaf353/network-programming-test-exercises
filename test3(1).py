def calc(*nums, op='+'):
    if op == '+':
        result = 0
        for n in nums:
            result += n
    elif op == '*':
        result = 1
        for n in nums:
            result *= n
    else:
        raise ValueError("Invalid operator. Use '+' or '*'.")
    return result

print(calc(1,1,4, op='+'))
print(calc(1,2, op='*'))
print(calc(1,2,3,4, op='+'))
print(calc(1,2,3,4,op='*'))



