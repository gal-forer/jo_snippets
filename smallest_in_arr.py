




def s(nums):
    nums.sort()
    prev = nums[0]
    for num in nums:
        if prev == num:
            continue
        elif num-prev > 1:
            return prev + 1
        prev = num

nums = [1,5,1,4,2,6,6,1,8,7,10,3,9,12]
print(s(nums))
