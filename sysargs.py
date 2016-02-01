
import sys

a = ['Impinge','Mohali','Python','JAVA']
print a

choice = sys.argv
for x in choice:
    try:
        x = int(x)
        print a[x]
    except:
        print "Iam in Exception :",x
#for x in a:
#    print x



