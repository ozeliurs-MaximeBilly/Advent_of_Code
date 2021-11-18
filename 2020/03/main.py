def get_trees_encountered(matrix, x_vect, y_vect):
    x = 0
    y = 0
    trees_encountered = 0

    while y <= len(matrix)-1:
        if matrix[y][x % len(matrix[0])] == "#":
            trees_encountered += 1

        x += x_vect
        y += y_vect

    return trees_encountered


def main():

    with open("input.txt", "r", encoding="utf8") as infile:
        intext = infile.read()

    matrix = [[car for car in line] for line in intext.split("\n")[:-1]]

    # Part One

    print(f"You have encountered {get_trees_encountered(matrix, 3, 1)} trees.")

    # Part Two

    a = get_trees_encountered(matrix, 1, 1)
    b = get_trees_encountered(matrix, 3, 1)
    c = get_trees_encountered(matrix, 5, 1)
    d = get_trees_encountered(matrix, 7, 1)
    e = get_trees_encountered(matrix, 1, 2)

    print()
    print(f"You have encountered {a} trees.")
    print(f"You have encountered {b} trees.")
    print(f"You have encountered {c} trees.")
    print(f"You have encountered {d} trees.")
    print(f"You have encountered {e} trees.")
    print()
    print(f"Multiplied together : {a*b*c*d*e}")


if __name__ == "__main__":
    main()
