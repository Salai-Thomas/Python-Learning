# Tuple VS List

# List ==> mutable      //ordered data strucuture
# tuple ==> immutable   //ordered data structure

create_tuple = ("Aung aung",'Maung Maung')
# create_tuple[0] = "kyaw Kyaw" # TypeError: 'tuple' object does not support item assignment
# print(create_tuple)
# print(type(create_tuple)) # <class 'tuple'>

create_list = ["Aung Aung","Maung Maung"]
create_list[0] = 'Kyaw Kyaw' # No Error
print(create_list)


#packing tuple
# new_tuple = 1,2,3
# print(type(new_tuple))

#tuple upacking
# one_tuple,two_tuple,three_tuple = new_tuple
# print(one_tuple)