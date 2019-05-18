import random


f=open("countries.txt","r")
text=f.read()
countries=text.split()
length=len(countries)
while length>1:
    rand1=random.randint(0,length-1)
    rand2=random.randint(0,length-1)
    while rand1==rand2:
        rand2=random.randint(0,length-1)
    print "--> "+countries[rand1]+" faces "+countries[rand2]
    decider=random.randint(0,1)
    if decider==0:
        print "--> "+countries[rand1]+" has been completely defeated\n"
        countries.remove(countries[rand1])
    else:
        print "--> "+countries[rand2]+" has been completely defeated\n"
        countries.remove(countries[rand2])
    length=len(countries)
    d=str(length)
    print "~ "+d+" countries remaining~\n"
print "--> "+countries[0]+" is only country remaining"
    
