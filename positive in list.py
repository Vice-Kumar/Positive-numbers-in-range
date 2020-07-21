"Program to print all positive numbers in a given range"
# creating an empty list 
lst = [] 
  
# number of elemetns as input 
n = int(input("Enter number of elements : ")) 
  
# iterating till the range 
for i in range(0, n): 
    e = int(input()) 
  
    lst.append(e) # adding the element 
      

for num in lst: 
      
    # checking condition, if element positive then print
    if num >= 0: 
       print(num, end = ", ") 
