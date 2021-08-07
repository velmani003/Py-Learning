def repeated_digit(n):
    a=[]
    
    while n!=0:
        d=n%10
        
        if d in a:
            return 0
        a.append(d)
        n=n//10
    return 1

def calculate(L,R):
    answer=0
    for i in range(L,R+1):
        answer = answer+repeated_digit(i)
    return answer

L=0
R=100

print(calculate(L, R))   
    

