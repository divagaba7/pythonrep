



def main():
     print("Main func calling")
   
     header()
     strings()
    
def header():
     print"""
1.simple
2.Reverse"""
def strings():
     a=raw_input("Enter first string:>")
     b=raw_input("Enter second string:>")
     choice(a,b)
def choice(a,b):
     choice=input("Enter your choice:>")
     if choice==1:
         print a+b
     else :
         print b+a
main()   
