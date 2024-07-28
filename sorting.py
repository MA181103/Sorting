#bubble sort-> if 4 elements in list, 3 passes r required
# Time complexity--> theta(n^2)
# stable algorithm
# def bubblesort(l):
#    n=len(l)
#    for i in range(n-1):
#       for j in range(n-i-1):
#          if l[j]>l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
# l=[10,8,20,5]
# bubblesort(l)
# print(l)

# optimizing in case of array becomes sorted after a pass
# linear time 
# def bubblesort(l):
#    n=len(l)
#    for i in range(n-1):
#       swapped=False
#       for j in range(n-i-1):
#          if l[j]>l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
#             swapped=True
#    if swapped==False:
#       return
# l=[21, 8, 10, 20]
# bubblesort(l)
# print(l)

# selection sort-->not stable, inplace algo-->doesnt require extra memory for sorting
# find minmum element and put it on first position
# list size is 6 , we will run a loop from 0 to 4 i.e n-2
# not a stable algorithm
# def selectsort(l):
#    n=len(l)
#    for i in range(n-1):
#       min_idx=i
#       for j in range(i+1,n):
#          if l[j]<l[min_idx]:
#             min_idx=j
#       l[min_idx],l[i]=l[i],l[min_idx]
# l=[10,5,8,20,2,18]
# selectsort(l)
# print(l)

# insertion sort TC worstcase--> o(n^2), inplace and stable, best case-->o(n),
# used for small arrays
# def insertionsort(l):
#    for i in range(1,len(l)):
#       x=l[i]
#       j=i-1
#       while j>=0 and x<l[j]:
#          l[j+1]=l[j]
#          j=j-1
#       l[j+1]=x
# l=[10,5,8,20,2,18]
# insertionsort(l)
# print(l)


# Quicksort
def quicksort(arr,low,high):
   if low<high:
      j=partition(arr,low,high)
      quicksort(arr,low,j-1)
      quicksort(arr,j+1,high)

def partition(arr,low,high):
   pivot=arr[low]
   i=low+1
   j=high
   while(i<j):
      while(arr[i]<=pivot):
         i+=1
      while(arr[j]>pivot):
         j-=1
      if(i<j):
         arr[i],arr[j]=arr[j],arr[i]
      
   arr[low],arr[j]=arr[j],arr[low]
   return j

arr=[10,5,8,20,2,18]
quicksort(arr,0,len(arr)-1)
print(arr)
    