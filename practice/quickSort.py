# quick sort implementation

def partiton(list, low, high):
    pivot = list[high]
    i = low-1
    for j in range(low, high):
        if list[j] <= pivot:
            i+=1
            list[i], list[j] = list[i], list[i]
            
    list[i+1], list[high] = list[high], list[i+1]
    return i+1

def quick_sort(list, low, high):
    if low >= high:
        return
    pivot_index = partiton(list,low,high)
    quick_sort(list, low, pivot_index-1) # left sub-list
    quick_sort(list, pivot_index+1, high) # right sub-list

if __name__ == "__main__" :
    Data_lsit = [34,45,67,64,23,76,11]
    print("Unsorted list:", Data_lsit)
    quick_sort(Data_lsit, 0, len(Data_lsit)-1)
    print("Sorted list:", Data_lsit)