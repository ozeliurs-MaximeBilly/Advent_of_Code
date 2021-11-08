import re

with open("input.txt","r",encoding="utf8") as file:
    data = file.read()

database = []

for line in data.split("\n")[:-1]:
    bag = line.split(" contain ")[0]
    contains = [x.split(" ", 1) for x in line.split(" bags contain ")[1].strip(".").split(", ")]
    database[bag] = contains

bags = [[1, "shiny gold bags"]]

while True:
    new_bags = []
    for bag in bags:
        for i in range(int(bag[0])):
            new_bags.append()