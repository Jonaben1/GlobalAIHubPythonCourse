#a program to reverse half of list
list = [1,2,3,4,5,6]

half_list1= list[:len(list)//2]

print(half_list1)

half_list2 = list[len(list)//2:]


print(half_list2)

reverse_list= half_list2+ half_list1

print(reverse_list)
