def hasDuplicate(nums:list[int])->bool:

    l=set()

    for key,val in enumerate(nums):
        if val not in l:
            l.add(val)
        else:
            return True
    return False

print(hasDuplicate([12,3,45,2,3]))
