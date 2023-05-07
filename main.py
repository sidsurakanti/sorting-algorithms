class Sort:
  def quicksort(self, arr: list) -> list:
    """
    Sorts :param arr: using the quicksort algorithm
    Time complexity: O(n*log(n))
    """
    # return array if already sorted
    if len(arr) <= 1:  
      return arr
      
    pivot = arr[-1]  

    # partition elements into two sub-arrays 
    left = [num for num in arr if num < pivot]   
    right = [num for num in arr if num > pivot]  
    middle = [num for num in arr if num == pivot]
    
    # recursively sort left and right 
    return self.quicksort(left) + middle + self.quicksort(right)

  def bubblesort(self, arr):
    """
    Sorts :param arr: by comparing adjacent values and putting them in the correct order
    Time complexity: O(n^2)

    TODO: increase efficiency by stopping iterations after arr is sorted
    """
    # return the array if already sorted
    arr_length = len(arr)
    if arr_length <= 1:  
      return arr
    
    # iterate len(arr) times through the array
    for i in range(arr_length):  
      # loop over the unsorted part of the array 
      for idx in range(0, arr_length - i - 1):
        # swap numbers if curr number > next number
        if arr[idx] > arr[idx + 1]:
          arr[idx + 1], arr[idx] = arr[idx], arr[idx + 1]

    return arr
