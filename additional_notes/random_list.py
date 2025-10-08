import random

"""Create a list of random ints and delete random elements until `keep` remain."""
keep = 5
nums = [random.randint(0, 100) for _ in range(5)]
print("Original:", nums)
print("Deleting some random numbers:")
while len(nums) > keep:
    idx = random.randint(0, len(nums) - 1)
    nums.pop(idx)
print("Remaining:", nums)
