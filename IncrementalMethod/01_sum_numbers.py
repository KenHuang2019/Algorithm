def sum_numbers(collection):
    sum_a = 0
    for n in collection:
        sum_a += n
    return sum_a


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(sum_numbers(unsorted))