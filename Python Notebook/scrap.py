def idk(self, nums):

    # maybe if the rightmost number isn't greater than the current one, then we have to look at other subarray

    left = 0
    right = len(nums) - 1

    while (left <= right):
        mid = (left + right) // 2
        if nums[mid+1 % len(nums)-1] < nums[mid]: return nums[mid+1 % len(nums)-1]
        if nums[mid] > nums[right]: left = mid + 1
        else: right = mid - 1
