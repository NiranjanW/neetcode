from typing import List

class Solution:
    def search( nums: List[int], target: int) -> int:
        found = False
        
        for i , val in enumerate(nums):
            if val == target:
                return i
        return -1

    def binSearch(self, nums: List[int], target: int) -> int:
        l,r= 0 , len(nums)-1
        
        val = nums[l]
        
        while l < r :
            mid = l -(l-r) //2
            if nums[mid] >= target:
                r = mid 
            else :
                 l = mid + 1
        
        if nums[l] != target:
            return -1
        return l   
    
    def searchBin(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right = mid-1
            else:
                left = mid+1
        
        return -1  
            
  
            
        
        
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left, right, s):
            if len(s) == n * 2:
                res.append(s)
                return 

            if left < n:
                dfs(left + 1, right, s + '(')

            if right < left:
                dfs(left, right + 1, s + ')')

        res = []
        dfs(0, 0, '')
        return res