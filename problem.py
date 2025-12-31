
# number_of_plants, dryness_plants = map(int,input().split())
# dryness_rates = list(map(int, input().split()))

# drynes_each_plants = [0] *number_of_plants

# survived_hours = 0

# water_stock = 0

# while True:
#     max_dryness =0
#     max_index = 0

#     for i in range(number_of_plants):
#         drynes_each_plants[i] += dryness_rates[i]
    
#         if drynes_each_plants[i] > max_dryness:
#             max_dryness = drynes_each_plants[i]
            
#             max_index =i
#     if max_dryness >= dryness_plants:
#         break
#     water_stock +=1

#     if water_stock >0:
#         drynes_each_plants[max_index]=0
#         water_stock -=1

#     survived_hours +=1
# print(survived_hours)



# number_test = int(input())
# for x in range(number_test):
#     each_test = int(input())
#     if each_test ==0:
#         print(1)
#         continue
#     count_ones = bin(each_test).count('1')
#     print(2**(count_ones-1))

# import bisect
# test_case = int(input())
# for x  in range((test_case)):
#     passensers = int(input())
#     bag_weight = list(map(int,input().split()))
#     sorted_list =[]
#     count=0

#     for i in range(passensers-1,-1,-1):
#         count += bisect.bisect_right(sorted_list,bag_weight[i])

#         bisect.insort(sorted_list,bag_weight[i])
#     print(count)




# rice_bag_types, total_weight = map(int, input().split())
# list_rice_bag_weight = list(map(int,input().split()))

# index_start = 0

# sum = 0

# for x in range(rice_bag_types):
#     sum += list_rice_bag_weight[x]
    
#     while sum > total_weight:
#         sum -= list_rice_bag_weight[index_start]
#         index_start +=1

#     if sum > 0 and total_weight % sum ==0:
#         print("YES")
#         exit()
# print("NO")

import sys 
input = sys.stdin.readline
mountain_nums, mountain_queries = map(int,input().split())
mountain_of_heights = list(map(int,input().split()))


limits_left = [0]* mountain_nums
for i in range(1, mountain_nums):
    limits_left[i] = limits_left[i-1] if mountain_of_heights[i] >= mountain_of_heights[i-1] else i

limits_right = [0]*mountain_nums
limits_right[-1] = mountain_nums-1
for i in range(mountain_nums-2, -1, -1):
    limits_right[i] = limits_right[i+1] if mountain_of_heights[i] >= mountain_of_heights[i+1] else i


size = 1
while size < mountain_nums: size <<= 1
segmentation = [(-1, 0, -1)] * (2 * size)

for i in range(mountain_nums):
    segmentation[size+i] = (mountain_of_heights[i], 1, i)

for i in range(size-1, 0, -1):
    left_child, right_child = segmentation[2*i], segmentation[2*i+1]
    if left_child[0] > right_child[0]:
        segmentation[i] = left_child
    elif left_child[0] < right_child[0]:
        segmentation[i] = right_child
    else:
        segmentation[i] = (left_child[0], left_child[1]+right_child[1], left_child[2])


def get(left_index_list, right_index_list):
    left_index_list += size
    right_index_list += size
    max_height, count, idx = -1, 0, -1
    while left_index_list <= right_index_list:
        if left_index_list & 1:
            if segmentation[left_index_list][0] > max_height:
                max_height, count, idx = segmentation[left_index_list]
            elif segmentation[left_index_list][0] == max_height:
                count += segmentation[left_index_list][1]
            left_index_list += 1
        if not right_index_list & 1:
            if segmentation[right_index_list][0] > max_height:
                max_height, count, idx = segmentation[right_index_list]
            elif segmentation[right_index_list][0] == max_height:
                count += segmentation[right_index_list][1]
            right_index_list -= 1
        left_index_list >>= 1
        right_index_list >>= 1
    return max_height, count, idx


for x in range(mountain_queries):
    left_index_list, right_index_list = map(int,input().split())
    left_index_list -= 1
    right_index_list -= 1
    max_height, count, height_of_mount = get(left_index_list, right_index_list)
    if count != 1:
        print("NO")
        continue
    print("YES" if limits_left[height_of_mount] <= left_index_list and limits_right[height_of_mount] >= right_index_list else "NO")





