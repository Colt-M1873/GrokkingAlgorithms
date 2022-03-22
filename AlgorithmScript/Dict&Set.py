# Two ways to initialte a dict
a=dict()
b={}
a['yi']=1
print(a)
b['yi']=1
print(b)

# Set do not allow duplicate, cannnot have two items with the same value
list1=[8,8,6,7,'fk',1,2,1,3,4,6,6,6,2,5]
print(list1)
set1=set(list1)
print(set1)
# Set is unordered and not subscriptable
# set1[0] will get error message
for i in set1:
    print(i)

