# https://leetcode.com/problems/find-the-duplicate-number/
# 2020 3.29

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # # v1  875ms 28MB using array a as hashmap, small extra memory
        # a=list(range(1,len(nums)))
        # for item in nums:
        #     if a[item-1]==item:
        #         a[item-1]=0
        #     else:
        #         return item

        # # v1.1 847ms 32.3MB using real hashmap, with a lot of extra memory
        # a={}
        # for item in nums:
        #     if item not in a:
        #         a[item]=1
        #     else:
        #         return item

        # v1.2 set seen item to negative instead of recording them in a new array
        # https://leetcode.com/problems/find-the-duplicate-number/discuss/705111/summary-7-solutions-%2B-consice-explanation-and-complexity-analysis
        for num in nums:
            if nums[ abs(num) ] < 0:
                ans = abs(num)
                break
            nums[ abs(num) ] = -nums[ abs(num) ]
        # restore nums
        for i in range(len(nums)):
            nums[i] = abs(nums[i])
        return ans

        
        # # v2 810ms 27.9MB using built-in sort(), no extra memory
        # nums.sort()
        # for i in range(1,len(nums)):
        #     if nums[i]-nums[i-1]==0:
        #         return nums[i]
        
        # v3 faster, 592ms 34.3MB using set() but with a lot of extra memory
        # my best solution
        a=set(nums)
        return (sum(nums)-sum(a))//(len(nums)-len(a))

        # # v3.1 oneliner but slower, 884ms 34.4MB, slow because it neet to calculate set(nums) twice
        # return (sum(nums)-sum(set(nums)))//(len(nums)-len(set(nums)))

        # v4 copied, really interesting with no extra memory
        # see this list nums as a linked listnode. using two-pointer
        # slow=nums[slow] fast=nums[nums[fast]]
        # an array with number from [1,n] and length n+1 can be seen as a linked list with cycle
        # this method is the same as 142. Linked List Cycle II
        # https://leetcode.com/problems/find-the-duplicate-number/discuss/72846/My-easy-understood-solution-with-O(n)-time-and-O(1)-space-without-modifying-the-array.-With-clear-explanation.
        # https://keithschwarz.com/interesting/code/?dir=find-duplicate
        slow=fast=0
        while 1:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                fast=0
                while slow!=fast:
                    slow=nums[slow]
                    fast=nums[fast]
                return slow

        # v5 copied , adapted binary search using pigeonhole principle
        # https://leetcode.com/problems/find-the-duplicate-number/discuss/72844/Two-Solutions-(with-explanation)%3A-O(nlog(n))-and-O(n)-time-O(1)-space-without-changing-the-input-array
        low=1
        high=len(nums)-1
        while low<high:
            mid=(low+high)//2
            count=0
            for item in nums:
                if item<=mid:
                    count+=1
            if count<=mid:
                low=mid+1
            else:
                high=mid
        return low

        # v6 copied, bit manipulation, rather slow 
        seen=0 # a number to record all seen numbers by 1 
        for item in nums:
            if seen&(1<<item): # if the tiem bit in seen is 1, means item has been seen before
                return item
            seen = seen|(1<<item) # if have seen item, set the seen bit to 1
        
        # v6.1 hard to understand, bit manipulation in groups
        # https://leetcode.com/problems/find-the-duplicate-number/discuss/72872/O(32*N)-solution-using-bit-manipulation-in-10-lines