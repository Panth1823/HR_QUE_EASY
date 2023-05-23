def binarySearch(arey,valuee):
    start=0
    end=len(arey)-1

    while start<=end:
        mid=(start+end)//2
        if arey[mid]==valuee:
            return mid
        elif arey[mid]<valuee:
            start=mid+1
        else:
            end=mid-1
    return -1


arey=input("Enter array elements separated with comma:")
arey=[int(i) for i in arey.split(",")]
valuee=int(input("Enter value to Search:"))
result=binarySearch(arey,valuee)
print("Index:",result)
