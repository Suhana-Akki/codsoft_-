#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("\n SIMPLE CALCULATOR")
while True:
    a=int(input("Enter 1st number: "))
    b=int(input("Enter 2nd number: "))  
    print(" select from following operations")
    print("1.ADD")
    print("2.SUBSTRACTION")
    print("3.MULTIPLICATION")
    print("4.DIVISION")
    print("5.MODULUS")
    print("6.QUIT")
       
    choice=input("whats your choice ")
         
    if(choice=="1"):
        c=a+b
        print(f"The Sum 0f {a} & {b} is {c}")
            
    elif(choice=="2"):
        c=a-b
        print(f"The Difference between {a} & {b} is {c}")
    elif(choice=="3"):
        c=a*b
        print(f"The Multiplication 0f {a} & {b} is {c}")
    elif(choice=="4"):
        c=a/b
        print(f"The Division 0f {a} & {b} is {c}")
    elif(choice=="5"):
        c=a%b
        print(f"The Modulus 0f {a} & {b} is {c}")
    elif(choice=="6"):
        break
    else:
        print("INVALID CHOOSE ANOTHER")
            


# In[ ]:





# In[ ]:




