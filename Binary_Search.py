list = [11,22,33,44,55,66,77,88,99,101]
list.sort()
first=0
last=len(list)-1
mid=(first+last)
element = int(input("Enter the number to be searched"))
found=False
while(first<=last and not found):
    mid = (first+last)//2
    if list[mid] == element :
        print(f"Found at location {mid}")
        found=True
    else:
        if element < list[mid] :
            last = mid-1
            
        else:
            first = mid +1
if found == False:
    print("Number Not Found")
    