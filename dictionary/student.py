aa={ 'Name':'divya',
     'class':'Btech',
     'roll no':17,
     'address':'Mohali'
    }
bb={'Name' : 'kiran',
    'class': 'MCA',
    'roll no':19,
    'address':'JAL'
   }
studen_data="""
1.search data
2.Quit"""

print studen_data

status = True
while status == True:
    choice=int(input("Enter your choice:>"))
    print choice
    if choice == 1:
       print "You are trying to search data"
       a=int(input("Enter your roll no:>"))
       mydict={ 
                17:aa,
                19:bb
               }
       try:
          tmp =  mydict[a]
          print "Name:", tmp['Name']
          print "Class:",tmp['class']
          print "roll no:", tmp['roll no']
          print "Address:", tmp['address']
       except: 
          print ("Not available")
        
    elif choice==2:
       print "You request to quit"
       break
    else: 
       print("Bad choice")

  







 


         
         
        
  

    



