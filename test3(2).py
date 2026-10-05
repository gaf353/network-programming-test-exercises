def min_max(nums):
    smallest = nums[0]
    largest = nums[0]
    for n in nums[1:]:
        if n < smallest:
            smallest = n
        if n > largest:
            largest = n
    return (smallest, largest)


nums = [int(x) for x in input("Enter integers separated by spaces: ").split()]
mn, mx = min_max(nums)
print(f"min = {mn}, max = {mx}")