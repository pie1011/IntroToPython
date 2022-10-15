def bubble_sort(list):
    # your code here
    return list

def is_sorted(list):
    for index in range(0, len(list)-1):
        if list[index] > list[index+1]:
            print("List is NOT sorted!!!")
            return False

    print("List is sorted.")
    return True


# Code to test function
sample_list = [1, 5, 2, 6, 7]

print(f"Unsorted list: {sample_list}")
bubble_sort(sample_list)
print(f"Sorted list:   {sample_list}")
is_sorted(sample_list)