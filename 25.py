t=0
while t<5:
    for i in range(1230411,100000000,13):
        s= str(i)
        if str(i)[-1]=="9" and s[:3]=="123" and str(i).count("4"):
            print(i,i//13)
            
