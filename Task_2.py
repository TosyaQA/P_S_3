#Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
#В результирующем списке не должно быть дубликатов. [1, 2, 3, 1, 2, 4, 5] -> [1, 2]

list = [2, 1, 2, 3, 1, 2, 4, 5, 5, 5]
uniq_dir = {}
result = []

for num in list:
    if (num in uniq_dir):
        uniq_dir[num] = uniq_dir[num] + 1
    else:
        uniq_dir[num] = 1

for key in uniq_dir.keys():
    if (uniq_dir[key] > 1):
        result.append(key)

print(result) # [2, 1, 5]