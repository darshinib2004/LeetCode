class Solution:
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        result = []
        
        # Three nested loops to generate all triplets
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = [nums[i], nums[j], nums[k]]
                        # Check if the triplet is unique before adding to result
                        if triplet not in result:
                            result.append(triplet)
        
        return result

def _driver():
    # Example usage
    param_1 = [-1, 0, 1, 2, -1, -4]
    ret = Solution().threeSum(param_1)
    print(ret)

# Call the driver function
if __name__ == "__main__":
    _driver()
