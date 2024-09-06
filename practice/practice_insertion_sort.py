#practice insertion sort 

# def insertion_sort(element_list):
#     length = len(element_list)

#     for k in range(1, length):
#         element = element_list[k]
#         l = k - 1
#         while l>=0 and element_list[l] > element:
#             element_list[l+1] = element_list[l]
#             l = l - 1

#         element_list[l+1] =  element

# element_list = [23,45,67,88,43,12]
# insertion_sort(element_list)
# print("insertion sort:", element_list)


# def insertion(data_list):
#     n = len(data_list)
#     for i in range(1, n):
#         item = data_list[i]
#         j = i-1
#         while j>=0 and data_list[j] > item:
#             data_list[j+1] = data_list[j]
#             j = j-1

#         data_list[j+1] = item

# data_list = [82,34,56,78,34,21]
# insertion(data_list)
# print("insetion sort:", data_list)

# def insertion_sort(element_list):
#     length = len(element_list)
#     for i in range(1, length):
#         element = element_list[i]
#         j = i-1
#         while j>=0 and element_list[j] > element:
#             element_list[j+1] = element_list[j]
#             j = j-1

#         element_list[j+1] = element

# element_list = [34,12,56,78,89,64]
# insertion_sort(element_list)
# print("", element_list)


