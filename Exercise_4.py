# Time Complexity : O(nlogn)
# Space Complexity : O(n)

# Python program for implementation of MergeSort 
def mergeSort(arr):
  divide(arr, 0, len(arr)-1)

def divide(arr, start, end):
  if (end - start + 1 <= 1):
    return
  
  mid = (start + end)//2

  divide(arr, start, mid)
  divide(arr, mid+1, end)
  merge(arr, start, mid, end)


def merge(arr, start, mid, end):
  left = arr[start:mid+1]
  right = arr[mid+1:end+1]

  lp = rp = 0
  k = start

  while lp < len(left) and rp < len(right):
    if left[lp] < right[rp]:
      arr[k] = left[lp]
      lp += 1
    else:
      arr[k] = right[rp]
      rp += 1
    k += 1
  
  while lp < len(left):
    arr[k] = left[lp]
    lp += 1
    k += 1

  while rp < len(right):
    arr[k] = right[rp]
    rp += 1
    k += 1

  
# Code to print the list 
def printList(arr): 
  print(arr)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
