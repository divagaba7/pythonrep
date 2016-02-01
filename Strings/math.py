
header =  """ 
	
	CALCULATOR

1.Addition
2.Subtraction
3.Multiply

"""
abc="""*****************************************
*$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"""


a = input("Enter Fisrt number")
b = input("Enter Secodn Number")

print header

choice = input("Enter Your Choice:->")

if choice == 1:
    
    print "User want to Add"
    print a+b
elif choice == 2:
    print "User wants to subtract"
    print a-b
elif choice == 3:
    print "User want to Multipy"
    print a*b
else:
    print "Bad Choice"
    print abc

print "Thank you :)"


