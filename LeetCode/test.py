

# nums是输入的数组
nums=[3,3,8,9,2,1,3,3]
left=0
right=len(nums)-1
result=0 # 加上这一句
while nums[left]<nums[left+1]:
    left+=1
while nums[right]<nums[right-1]: # 大于变小于
    right-=1
index=0
while left<right:
    if nums[left]<=nums[right]:
        index=left+1
        if index==right:
            break
        ##---------------------------------
        if nums[index]>nums[left]:
            left+=1
            continue
        ##--------------------------------
        result+=(nums[left]-nums[index]+1)
        nums[index]=nums[left]+1
        left+=1
    else:
        index=right-1
        if index==left:
            break
        ##----------------------------
        if nums[index]>nums[right]:
            right-=1
            continue
        ##----------------------------
        result+=(nums[right]-nums[index]+1)
        nums[index]=nums[right]+1
        right-=1

print(result)

