# def binarySearch(arey,valuee):
#     start=0
#     end=len(arey)-1
#
#     while start<=end:
#         mid=(start+end)//2
#         if arey[mid]==valuee:
#             return mid
#         elif arey[mid]<valuee:
#             start=mid+1
#         else:
#             end=mid-1
#     return -1
#
#
# arey=input("Enter array elements separated with comma:")
# arey=[int(i) for i in arey.split(",")]
# valuee=int(input("Enter value to Search:"))
# result=binarySearch(arey,valuee)
# print("Index:",result)

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
swap=0
for i in range (0,len(a)):
    for j in range (0,len(a)-1):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
            swap+=1
print("Array is sorted in",swap,"swaps.")
print("First Element:",a[0])
print("Last Element:",a[len(a)-1])