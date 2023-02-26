

#1. Use a for loop when you know the loop should execute n times. 
# Use a while loop for reading a file into a variable. Use a while loop when asking for user input. 
# Use a while loop when the increment value is nonstandard.

#Eg :-       While loop 
i = 1
while i < 6:
    print(i)
    i += 1
    
#Eg :-     For loop 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

#2.    
#Sum of First 10 natural number  using for loop 
        
sum = 0
for i in range(1,11):
    sum  += i
    print(i,end=" ")
print("sum = " , sum)    

#product of First 10 natural number  using for loop 

product = 0
for i in range(1,11):
    product  *= i
    print(i,end=" ")
print("product = ", product)  

#Sum of First 10 natural number  using while loop 

sum = 0
num = 1
while num<11:
    sum  += num
    print(num ,end=" ")
print("sum = " , sum) 

#Sum of First 10 natural number  using while loop 

product = 0
num = 1
while num<11:
    product  *= num
    print(num ,end=" ")
print("Product = " , product) 

#Q3. 

unit = int(input("input num = "))        
result=0
if unit<=100:
    result = 4.5*unit     
elif unit<=200:
    result = (100*4.5) + ((unit-100)*6)
elif unit<=300:
    result = (100*4.5) + (100*6) + ((unit-200)*10)
else:
    result = (100*4.5) + (100*6) + (100*10) +((unit-300)*20)
    
print("Result = ",result)  

#Q4.
    
cubelist = []  
l = list(range(1,101))
for i in l:
    result = i**3
    if result%4==0 or result%5==0:
        cubelist.append(i)
print(cubelist)        

# #Q5.

data = "I want to become a data scientist"
count = 0

for vowel in data.lower():
    if vowel=="a" or vowel=="e" or vowel=="i" or  vowel=="o" or vowel=="u":
        count += 1
print("Numbers of vowels in this string is = ",count)    
    