def squareOfNumber(num:int):
    

    if(num<0):
        num=-num 

    if num==0 or num==1:
        return num 
    

    x=num>>1
    
    if num&1:
        return (squareOfNumber(x)<<2)+(x<<2)+1
    else:
        return (squareOfNumber(x)<<2)

if __name__=="__main__":
    print(squareOfNumber(12))
