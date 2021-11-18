import json


def gen_passport_dict(instring):
    output_dict = {}
    for line in instring.split("\n"):
        if line != "":
            for field in line.split(" "):
                output_dict[field.split(":")[0]] = field.strip().split(":")[1]
    return output_dict


def validate(passport):
    missing = []
    looking_for = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for field in looking_for:
        missing.append(field not in passport)
    return not any(missing)


def main():
    with open("input.txt", "r", encoding="utf8") as infile:
        intext = infile.read()

    passport_dict_list = []

    for passport in intext.split("\n\n"):
        passport_dict_list.append(
            gen_passport_dict(passport)
        )

    valid_passport = 0

    for passport in passport_dict_list:
        if validate(passport):
            valid_passport += 1

    print(f"There are {valid_passport} valid passports.")


if __name__ == "__main__":
    main()
