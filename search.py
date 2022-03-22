import math

class Search:
    @staticmethod
    def linear(arr_, n_, x_):
        """
            Complexity : O(n)

            Pseudo Code :
                > Start from the leftmost element of array 
                > Iterate to the next element one by one
                > If x matches with an element, return index
                > I x doesn't match with any of elements, return -1

            C/C++ code : 
                int linear(int arr[], int n, int x){
                    int i;
                    for (i = 0; i < n; i++)
                        if (arr[i] == x) return i;
                    return -1;
                }
        
        """
        for i in range(0,n_):
            if(arr_[i] == x_):
                return i
        return -1

    class Binary:
        """
            > Kind of Algorithmic Paradigm : Decrease and Conquer(Divide and Conquer)
            > Search algorithm for the sorted arrays

            Complexity : O(log(n)) 

            Pseudo Code : 
                > Sort the array (! ARRAY MUST BE SORTED FOR THE BINARY TREE)
                > If the value of the search key is less than the item in the middle of array,
                    continue from the left half side of the middle
                > otherwise, continue from right half side
                > repeat the process until the value is found
                > If x matches with an element, return index 
                > I x doesn't match with any of elements, return -1
        """
        @staticmethod
        def recursive(arr_, l_, r_, x_):
            """
                C/C++ Code :
                    int recursive(int arr[], int l, int r, int x){
                        if (r >= l) {
                            int mid = l + (r - l) / 2;
                            if (arr[mid] == x) return mid;
                            if (arr[mid] > x) return recursive(arr, l, mid - 1, x);
                            return recursiveh(arr, mid + 1, r, x);
                        }
                        return -1;
                    }
            """
            if r_ >= l_:
                mid = l_ + (r_ - l_) // 2
                if arr_[mid] == x_: # if x is present at the middle
                    return mid
                elif arr_[mid] > x_: # if x is smaller than mid
                    return Search.Binary.recursive(arr_, l_, mid-1, x_)
                else: # if x is greater than mid
                    return Search.Binary.recursive(arr_, mid + 1, r_, x_)
            else:
                return -1 # x is not present in the array
        
        @staticmethod
        def iterative(arr_, l_, r_, x_):
            """
                C/C++ Code :
                    int iterative(int arr[], int l, int r, int x){
                        while (l <= r) {
                            int m = l + (r - l) / 2;
                            if (arr[m] == x) return m;
                            if (arr[m] < x) l = m + 1;
                            else r = m - 1;
                        }
                        return -1;
                    }
            """
            while l_ <= r_:
                mid = l_ + (r_ - l_) // 2
                if arr_[mid] == x_: # if x is present at mid
                    return mid
                elif arr_[mid] < x_: # If x is greater then mid
                    l_ = mid + 1
                else: # If x is smaller then mid
                    r = mid - 1
            return -1 # x is not present in the array

    @staticmethod
    def jump(arr_ , x_ , n_):
        """
            > Search algorithm for the sorted arrays

            Complexity : O(n^(1/2)) 

            Pseudo Code : 
                > sort the array if not sorted
                > calculate the block size to jump (generally : block_size sqrt(n))
                > Jump from index 0 to index block_size
                > Jump from index block_size to index 2*block_size
                > Jump from index 2*block_size to index 3*block_size
                > Jump from index .. to index .. until the end reached
                > If element at last index  is greater than x,
                     we will jump back a step to come to previous index. 
                >  Apply a linear search from previous index to get the element x
                > I x doesn't match with any of elements, return -1

            C/C++ Code : 
                int jump(int arr[], int x, int n){
                        int step = sqrt(n);
                        int prev = 0;
                        while (arr[min(step, n)-1] < x){
                            prev = step;
                            step += sqrt(n);
                            if (prev >= n) return -1;
                        }
                        while (arr[prev] < x){
                            prev++;
                            if (prev == min(step, n)) return -1;
                        }
                        if (arr[prev] == x) return prev;
                        return -1;
                    }

        """
        step = math.sqrt(n_) # calculate block size to be jumped
        prev = 0
        while arr_[int(min(step, n_)-1)] < x_: # the block where x is
            prev = step
            step += math.sqrt(n_)
            if prev >= n_:
                return -1
        while arr_[int(prev)] < x_: # linear search for x in block beginning with prev.
            prev += 1
            if prev == min(step, n_): # If next block or end is reached
                return -1
        if arr_[int(prev)] == x_: # if x it not found
            return prev
        return -1 # x is not presented in given array.