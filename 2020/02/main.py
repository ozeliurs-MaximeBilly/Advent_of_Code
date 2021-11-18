from operator import xor


def process_string(instr):
    stra, strd = instr.split(": ")
    stra, strc = stra.split(" ")
    stra, strb = stra.split("-")

    return int(stra), int(strb), strc, strd


def main():
    with open("input.txt", "r", encoding="utf8") as infile:
        inlist = infile.read()

    inlist = inlist.split("\n")[:-1]

    # Part One
    valid_password = 0

    for line in inlist:
        lowlim, highlim, spec, pwd = process_string(line)

        if highlim >= len([car for car in pwd if car == spec]) >= lowlim:
            valid_password += 1

    print(f"There are {valid_password} valid passwords with respect to the first rule.")

    # Part Two
    valid_password = 0

    for line in inlist:
        car1, car2, spec, pwd = process_string(line)
        if len(pwd) >= car1-1 and len(pwd) >= car2-1:
            if xor(bool(pwd[car1-1] == spec), bool(pwd[car2-1] == spec)):
                valid_password += 1

    print(f"There are {valid_password} valid passwords with respect to the second rule.")


if __name__ == "__main__":
    main()
