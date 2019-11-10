def draw_right_triangle(l):
    for i in range(l, 0, -1):
        print('@'*i)

if __name__ == "__main__":
    user_input = input("Enter a number as side length:\n").strip()
    draw_right_triangle(int(user_input))