n=int(input("enter the number of elements in list: "))
list1=list(map(int,input().strip().split()))[:n]
list2=list()
for i in list1:
    if i>0:
        print(i,end=" ")
