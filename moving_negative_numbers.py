def moving(arr:list[int])->list[int]:
    left=0
    right=len(arr)-1
    while left<=right:
        if arr[left]>arr[right]:

            arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr

print(moving([12,3,4,-1,5,-7,8,-9]))
