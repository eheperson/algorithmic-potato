class Sort:
    @staticmethod
    def bubble(arr_, n_): # optimize approach
        """
            > Bublesort algorithm implementation
            > Methodology :swapping the adjacent elements if they are in wrong order

            Complexity : O(n^2)

            Pseudo Code:
                > start from the first element of the array
                > move one-by-one to the end
                > compare each pair of array element 
                > stop if whole array is completely sorted in an ascending order

            C/C++ Code :
                void bubble(int arr[], int n){
                    int temp;
                    int i, j;
                    for (i = 0; i < n-1; i++)    
                    for (j = 0; j < n-i-1; j++)
                        if (arr[j] > arr[j+1])
                            temp = arr[j];
                            arr[j] = arr[j+1];
                            arr[j+1] = temp;
                }
            
        """
        for i in range(n_): # traverse through all array elements
            swapped = False
            for j in range(0, n_-i-1): # traverse  from 0 to n-i-1
                if arr_[j] > arr_[j+1] :  # Swap if the element found is greater than the next element
                    arr_[j], arr_[j+1] = arr_[j+1], arr_[j]
                    swapped = True
                if swapped == False: # if no two elements were swapped by inner loop
                    break

    @staticmethod
    def selection(arr_, n_):
        """
            > Selection sort algorithm implementation

            Complexity : O(n^2)

            Pseudo Code:
                > Set MIN to the  0. element of array
                > traverse array to find minimum element
                > swap the finded minimum element with the 0.th position
                > Increment MIN to point to next element
                > Repeat until list is sorted

            C/C++ Code :
                void selection(int arr[], int n){ 
                    int i, j, minIndex; 
                    int temp;
                    for (i = 0; i < n-1; i++){ 
                        minIndex = i; 
                        for (j = i+1; j < n; j++) 
                            if (arr[j] < arr[minIndex]) 
                                minIndex = j; 
                        temp = arr[minIndex];
                        arr[minIndex] = arr[i];
                        arr[i] = temp;
                    } 
                } 
            
        """
        for i in range(n_): # traverse through array
            minIndex = i # set the min index to the 0. element
            for j in range(i+1, n_): # Find the minimum element in remaining
                if arr_[minIndex] > arr_[j]:
                    minIndex = j
            arr_[i], arr_[minIndex] = arr_[minIndex], arr_[i] # Swap the found minimum element with min index

    @staticmethod
    def  merge(arr_, n_):
        """
            > Merge sort algorithm implementation
            > It is an divide an conquer approach
            > It uses recursion

            Complexity : O(nlog(n))

            Pseudo Code:
                > find the index of the middle element
                > divide array from middle
                > call mergeSort for first half
                > call mergeSort for last half
                > merge first and last halves

            C/C++ Code :
                -will be implemented later
            
        """
        if n_ > 1:
            mid = n_//2 # find the midle index
            left = arr_[:mid] # divide array and take first half
            right = arr_[mid:] # divide array and take first half
            Sort.merge(left) ## Sort the first half
            Sort.merge(right) ## Sort the last half
            i = j = k = 0
            while i < len(left) and j < len(left):
                # Copy data to temp arrays L[] and R[]
                if left[i] < right[j]:
                    arr_[k] = left[i]
                    i += 1
                else:
                    arr_[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                # Checking if any element was left on the left side
                arr_[k] = left[i]
                i += 1
                k += 1
            while j < len(left):
                # Checking if any element was left on the right side
                arr_[k] = right[j]
                j += 1
                k += 1

    @staticmethod
    def quick(start_, end_, array_):
        """
            > Quick sort algorithm implementation
            > It is an divide an conquer approach
            > It uses recursion

            Complexity : O(n^2)

            Pseudo Code:
                > Choose the highest index value has pivot
                > Take two variables to point left and right of the list excluding pivot
                > left points to the low index
                > right points to the high
                > while value at left is less than pivot move right
                > while value at right is greater than pivot move left
                > if both step 5 and step 6 does not match swap left and right
                > if left ≥ right, the point where they met is new pivot

            C/C++ Code :
                -will be implemented later
            
        """
        tmpend = end_ # end pointer 
        tmpstart = start_ # start pointer
        tmparray = array_
        if (start_ < end_):
            
            # Initializing pivot's index to start
            pivot_index = tmpstart
            pivot = tmparray[pivot_index]
            while tmpstart < tmpend:
                # run till start pointer crosses end pointer
                # and swap the pivot with element on the end pointer 
                # when start pointer crosses end pointer
                
                while tmpstart < len(tmparray) and tmparray[tmpstart] <= pivot:
                    # increment start pointer till find an greater element than pivot
                    tmpstart += 1
                    
                while tmparray[tmpend] > pivot:
                    # decrement end pointer till find an less element than pivot
                    tmpend -= 1
                
                if(tmpstart < tmpend):
                    # swap the start and end pointer values 
                    # if start and end pointers have not crossed each other
                    tmparray[tmpstart], tmparray[tmpend] = tmparray[tmpend], tmparray[tmpstart]
            
            # Swap pivot element with element on end pointer.
            tmparray[tmpend], tmparray[pivot_index] = tmparray[pivot_index], tmparray[tmpend]
            
            p = tmpend
            Sort.quick(start_, p - 1, array_) # sort elements before partition
            Sort.quick(p + 1, end_, array_) # sort elements after partition
    
    @staticmethod
    def insertion(arr_, n_):
        """
            > Insertion sort algorithm implementation
            > It is an comparison-based sorting algorithm

            Complexity : O(n^2)

            Pseudo Code:
                > start from the first element of array
                > pick 2th element
                > compare next element with first
                > swap them if not sorted
                > pick 3th element
                > compare 3th with 1st and 2th
                > swap if not sorted
                > pick 4th element 
                > compare 4th with all elements in the sorted sub-list
                > shift all the elements in the sorted sub-list that is greater than the 4th
                > Insert the 4th
                > ...
                > repeat until list is sorted

            C/C++ Code :
                void insertion(int arr[], int n){
                    int i, key, j;
                    for (i = 1; i < n; i++){
                        key = arr[i];
                        j = i - 1;
                        while (j >= 0 && arr[j] > key){
                            arr[j + 1] = arr[j];
                            j = j - 1;
                        }
                        arr[j + 1] = key;
                    }
                }
        """
        for i in range(1, n_):
            key = arr_[i]
            j = i-1
            while j >= 0 and key < arr_[j] :
                    arr_[j + 1] = arr_[j]
                    j -= 1
            arr_[j + 1] = key

    @staticmethod
    def shell(arr_, n_):
        """
            > Shell sort algorithm implementation
            > It is a variation of insertion sort
            > Avoids large shifts as in case of insertion sort, 
                if the smaller value is to the far right 
            > search the Knuth's Formula for better understanding :
                    h = h * 3 + 1, h : interval with initial value 1

            Complexity : O(n)

            Pseudo Code:
                > Initialize the value of h as 1
                > Divide the list into smaller sub-list of equal interval h
                > Sort these sub-lists using insertion sort
                > Repeat until complete list is sorted

            C/C++ Code :
                int shell(int arr[], int n){
                    for (int gap = n/2; gap > 0; gap /= 2){
                        for (int i = gap; i < n; i += 1){
                            int temp = arr[i];
                            int j;           
                            for (j = i; j >= gap && arr[j - gap] > temp; j -= gap)
                                arr[j] = arr[j - gap];
                            arr[j] = temp;
                        }
                    }
                    return 0;
                }
        """
        gap = n_//2 # initialize the gap
        while gap > 0:
            i = 0
            j = gap
            # check the array in from left to right
            # till the last possible index of j
            while j < len(arr_):
                if arr_[i] >arr_[j]:
                    arr_[i],arr_[j] = arr_[j],arr_[i]
                i += 1
                j += 1
                # now, we look back from ith index to the left
                # we swap the values which are not in the right order.
                k = i
                while k - gap > -1:
                    if arr_[k - gap] > arr_[k]:
                        arr_[k-gap],arr_[k] = arr_[k],arr_[k-gap]
                    k -= 1
            gap //= 2