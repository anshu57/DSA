# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        si, ei = 0, l - 1
        res = []
        while si < ei:
            newtarget_3 = target - nums[si]
            smallAns = self.threeSum(nums, newtarget_3, si + 1, ei)
            self.createAns(nums[si], smallAns, res)
            si += 1
            while si < ei and nums[si] == nums[si - 1]:
                si += 1

        return res
        
    def createAns(self, fixNumber, smallAnsList, res):
        for innerList in smallAnsList:
            innerList.append(fixNumber)
            res.append(innerList)    
        
    def threeSum(self, arr_3: List[int], target_3: int, si: int, ei: int) -> List[List[int]]:
        ans_3 = []
        while si < ei:
            newtarget_2 = target_3 - arr_3[si]
            smallAns_1 = self.twoSum(arr_3, newtarget_2, si + 1, ei)
            self.createAns(arr_3[si], smallAns_1, ans_3)
            si += 1
            while si < ei and arr_3[si] == arr_3[si - 1]:
                si += 1

        return ans_3
            
        
    def twoSum(self, arr: List[int], tar: int, si: int, ei: int) -> List[int]:
        ans = []
        while si < ei:
            sum_ = arr[si] + arr[ei]
            if sum_ == tar:
                ans.append([arr[si], arr[ei]])
                si += 1
                ei -= 1

                while si < ei and arr[si] == arr[si - 1]:
                    si += 1
                while si < ei and arr[ei] == arr[ei + 1]:
                    ei -= 1

            elif sum_ < tar:
                si += 1
            else:
                ei -= 1

        return ans

    

    