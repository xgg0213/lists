# Create a function that takes a list of elements and return the first and last
# elements as a new list.

# Write your function here.
def first_last(input_list):
    # new_list=[]
    # new_list.append(input_list[0])
    # new_list.append(input_list[len(input_list)-1])
    # return new_list
    return list([input_list[0], input_list[len(input_list)-1]])

print(first_last([5, 10, 15, 20, 25]))            #> [5, 25]
print(first_last([13, None, False, True]))        #> [13, True]
print(first_last([None, 4, "6", "hello", None]))  #> [None, None]