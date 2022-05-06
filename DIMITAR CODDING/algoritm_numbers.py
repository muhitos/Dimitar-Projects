# Сортиране на номера

nums = [5,7,6,9,8,2,4,3,1]

print("Mix", nums)

for i in range(len(nums)):
    lowest = i # първи елемент за

    for j in range(i+1, len(nums)):
        if nums[j] < nums[lowest]:
            lowest = j # Нашия елемент в прав текст

    nums[i], nums[lowest] = nums[lowest], nums[i]

print("Normal", nums)
