#from Scripts.Src.ex_14102024.Literals import my_list
# List
# List - Collection of Items( Duplicate is allowed)
#started with square
my_list= [1,2,3,"Dutta44"]# Same type of data (int)
# my_list2 = [1, True, "Pramod", 12.34]

print(my_list)
print(len(my_list))

my_list[0]
my_list[1]
my_list[2]
my_list[3]
print(my_list[0])
#my_list[10] = "Dutta44" # list assignment index out of range

# Indexing
print("element at the index 0 - ", my_list[2])

print(my_list)
for element in my_list:
    print(element)

for i in range(1,10,1): # [1,2,3,4,5,6,7,8,9]
    print(i)

    #list -> [1,2,3,4,5,6,7,8,9]

    print(" - -------------")
    my_list = [1, 2, 3]

#append()
my_list.append(4)# Append object to the end of the list. append ke through list end me wo digit and word add kar sakte ho.
my_list.append(100)
my_list.append("cesur")
print(my_list)

#extend()
my_list.extend([7, 8, 9])
my_list.extend([10])
my_list.extend(["Ankush"])
print(my_list)
print(len(my_list))

#insert()
my_list.insert(0,"Almdaar")
print(my_list)
print(len(my_list))
my_list[1] ="Ashish"
print(my_list)

#remove
my_list.remove("Ashish")
print(my_list)


# copy mylist
my_copy_list= my_list.copy()
print(my_list)
print(my_copy_list)

my_list.clear()
print(my_list)
print(my_copy_list)

my_copy_list.remove("cesur")
my_copy_list.remove("Almdaar")
my_copy_list.remove("Ankush")
my_copy_list.sort()
print(my_copy_list)
my_copy_list.sort(reverse=False)
print("Sorted list (descending  order):", my_copy_list)

my_copy_list.reverse()
print(my_copy_list)

name = "cesur"
name = name.upper()
print(name)

l1=[1,2,3]
l2=[100,214,3.1]
l3=l1+l2
print(l3)