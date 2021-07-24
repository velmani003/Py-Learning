#Basic operations on strings
name="Loki"
new_name="Appu"
info="""He is Thor's brother but villan in movies"""
print(f' name is: {name} \n new name is : {new_name} \n info is: {info}')

my_code_lang="Python"
print(f'\n{my_code_lang}')
print(my_code_lang[5])
print(my_code_lang[-6])

#Slicing of a string
print(my_code_lang[0:3])
my_str="My fav Colour is purple"
print(my_str[4:9])

#Delete operation in string(Entire string we can del but we can't del a part of a string)
#Strings are immutable
#Length of a string
my_new_str=len("I would like to fly with my wings of hope")
print(f'Length of the string: {my_new_str}')

#Add or concatenate two strings
my_str1="Learn to Live"
my_str2=" with a positive vibes"
my_str3=my_str1[6:10]+my_str2[3:7]
print(my_str3)

#join function
str1="Happy"
str2="*".join(str1)
print(str2)

#Center
f1="Happy"
f2="day"
f3="enjoy it"
print(f1.center(20))
print(f'{f1.center(5)} {f2.center(5)} {f3.center(5)}')

#zfill --> zero fill padding zeros in front of the given string
print(f3.zfill(10))