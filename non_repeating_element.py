def non_repeat(nums:list[int])->list[int]:
    xor_val=0

    for i in nums:
        xor_val^=i
    
    xor_val &=-xor_val
    res=[0,0]

    for num in nums:

        if num & xor_val==0:
            res[0]^=num

        else:
            res[1]^=num

    if res[0]>res[1]:
        res[0],res[1]=res[1],res[0]

    return res 

if __name__=='__main__':
    print(non_repeat([12,23,12,34,34,1]))




