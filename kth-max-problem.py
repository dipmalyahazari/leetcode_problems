#using quickselect algorithm to find the kth largest element
import random
def quick_select(arr:list[int],k:int)->int:
    pivot=random.choice(arr)

    leftArr=[x for x in arr if x>pivot]
    
    midArr=[x for x in arr if x==pivot]

    rightArr=[x for x in arr if x<pivot]

    if k<=len(leftArr):
        return quick_select(leftArr,k)
    if len(leftArr)+len(midArr)<k:
        return quick_select(rightArr,k-len(leftArr)-len(midArr))

    return pivot

def kth_largest(arr:list[int],k:int):
    return quick_select(arr,k)

if __name__=="__main__":
    print(kth_largest([12,3,4,5,7,8,9],2))
