# Input: [3, 4, 1, 1, 6], S=8 
# Output: 3
# Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] 
# or [1, 1, 6].
import numpy as np
def ssub_g_e(list, s):
    winstrt=0
    sum=0
    l=[]
    for winend in range(len(list)):
        rnum=list[winend]
        sum+=rnum
        while sum>=s:
            l.append(list[winstrt:winend+1])
            lnum=list[winstrt]
            sum-=lnum
            winstrt+=1
    length=[]
    result=[]
    #print(l)
    for lbaby in l:
        length.append(len(lbaby)) 
    for x,lbabe in enumerate(length):
        if lbabe==min(length):
            result.append(l[x])
    return result

def cmd_line():
    li1=[3, 4, 1, 1,19,0.5,0.5,2,1,0,5,8,9]; S=21
    print(ssub_g_e(li1,S))
cmd_line()

    
