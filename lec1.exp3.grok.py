
# Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters is "araa".

def f_distinct_long(str,k):
    winstrt=0
    c_f={}
    maxlen=0
    s=[]
    length=[]
    result=[]
    for winend in range(len(str)):
        rchar=str[winend]
        if rchar not in c_f:
            c_f[rchar]=0
        c_f[rchar]+=1
        
        while len(c_f)>k:
            lchar=str[winstrt]
            if lchar not in c_f:
                c_f[lchar]=0
            c_f[lchar]-=1
            if c_f[lchar]==0:
                del c_f[lchar]
            winstrt+=1
        maxlen=max(maxlen,winend-winstrt+1)
        s.append(str[winstrt:winend+1])
    print(s)
    for sbaby in s:
        length.append(len(sbaby))
    for x,lbabe in enumerate(length):
        if lbabe==max(length):
            result.append(s[x])
    return maxlen,result

def cmd_line():
    str="cababbonab"; k=3
    print(f_distinct_long(str,k))
cmd_line()



