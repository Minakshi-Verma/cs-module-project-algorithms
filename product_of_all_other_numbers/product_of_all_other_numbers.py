'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    
    product = 1
    # remove the 1st element(arr[0])of the array, multiply arr[1]*arr[2]*arr[3]
    for i in range(len(arr)):
        # if arr[i] == arr[0]:
        # popped = arr.pop(arr[i])
        product= product*arr[i]
    
        # arr.append
        # print(popped)
            
        return product    
        


    # remove the 2nd element (arr[1])of the arrry, multiply arr[0]*arr[2]*arr[3]
    # remove the 3rd element (arr[2])of the arrry, multiply arr[0]*arr[1]*arr[3]
    # remove the 4th element (arr[3])of the arrry, multiply arr[0]*arr[1]*arr[2]
    #return arr


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
   
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
   
