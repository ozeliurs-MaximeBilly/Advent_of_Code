with open("input.txt","r",encoding="utf8") as infile:
    inlist = infile.read()

inlist = inlist.split("\n")[:-1]

# Part One
for i, val1 in enumerate(inlist):
    for val2 in inlist[i:]:
        if int(val1)+int(val2) == 2020:
            print(f"{val1} and {val2} add up to 2020 here is {val1}x{val2}={int(val1)*int(val2)}")

# Part Two
for i, val1 in enumerate(inlist):
    for j, val2 in enumerate(inlist[i:]):
        for val3 in inlist[j:]:
            if int(val1)+int(val2)+int(val3) == 2020:
                print(f"{val1}, {val2} and {val3} add up to 2020 here is {val1}x{val2}x{val3}={int(val1)*int(val2)*int(val3)}")