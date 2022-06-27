

from numpy import signedinteger


def max_sub_k(list:list,k:signedinteger)->int:
    winstrt=0
    total=0
    l=[]

    for winend in range(len(list)):
        num=list[winend]
        total+=num
        if winend>=k-1:
            l.append(total)
            total-=list[winstrt]
            winstrt+=1
    return max(l)


# Input: [2, 1, 5, 1, 3, 2], k=3 
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].

# Example 2:

# Input: [2, 3, 4, 1, 5], k=2 
# Output: 7
# Explanation: Subarray with maximum sum is [3, 4].

def cmd_line():
    list=[2, 1, 5, 1, 3, 2]; k=2
    print(max_sub_k(list,k))
cmd_line()