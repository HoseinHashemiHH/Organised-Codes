

def max_subarr(arr,k):
    l=[]
    winstrt,winsum=0,0
    for i in range(len(arr)):
        winsum+=arr[i]
        if i>=k-1:
            l.append(winsum)
            winstrt+=1
            winsum-=arr[i-k]
    return max(l)
ar=[2, 1, 5, 1, 3, 2]; k=3 
print(max_subarr(ar,k))