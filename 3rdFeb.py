#1.
# def keyword is used to create a function.

# # eg : -  
#      def Function_name(x):
#          print("statement") 

#      print(function_name(5))  

odd_list=[]
def odd_num():
    
    for i in range(1,25):
        if i%2 != 0:
            odd_list.append(i)
    return odd_list
     
odd_num()
print(odd_list)

#2. 
# We use *args and **kwargs to handle new input data automatically in function. 
# which is by default store as a tuple . 
# basically *args and *kwargs are an arguments which automatocally pass in the 
# functions argument instead of passing manually one by one .