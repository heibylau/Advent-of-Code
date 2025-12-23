FILE = "day_1_input.txt"
TICKS = 100

# Reads file
lines = []
with open (FILE, 'r') as file:
    for line in file:
        lines.append(line.strip())

#----------
# Part 1
#----------
start = 50
end = 50
password = 0
for line in lines:
    if line[0] == 'L':
        mul = -1
    elif line[0] == 'R':
        mul = 1
    end = (start + (mul * int(line[1:]))) % TICKS
    if end == 0:
        password += 1
    start = end

print(password)


#----------
# Part 2
#----------
num = 50
password = 0
for line in lines:
    if line[0] == 'L':
        mul = -1
    elif line[0] == 'R':
        mul = 1
    ticks = int(line[1:])

    if mul == -1 and num == 0:
        password -= 1  # edge case to prevent overcounting

    num += mul * ticks

    # count how many times the dial passes 0
    while (num < 0 or num > 99):
        if num < 0:
            num += TICKS
            password += 1
        if num > 99:
            num -= TICKS
            password += 1

    if mul == -1 and num == 0:
        password += 1  # edge case for when landing exactly on 0
print(password)