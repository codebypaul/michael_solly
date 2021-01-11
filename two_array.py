def two_array(array_one,array_two):
    array_one.sort()
    array_two.sort()
    if len(array_one) != len(array_two):
        return []
    output_list = []
    # linear time complexity
    for i in range(len(array_one)):
        if array_one[i] == array_two[i]:
            output_list.append(array_one[i])
    return output_list

array_one = [0, 1, 4, 5, 8]
array_two = [0, 2, 7, 9, 4]

print(two_array(array_one,array_two))