def SELECTION_SORT(array):                          #sorting the array by  using Selection_Sort

    for i in range(0,length- 1):                    #(outer loop ) which Traversthrough all array elements started from 0 to length-1 (index)
        minn = i
        for j in range(i + 1, length):              #(inner loop) to check minimum element 
             if array[j] < array[minn] :                                  
                minn = j     
        if (minn != i):                             #swapping values if minn is not equal to index 'i'
              array[i], array[minn] = array[minn], array[i]     #swapping to place the  minimum element at the correct position

length = int(input("Enter the length of array : "))             # take input the length of the array from the user
print("Enter one by one elements of your unsorted array :")
array = [int(input(f"Enter {k+1} element :")) for k in range(length)]   # collecting the array elements
print("Your given array is:", array)                                  # displaying the unsorted array
SELECTION_SORT(array)                                   #call the ‘selection_sort’ function 
print ("Your sorted array is :", array)                     # displaying the sorted array
