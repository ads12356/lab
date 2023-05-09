#0 , 97 , 97 , 99 , 101 , 103 , 196 , 198 , 198 , 200 , 202 , 295 , 297 , 299 , 299 , 301 , 394 , 396 , 398 , 400 , 400 , 497
spectrum = [0 , 97 , 97 , 99 , 101 , 103 , 196 , 198 , 198 , 200 , 202 , 295 , 297 , 299 , 299 , 301 , 394 , 396 , 398 , 400 , 400 , 497]

print(spectrum)
a = {'G':57 , 'A':71 , 'S':87 , 'P':97 , 'V':99 , 'T':101 , 'C':103 , 'I':113 , 'L':113 , 'H':114 , 'D':115 , 'K':128 , 'Q':128 , 'E':129 , 'M':131 , 'H':137 , 'F':147 , 'R':156 , 'U':163 , 'W':186}
a


one_mer = []
for i in a:
    if a in spectrum:
        print(i)
        one_mer.append(i)
print(one_mer)

two_mer = {}
for i in one_mer:
    for j in a:
        b = a[i]+a[j]
        if b in spectrum:
            print(i+j)
            two_mer[i+j] = b
two_mer 