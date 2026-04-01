nums = [1, 2, 3, 1]

def find_match9(nums):
    for i in range(len(nums)):  # Initialize 'i' within the function
        if nums[i] == 3 and (i < len(nums) - 1 and nums[i + 1] == 3):
            return True
    return False  # Return False if no match is found

result = find_match9(nums)
print(result)

# or course solution:
def has_33(nums):
    for i in range(0,len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
print(has_33([1, 3, 3]))      # True
print(has_33([1, 3, 1, 3]))   # False
print(has_33([3, 3]))         # True
print(has_33([1, 2, 3]))      # False
