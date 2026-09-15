class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0 and n > 0:
            for i in range(n):
                nums1[i] = nums2[i]
        else:
            valid_nums = []
            
            for i in range(m):
                valid_nums.append(nums1[i])
            
            results = []
            i, j = 0, 0
            while i < len(valid_nums) and j < len(nums2):
                if valid_nums[i] <= nums2[j]:
                    results.append(valid_nums[i])
                    i += 1
                else:
                    results.append(nums2[j])
                    j += 1
            
            while i < len(valid_nums):
                results.append(valid_nums[i])
                i += 1

            while j < len(nums2):
                results.append(nums2[j])
                j += 1

            for i in range(len(results)):
                nums1[i] = results[i]




        
            

