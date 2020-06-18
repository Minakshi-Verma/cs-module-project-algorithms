'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    #return length
    #return mutated array

    zerovalue_item =0

   
    # for i in range(len(arr)):
    #     arr[i]==zerovalue_item       
    #     arr.remove(zerovalue_item)
    #     print(len(arr))
        
    #     arr.append(zerovalue_item)        
    #     print(arr)         
            
    # return arr
      
    for i in range(len(arr)):
        if arr[i]==zerovalue_item:       
            arr.remove(zerovalue_item)
            print(len(arr))
            arr.append(zerovalue_item)        
            print(arr)
        else:
            print(arr)                 
            
    return arr

    


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]


    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")