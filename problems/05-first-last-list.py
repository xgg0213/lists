# Create a function that returns the sum of the first value in the first list
# and the last value of the second list.

# Write your function here.
def sum_first_last_list(list1, list2):
    return list1[0]+list2[len(list2)-1]

print(sum_first_last_list([1, 2, 3], [5, 8, 9]))     #> 10
print(sum_first_last_list([53, 26], [5]))            #> 58
print(sum_first_last_list([9], [5, 8]))              #> 17
print(sum_first_last_list([64], [5, 6, 2]))          #> 66