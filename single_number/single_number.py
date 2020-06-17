'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):

    # Your code here
    # Array can not be empty, so len(arr)>0
    # All the numbers will have a duplicate except for 1
    # dict.fromkeys will remove all the listduplicates
    # arr1 = list(dict.fromkeys(arr))
    # print(arr1)
  
    from collections import Counter
     

    dict_arr = Counter(arr)
    print(dict_arr)
    result = [k for k, v in dict_arr.items() if v<2]
    print(result)
    print(type(result))  
    return result[0]    


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")