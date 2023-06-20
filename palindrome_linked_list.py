# from typing import str
import re

class ListNode:
    def __init__(self,value=0, next=None):
        self.value = value
        self.next = next

class solution:
    
    def is_palindrome( s :str) -> bool:
       
        s1 = re.sub("[^a-zA-Z0-9]" ,'',s) 
        s1.lower()
        # s = s.replace(/[^a-zA-Z]+/g, " ").toLowerCase().replace(/\s+/g, '');
        return s1 == s1[::-1]
    
    def isPalindrome (  head:ListNode) -> bool : 
        nums =[]
        
        while head:
            nums.append(head.value)
            head =head.next
        
        l ,r = 0 , len(nums) -1
        while l <= r:
            if nums[l] != nums[r]:
                return False 
            l +=1
            r -= 1
        return True