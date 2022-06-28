# Input: Fruit=['A', 'B', 'C', 'A', 'C']
# Output: 3
# Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']


# Example 2:

# Input: Fruit = ['A', 'B', 'C', 'B', 'B', 'C']
# Output: 5
# Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

from numpy import c_


def pick_fruit_most(list):
    c_f={}
    winstrt=0
    lengthmax=0
    l=[]
    for winend in range(len(list)):
        rchar=list[winend]
        if rchar not in c_f:
            c_f[rchar]=0
        c_f[rchar]+=1
        while len(c_f)>2:
            lchar=list[winstrt]
            if lchar in c_f:
                c_f[lchar]-=1
            if c_f[lchar]==0:
                del c_f[lchar]
            winstrt+=1
        lengthmax=max(lengthmax,winend-winstrt+1)
        l.append(list[winstrt:winend+1])
    return lengthmax,l

def cmd_line():
    Fruit=['A', 'B', 'C', 'B', 'B', 'C']
    p=pick_fruit_most(Fruit)
    print(p)
cmd_line()