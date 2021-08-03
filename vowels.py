#Count the vowels
vowels='aeiou'
ip_str='Have a wonderful day'
ip_str=ip_str.casefold()
count={}.fromkeys(vowels,0)
for char in ip_str:
    if char in count:
        count[char]+=1
print(count)

