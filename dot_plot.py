v="""AAASAGAPWVPVWTAASCALLAHVRTDALREDVGDQAANRVDEPLISHPGLASYRVRDLPDGVVSGDFNY
VINLLVHRMGQCLPRSAAAVALNTFPGLDPPDVTAALAEILPNCVPFGPYHLLLAEDDADTAAPADPHGC
"""
a=len(v)
print(a)

l="""AAASAGAPWVPVWTAASCALLAHVRTDALREDVGDQAANRVDEPLISHPGLASYRVRDLPDGVVSGDFNY
VINLLVHRMGQCLPRSAAAVALNTFPGLDPPDVTAALAEILPNCVPFGPYHLLLAEDDADTAAPADPHGC
"""
b=len(l)
print(b)

for i in range (0,len(l)):
    for j in range(0,len(l)):
        if(l[i]==v[j]):
            print(".",end='')
        else:
            print(" ",end='')
    print("\n")