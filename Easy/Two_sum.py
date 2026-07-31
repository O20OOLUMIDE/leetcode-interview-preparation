def two_sum(nums, target): 

    for i in range(len(nums)): 
        for index in range(i + 1, len(nums)): 
            total = nums[i] + nums[index]

            if total == target: 
                return [i, index]

# Main program 
nums = [2, 7, 11, 15]
target = 9

print("The indices are {}".format(two_sum(nums, target)))
