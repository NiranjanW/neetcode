
from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    
    prefix = strs[0]
    # print(prefix)
    
    for idx in range (1,len(strs)):
        j = 0
        new_prefix= ''
        for ch in  strs[idx]:
            if j < len(prefix) and ch == prefix[j]:
                    new_prefix += ch
            else:
                break
            j += 1
        prefix = new_prefix
    return prefix
            
        
    # for str in strs:
        
    #     for chr in str:
    #         print(chr)
        
    
    
    
if __name__ == '__main__':
     
     strs = ["flower","flow","flight"]
     strs1 = ["dog","racecar","car"]
     
     print(longestCommonPrefix(strs)    )