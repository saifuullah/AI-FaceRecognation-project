# initializing list  
test_list = [1, 0, 0] 
    
# converting binary list to integer  
res = int("".join(str(x) for x in test_list), 2) 
  
# printing result  
print ("The converted integer value is : " +  str(res)) 