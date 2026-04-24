def twoSum(nums, target):
    output = []
    for i in range(len(nums)-1):
        for j in range(len(nums)-1):
            if nums[i]+nums[j+1]==target:
                output.append(i)
                output.append(j+1)
            break
    return output            
nums = [int(x) for x in input().split()]
target = int(input())
print(twoSum(nums,target))