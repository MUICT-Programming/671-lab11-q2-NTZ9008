def summation():
    updated_list = []
    for i in range(n):
        updated_list.append(list1[i]+list2[i])
    return updated_list
def find_min_max():
    x = min(summation())
    y = max(summation())
    return (x,y)
list1 = []
list2 = []
n = int(input())
for i in range(n):
    x = int(input())
    list1.append(x)
for i in range(n):
    x = int(input())
    list2.append(x)
print(summation())
print(find_min_max())
