# Бинарно търсене

nums = [5, 7, 6, 9, 8, 4, 2, 3, 1]
nums.sort()
print(nums)

search_for = 9

lowest = 0
highest = len(nums) - 1
index = None

while(lowest <= highest) and (index is None):

    mid = (lowest+highest) // 2

    if nums[mid] == search_for:

        index = mid
    else:
        if search_for < nums[mid]:

            highest = mid - 1
        else:

            lowest = mid + 1

print("Исканият елемент", search_for, "се намира под индекс", index)
