#!/usr/bin/env python
# coding: utf-8

# In[1]:


tasks=[]

def ADDD():
    task = input("ENTER TASK TO ADD ")
    tasks.append(task)
    print(f"TASK '{task}' add to list ")
    
def listt():
    if not tasks:
        print("there are no tasks currently ")
    else:
        print("current task:")
        for index,task in enumerate(tasks):
            print(f"task #{index}. {task}")
    
def Remove():
    listt()
    try:
        taskdelete = int(input("enter the # to delete:"))
        if taskdelete >=0 and taskdelete < len(tasks):
            tasks.pop(taskdelete)
            print(f"task {taskdelete} has been removed")
        else:
            print(f"task #{taskdelete} was not found")
    except:
        print("INVALID INPUT")
    
if __name__ == "__main__":
    print("TO DO LIST")
    while True:
        print("\n")
        print(" select from following operations")
        print("1.ADD")
        print("2.REMOVE")
        print("3.NEW")
        print("4.QUIT")
        
        choice=input("whats your choice ")
        
        if(choice=="1"):
            ADDD()
        elif(choice=="2"):
            Remove()
        elif(choice=="3"):
            listt()
        elif(choice=="4"):
            break
        else:
            print("INVALID CHOOSE ANOTHER")
        


# In[ ]:




