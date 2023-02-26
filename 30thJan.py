#Q1.

marks = int(input("Input value : "))

if(marks>90):
    print("Your Grade is A")
elif(marks>80 and marks <=90):
    print("Your Grade is B")
elif(marks>=60 and marks <=80):
    print("Your Grade is C")
elif(marks<60):
    print("Your Grade is D")
else:
    print("Invalid input")    


#Q2

cost_price = int(input("input the cost price of bike : "))

if(cost_price>100000):
    tax = 15 * cost_price/100
    print("Road tax is = ", tax)
elif(cost_price > 50000 and cost_price<=100000):
    tax = 10 * cost_price/100
    print("Road tax is = ", tax)
elif(cost_price <= 50000):
    tax = 5 * cost_price /100
    print("Road tax is = ", tax)
else:
    print("Invalid Input")


#Q3 

city = input(" Input city name : ")
monuments = { "Delhi" : "Red Fort" , "Agra":"Taj Mahal" , "Jaipur" : "Jal Mahal" , "Patna":"Golghar" , "Amritsar" : "Golden Temple" , "Mumbai" : "Zuhu Beach" } 
print(monuments[city]) 

#Q4
num = int(input("Input a number : "))
count=0
for i in range(num):
    if(num>10):
        num = num//3
        count += 1
print(count)

#Q5
'''
Python While Loop is used to execute a block of statements repeatedly until a given condition is     
satisfied. And when the condition becomes false, the line immediately after the loop in the program is  
Executed.
       
The while statement lets you repeat a statement until a specified expression becomes false.
'''

#Q6.

'''
Square pattern printimg in python 
*  *  *  * 
*  *  *  *
*  *  *  *
*  *  *  *

'''

num = int(input("Input the number : "))
i = 1
while i <= num:
    j = 1
    while j <= num:
        print("*",end = " ")
        j += 1
    print()
    i += 1 
    





#Q7.

num = 10
while num > 0 :
    print(num)
    num -= 1
    

