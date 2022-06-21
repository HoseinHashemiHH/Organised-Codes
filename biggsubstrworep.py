# Given a string, find the length of the longest substring in it with no
#  more than K distinct characters.
# You can assume that K is less than or equal to the length of the given string.

from matplotlib.cbook import ls_mapper


def smallsubarray(str,k):
    winstrt=0
    char_fr={}
    maxlen=0
    for windend in range(len(str)):
        right_char=str[windend]
        if right_char not in char_fr:
            char_fr[right_char]=0
        char_fr[right_char]+=1

        #change the window size
        while len(char_fr)>k:
            left_char=str[winstrt]
            char_fr[left_char]-=1
            if char_fr[left_char]==0:
                del char_fr[left_char]
            winstrt+=1
    maxlen=max(maxlen,windend-winstrt+1)
    return maxlen

def main():
  print("Length of the longest substring: " 
           + str(smallsubarray("araaci", 2)))
  print("Length of the longest substring: " 
           + str(smallsubarray("araaci", 1)))
  print("Length of the longest substring: " 
           + str(smallsubarray("cbbebi", 3)))

main()
    





