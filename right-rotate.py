def rightRotate(arr:list[int],k:int)->list[int]:
    n=len(arr)

    for _ in range(k):

        last=arr[n-1]

        for i in range(n-1,0,-1):
            arr[i]=arr[i-1]
        arr[0]=last
    return arr

if __name__=="__main__":
    print(rightRotate([1,2,3,4,5,6],3))

