
def BianrySearch(list,item):
    low=0
    high=len(list)-1

    while low<=high:
        mid=(low+high)//2
        guess=list[mid]
        if guess == item:
            return mid #return the position
        if guess>item:
            high=mid-1
        else:
            low=mid+1
    return None




list1=[1,2,3,4,8,9]

list2=list(range(-1000,1000000))

print(BianrySearch(list2,3046))