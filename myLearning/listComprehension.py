lst = [2,3,4,5]
new_lst = []

# for num in lst:
#     new_lst.append(num * 2)
#     print(new_lst)

#list comprehension
# new_lst= [num * 2 for num in lst]
# print(new_lst)

even_lst = [even for even in range(1,21) if even % 2 == 0]
print(even_lst)