import re

FILE = "day_2_input.txt"

with open (FILE, 'r') as file:
    line = file.readline()
    ranges = line.strip().split(",")

#----------
# Part 1
#----------
invalid_sum = 0
for r in ranges:
    bounds = r.split("-")
    low = int(bounds[0])
    high = int(bounds[1])
    for i in range(low, high+1):
        pattern = re.compile(r'^(\d+)\1$')  # lol time to use regex
        if pattern.match(str(i)):
            invalid_sum += i
print(invalid_sum)

#----------
# Part 2
#----------
invalid_sum = 0
for r in ranges:
    bounds = r.split("-")
    low = int(bounds[0])
    high = int(bounds[1])
    for i in range(low, high+1):
        pattern = re.compile(r'^(\d+)\1+$')  # regex to check if a pattern is repeated at least twice
        if pattern.match(str(i)):
            invalid_sum += i
print(invalid_sum)