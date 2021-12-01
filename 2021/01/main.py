with open("input.txt", "r", encoding="utf8") as in_file:
    in_content = in_file.read()

in_content = in_content.split("\n")[:-1]

increased = 0

# Part One
for i in range(len(in_content)):
    if i != 0:
        if int(in_content[i - 1]) < int(in_content[i]):
            print(f"{in_content[i - 1]} -> {in_content[i]} : Increase !!")
            increased += 1

print(increased)

# Part Two
window = []

for i in range(len(in_content)):
    if i != 0 and i != len(in_content)-1:
        window.append(int(in_content[i-1]) + int(in_content[i]) + int(in_content[i+1]))

increased = 0
for i in range(len(window)):
    if i != 0:
        if window[i] > window[i-1]:
            print(window[i])
            increased += 1

print(increased)
