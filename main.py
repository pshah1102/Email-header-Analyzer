
f=open('header.txt')
returnpath=[]
From=[]
for line in f:
    if(line.startswith("Return")):
        str=line
        returnpath=str.split()
        #print(returnpath)
    if (line.startswith("From")):
        str = line
        # From= str.split()
        From.append(str)
       # print(From)
    if (line.startswith("Subject")):
        str = line
        # From= str.split()
        From.append(str)
        #print(From)
    if (line.startswith("DKIM")):
         str = line
         From.append(str)
       # print(From)
    if (line.startswith("Authentication")):
        str = line
        From.append(str)
        print(From)
    if (line.startswith("Received")):
        str = line
        str.find("envelope")
        # From= str.split()
        From.append(str)

string2='\n'.join(returnpath)
file1=open("result.txt",'w')
s1='\n'.join(From)
file1.write(s1)
file1.write(string2)
f.close()
