#1) two sum in leetcode
def twosums(nums, target):
    hashmap = {}
    for i , num in enumerate (nums):
        diff =target -num
        if diff in hashmap:
            return [hashmap[diff],i]
        hashmap[num]=i