FILE = "day_3_input.txt"

# Reads file
lines = []
with open (FILE, 'r') as file:
    for line in file:
        lines.append(line.strip())

#----------
# Part 1
#----------
sum = 0
for line in lines:
    max = 0
    for i in range(len(line)):
        tens = int(line[i]) * 10
        for j in range(i+1, len(line)):  # O(n^3) ahh code
            units = int(line[j])
            if tens + units > max:
                max = tens + units
    sum += max
print(sum)

# tries to optimize it but is off by 1
sum = 0
for line in lines:
    max_units = int(line[-1])  
    max = 0
    for i in range(len(line)-2, -1, -1):
        tens = int(line[i]) * 10
        if tens + max_units > max:
            max = tens + max_units
        if int(line[i+1]) > max_units:
            max_units = int(line[i+1])
    sum += max
print(sum)


#----------
# Part 2
#----------
digits = 12
sum = 0
for line in lines:  # greedy method??
    n = len(line)
    result = []
    start = 0
    for i in range(digits):
        max_digit = -1
        max_pos = -1
        for j in range(start, n - (digits - i) + 1):  # ensures there are enough digits left to fill remaining slots
            if int(line[j]) > max_digit:
                max_digit = int(line[j])
                max_pos = j
        result.append(str(max_digit))
        start = max_pos + 1
    num = int(''.join(result))
    sum += num
print(sum)