def twoSum(nums:list[int],target:int)->list[int]:
    hashmap={}
    for key,val in enumerate(nums):
        if val in hashmap.keys():
            return hashmap[val],key
        hashmap[val]=key


