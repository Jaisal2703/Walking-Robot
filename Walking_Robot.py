class Dir:
    def __init__(self):
        pass
    def N(self,S,D,X,Y):
        for i in range(len(S)):
            if S[i]=='r':
                D=(D+1)%4
            elif S[i]=='l':
                D=(D-1)%4
            elif S[i]=='w':
                if D==0:
                    Y=Y+(int(S[i+1]))
                elif D==1:
                    X=X+(int(S[i+1]))
                elif D==2:
                    Y=Y-(int(S[i+1]))
                else:
                    X=X-(int(S[i+1]))
            
        print(X," ",Y)
        if D==0:
            D="North"
        elif D==1:
            D="East"
        elif D==2:
            D="South"
        else:
            D="West"
        print(D)
                

import re
s = input("Please enter all required Co-ordinates in a row seperating by  giving SPACE: \n")
z=re.split(' +', s)
X=int(z[0])
Y=int(z[1])
D=str(z[2])
S=str(z[3])
num=""
y=re.split('w+',S)
dir=Dir()
if D=="North":
    D=0
elif D=="East":
    D=1
elif D=="South":
    D=2
elif D=="West":
    D=3
dir.N(S,D,X,Y)