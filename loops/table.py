import sys
b=(2,4,6,8,10,12,14,16,18,20)
c=(3,6,9,12,15,18,21,24,27,30)
d=(0)
e=(1,2,3,4,5,6,7,8,9,10)
a=[d,e,b,c]
print a
choice=sys.argv
for x in choice :
    
     
    try:
        x = int(x)
        print a[x]
    except:pass
