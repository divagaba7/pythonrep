


b = (4,5,6,7)


a = [1,2,3,4,5,b]

for x in a:
    ty = str(type(x))
    ty = ty.split("'")
    ty = ty[1]

    if ty == 'tuple':
        for vv in x:
            print vv
    else:
        print x 










