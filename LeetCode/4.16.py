
row=0
col=0
nums=[]

def right(n,m):
    global row,col
    while col<m-2:
        col+=2
        if nums[row][col]=='*':
            nums[row][col]='.'
        else:
            break

def down(n,m):
    global row,col
    while row<n-2:
        row+=2
        if nums[row][col]=='*':
            nums[row][col]='.'
        else:
            break

def left(n,m):
    global row,col
    while col>1:
        col-=2
        if nums[row][col]=='*':
            nums[row][col]='.'
        else:
            break

def up(n,m):
    global row,col
    while row>1:
        row-=2
        if nums[row][col]=='*':
            nums[row][col]='.'
        else:
            break

def main():
    n=3
    m=3 # 处理输入
    global nums
    nums1=["**.",".*.","***"]
    nums=[]

    for item in nums1:
        nums.append(list(item))

    global row,col
    result =0
    for i in range(n):
        for j in range(m):
            if nums[i][j]=='*':
                nums[row][col]='.' # 新加这一行
                row=i
                col=j
                result+=1
                right(n,m)
                down(n,m)
                left(n,m)
                up(n,m)
                right(n,m) # 这四行重复一遍
                down(n,m)
                left(n,m)
                up(n,m)
                
    print(result)

    return 

if __name__ == '__main__':
    main()






