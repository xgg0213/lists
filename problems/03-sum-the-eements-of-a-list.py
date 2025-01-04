# Create a function that takes a list and returns the sum of all numbers in the
# list.

# Write your function, here.
def get_sum_of_elements(input_list):
    output=0
    for n in range(len(input_list)):
        output+=input_list[n]
    return output

print(get_sum_of_elements([2, 7, 4]))     #> 13
print(get_sum_of_elements([45, 3, 0]))    #> 48
print(get_sum_of_elements([-2, 84, 23]))  #> 105