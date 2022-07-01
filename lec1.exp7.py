

# Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
# Output: 6
# Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

def max_sub_allone(list,k):
    winstrt=0
    maxone=0
    maxlen=0
    for winend in range(len(list)):
        rbool=list[winend]
        if rbool:
            maxone+=1
        if winend-winstrt+1-maxone>k:
           lbool=list[winstrt]
           if lbool:
                maxone-=1
           winstrt+=1
        maxlen=max(maxlen,winend-winstrt+1)
    return maxlen

def cmd_line():
    Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]; k=2
    L=max_sub_allone(Array,k)
    print(L)
cmd_line()
    