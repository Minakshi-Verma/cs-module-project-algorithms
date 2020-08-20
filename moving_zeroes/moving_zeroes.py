'''
Input: a List of integers
Returns: a List of integers
'''
#-----------
## Instructors notes
# '''
# what if we had a pointer that started at the beginning
# and a pointer that started at the end
# and they moved towards each other in the middle?
# ​
# if the left pointer "sees" a zero and the right pointer "sees" a non-zero
# swap
# ​
# if the left sees a non-zero increment
# if the right sees a zero increment
# '''
# ​
# def moving_zeroes(arr):
#     # left pointer at the beginning
#     # right pointer at the end
# ​
#     # loop until left and right pointers meet or right pointer passes the left pointer
#         # swap situation:
#         # left sees zero and right sees non-zero
#             # swap the items
#             # increment left
#             # decrement right
#         # non-swap situation
#             # if left sees non-zero
#                 # increment left
#             # if right sees zero
#                 # decrement right
# ​
#     return arr

#-----------
def moving_zeroes(arr):
    zerovalue_item =0
      
    for i in range(len(arr)):
        # if there are items with zero value, remove them, then append them in the end
        if arr[i]==zerovalue_item:       
            arr.remove(zerovalue_item)
            print(len(arr))
            arr.append(zerovalue_item)        
            print(arr)
           # if no zero item, return the original array              
        else:
            print(arr)                 
            
    return arr

    


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]


    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")