file=open("/content/sequence (4).fasta","r")
f=file.readlines()
print(f)
str=""
for i in range(1,len(f)):
    c=f[i].rstrip()
    str=str+c
print("\n",str)
print("The length of the string:",len(str))

lis=[]
for i in  range(0,len(str)-2):
    k=str[i:i+3]
    lis.append(k)
print(lis)
print("count of 3mer:",len(lis))

lis1=[]
for i in  range(0,len(str)-4):
    k=str[i:i+5]
    lis1.append(k)
print(lis1)
print("count of 5mer:",len(lis1))