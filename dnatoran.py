n="""ACCATTAAAGAAAATATCATTGGTGTTTCC"""
b=n.replace('A','K').replace('T','A').replace('K','T')
c=b.replace('G','K').replace('C','G').replace('K','C')
d=c.replace('T','U')
print(d)
print(len(n))
m="""CCACACGAAAAGTGTCACTGGCCCCCTCAGGCAAACTTGACTGAACT"""
e=m.replace('A','K').replace('T','A').replace('K','T')
f=e.replace('G','K').replace('C','G').replace('K','C')
g=f.replace('T','U')
print(g)
print(len(m))
S = 0 
P = 0
for i in range (0,len(n)):
    if n[i]=='A' and m[i]=='G' or n[i]=='T' and m[i]=='C':
        print(i,"-->Transition")
        S = S + 1
    elif n[i]=='G' and m[i]=='A' or n[i]=='C' and m[i]=='T':
        print(i,"-->Transition")
        S = S + 1
    elif n[i]=='A' and m[i]=='A' or n[i]=='C' and m[i]=='C':
        print(i,"-->no mutation")
        P = P + 1
    elif n[i]=='G' and m[i]=='G' or n[i]=='T' and m[i]=='T':
        print(i,"-->no mutation")
        P = P + 1
    else :
        print(i,"-->Traversion")
print("number of transitions",S)
print("number of tranversion",30-S-P)
