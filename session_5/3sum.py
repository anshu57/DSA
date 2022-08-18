# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.





class Solution:
    def twoSumSolution(self, arr: List[int], tar: int, si: int, ei: int) -> List[int]:
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

    def createAns(self, fixNumber, smallAnsList, res):
        for innerList in smallAnsList:
            innerList.append(fixNumber)
            res.append(innerList)

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        si, ei = 0, l - 1
        res = []
        while si < ei:
            newtarget = 0 - nums[si]
            smallAns = self.twoSumSolution(nums, newtarget, si + 1, ei)
            self.createAns(nums[si], smallAns, res)
            si += 1
            while si < ei and nums[si] == nums[si - 1]:
                si += 1

        return res

