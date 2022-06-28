

# Given a string, find the length of the longest substring, which has all distinct characters.
#  Example 1:

# Input: String="aabccbb"
# Output: 3
# Explanation: The longest substring with distinct characters is "abc".

# Example 2:

# Input: String="abbbb"
# Output: 2
# Explanation: The longest substring with distinct characters is "ab".

# Example 3:

# Input: String="abccde"
# Output: 3
# Explanation: Longest substrings with distinct characters are "abc" & "cde".

from pyrsistent import l


def long_sub_distinct(str):
    winstrt=0
    maxlength=0
    c_f={}
    l=[]

    for winend in range(len(str)):
        rchar=str[winend]
        if rchar not in c_f:
            c_f[rchar]=0
        c_f[rchar]+=1
        while c_f[rchar]>1:
            lchar=str[winstrt]
            if lchar in c_f:
                c_f[lchar]-=1
            winstrt+=1
        maxlength=max(maxlength,winend-winstrt+1)
        l.append(str[winstrt:winend+1])
        
    return maxlength,l

def cmd_line():
     String="salam!manamadam"
     result=long_sub_distinct(String)
     print(result)
cmd_line()

