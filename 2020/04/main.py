def gen_passport_dict(instring):
    output_dict = {}
    for line in instring.split("\n"):
        for field in line.split(" "):
            output_dict[field.split(":")[0]] = field.strip().split(":")[1]
    return output_dict


def validate(passport):
    missing = []
    looking_for = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for field in looking_for:
        missing.append(field not in passport)
    return not any(missing)


def valid(passport):
    missing = []
    looking_for = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for field in looking_for:
        missing.append(field not in passport)
    if not any(missing):
        try:
            a = int(passport["byr"])
        except ValueError:
            return False

        try:
            a = int(passport["iyr"])
        except ValueError:
            return False

        try:
            a = int(passport["pid"])
        except ValueError:
            return False

        try:
            a = int(passport["eyr"])
        except ValueError:
            return False

        if not (len(passport["ecl"]) == 3):
            return False

        if not ( "#" in passport["hcl"] and len(passport["hcl"]) == 7 ):
            return False

        if not ("cm" in passport["hgt"]):
            return False
    return True


def main():
    with open("input.txt", "r", encoding="utf8") as infile:
        intext = infile.read()

    passport_dict_list = []

    for passport in intext.split("\n\n")[:-1]:
        passport_dict_list.append(
            gen_passport_dict(passport)
        )

    valid_passport = 0

    for passport in passport_dict_list:
        if validate(passport) and valid(passport):
            print(passport["byr"], passport["iyr"], passport["eyr"], passport["hgt"], passport["hcl"], passport["ecl"], passport["pid"], passport)
            valid_passport += 1

    print(f"There are {valid_passport} valid passports.")


if __name__ == "__main__":
    main()
