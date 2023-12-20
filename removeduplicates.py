
def remove_duplicates(list1,list2):
    for i in list1:
        if(i not in list2):
             list2.append(i)
    return list2
list1=[1,2,3,4,1,3,6,8,6]
list2=[]
result=remove_duplicates(list1,list2)
print(result)
