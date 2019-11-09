a = [3, 6, 9, -8, 1]

for i in range(len(a)):
    min_index = i

    # 找尋小於當下數字的所有數字
    for j in range(i, len(a)):
        # 透過迭代 找出最小的數字 的 index
        if a[j] < a[min_index]:
            min_index = j

    # 將最小的數字換到排序位置
    a[i], a[min_index] = a[min_index], a[i]
    print(a) # 確認每一次交換位置的結果

print(f'sorted a:{a}')