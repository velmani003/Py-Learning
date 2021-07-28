n=int(input("Terms to be included"))
#first two terms
n1,n2= 0,1
count=0
#Check if the number is valid or not
if n<=0:
    print("Enter a positive integer")
elif n ==1:
    print("The series upto",n,";")
    print(n1)
else:
    print("Fib Seq")
    while count < n:
        print(n1)
        nth = n1+n2
        #updated values
        n1=n2
        n2=nth
        count+=1
        