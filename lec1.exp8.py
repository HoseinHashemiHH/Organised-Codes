

# Input: String="oidbcaf", Pattern="abc"
# Output: true
# Explanation: The string contains "bca" which is a permutation of the given pattern.

# Example 2:

# Input: String="odicf", Pattern="dc"
# Output: false
# Explanation: No permutation of the pattern is present in the given string as a substring.

# Example 3:

# Input: String="bcdxabcdy", Pattern="bcdyabcdx"
# Output: true
# Explanation: Both the string and the pattern are a permutation of each other.

# Example 4:

# Input: String="aaacb", Pattern="abc"
# Output: true
# Explanation: The string contains "acb" which is a permutation of the given pattern.

def is_comb_sub(string,ptrn):
    comb={}
    for p in ptrn:
        if p not in comb:
            comb[p]=0
        comb[p]=1
    sumb=comb.copy()
    c_f={}
    winstrt=0
    for winend in range(len(string)):
        rchar=string[winend]
        if rchar not in comb:
            sumb=comb.copy()
            continue
        elif rchar not in sumb:
            pass
        else:
            sumb[rchar]-=1
        if rchar not in sumb:
            pass
        else:
            if sumb[rchar]==0:
               del sumb[rchar]
        if len(sumb)==0:
                return True
        if winend-winstrt+1>len(ptrn):
            lchar=string[winstrt]
            if lchar in sumb:
                sumb[lchar]+=1
            winstrt+=1
    return False

def cmd_line():
    String="oidbcaf"; Pattern="abic" 
    bul=is_comb_sub(String,Pattern)
    print(bul)
cmd_line()
    

        


