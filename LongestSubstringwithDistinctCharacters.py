

# Longest Substring with Distinct Characters



def lswdc(str):
    winstrt=0
    ch_freq={}
    maxlen=0
    for winend in range(len(str)):
        right_char=str[winend]
        if right_char not in ch_freq:
            ch_freq[right_char]=0
        ch_freq[right_char]+=1
        while ch_freq[right_char]>1:
            left_char=str[winstrt]
            ch_freq[left_char]-=1
            if ch_freq[left_char]==0:
                del ch_freq[left_char]
            winstrt+=1
            maxlen=max(maxlen, winend-winstrt+1)
        
    
    return maxlen

def commandline():
    x=lswdc("abcvervtvyivmopcvxhvbuvzbvaqcvbvnjgvhde")
    print(x)

commandline()
