nums = [1,2,3,4,5,6,7]
k = 3
n = len(nums)
k %= n

# Step 1: Reverse entire array
nums.reverse()

# Step 2: Reverse first k elements
nums[:k] = reversed(nums[:k])

# Step 3: Reverse remaining elements
nums[k:] = reversed(nums[k:])

print(nums)