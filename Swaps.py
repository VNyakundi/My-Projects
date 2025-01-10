# Rearranging nmbers so that every number is bigger than the one before
# We can only swap numbers that are besides each other
# We wanna do this in the fewest number of swaps possible



def rearrange_numbers(arr):
    n = len(arr)
    swaps = 0  # To count the number of swaps
    sorted = False

    while not sorted:
        sorted = True
        for i in range(n-1):
            if arr[i]>arr[i+1]:
                # Swap adjacent elements if the current one is greater than the next
                arr[i],arr[i+1] = arr[i+1],arr[i]
                swaps += 1
                sorted = False  # We made a swap, so it's not sorted yet

    return arr,swaps

# Test the function

numbers = [2,7,3,8,1,4]
sorted_numbers,swap_count = rearrange_numbers(numbers)
print(f"sorted list:{sorted_numbers}")
print(f"total swaps:{swap_count}")