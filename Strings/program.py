a=raw_input("enter first string:->")
b=raw_input("enter second string:->")
header="""@@@@@@@@@@@@@@@@
1. Simple
2. Reverse"""

choice=input("enter your choice:->")
if choice==1:
    print a+b
elif choice==2:
    print b+a
else:
    print("Bad choice") 
  
