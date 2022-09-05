from unittest import result

f=open("Biology.txt","r")
f2=open("Biology_new.txt","w")

count=0
for data in f:
    print(data)
    x=data.replace(" ","_").strip()
    count+=1
    # data1= x,"=",count
    data1=(f"{x}={count}")
    f2.write(data1+"\n")
