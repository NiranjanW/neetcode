from typing import List

nums = [0,0,1,1,1,2,2,3,3,4]


def removeDuplicates( nums: List[int]) -> int:
    ans=1
    for i in range(1, len(nums)):
        
        if nums[ans] != nums[i]:
            # nums[ans] = nums[i] 
            ans += 1
    return ans

def removeDup(nums: List[int]) -> int:
        ans = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]: 
                # nums[ans] = nums[i] 
                ans += 1
        return ans

if __name__ == "__main__":
    print(removeDup(nums))
    
    
