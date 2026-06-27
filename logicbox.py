# Pattern Generator and Number Analyzer

def right_triangle(rows):
    print("\nRight-Angled Triangle Pattern")
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end=" ")
        print()


def pyramid(rows):
    print("\nPyramid Pattern")
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end=" ")
        for k in range(2 * i - 1):
            print("*", end=" ")
        print()


def left_triangle(rows):
    print("\nLeft-Angled Triangle Pattern")
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end=" ")
        for k in range(i):
            print("*", end=" ")
        print()


def number_analyzer():
    print("\nNumber Analyzer")

    start = int(input("Enter start number: "))
    end = int(input("Enter end number: "))

    if end < start:
        print("Error: End number must be greater than or equal to start number.")
        return

    total = 0

    print("\nOdd and Even Numbers:")
    for num in range(start, end + 1):

        # Example of continue statement
        if num == 0:
            pass

        if num % 2 == 0:
            print(num, "- Even")
        else:
            print(num, "- Odd")

        total += num

    print("\nSum of all numbers =", total)


def pattern_menu():
    print("\nSelect Pattern")
    print("1. Right-Angled Triangle")
    print("2. Pyramid")
    print("3. Left-Angled Triangle")

    choice = input("Enter your choice: ")

    rows = int(input("Enter number of rows: "))

    if rows <= 0:
        print("Invalid row count! Rows must be positive.")
        return

    if choice == "1":
        right_triangle(rows)
    elif choice == "2":
        pyramid(rows)
    elif choice == "3":
        left_triangle(rows)
    else:
        print("Invalid pattern choice.")


def main():
    print("===================================")
    print(" Pattern Generator and Number Analyzer ")
    print("===================================")

    while True:
        print("\nMenu")
        print("1. Generate Pattern")
        print("2. Analyze Numbers")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            pattern_menu()

        elif choice == "2":
            number_analyzer()

        elif choice == "3":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice. Please try again.")


main()