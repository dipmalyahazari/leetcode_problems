def count(num:int)->int:
    count=0
    while num:
        num&=(num-1)
        count+=1
    return count

if __name__=="__main__":
    print(count(12))
