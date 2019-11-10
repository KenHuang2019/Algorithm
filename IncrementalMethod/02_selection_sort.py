def selection_sort(collection):
    length = len(collection)
    for i in range(length - 1):
        least = i
        # 找尋小於當下數字的所有數字
        for k in range(i + 1, length):
            # 透過迭代 找出最小的數字 的 index
            if collection[k] < collection[least]:
                least = k
        if least != i:
            # 將最小的數字換到排序位置
            collection[least], collection[i] = (collection[i], collection[least])
    return collection

if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(selection_sort(unsorted))