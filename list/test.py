num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
new_num_list1 = []
new_num_list2 = []

while i < len(num_list):
    if ((num_list[i] % 2) == 0):
        new_num_list1.append(num_list[i])
    i += 1
print(new_num_list1)

for i in num_list:
    if(i % 2 == 0):
        new_num_list2.append(i)
print(new_num_list2)
