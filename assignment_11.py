import re

filename = "assignment_data_11.txt"
file = open(filename, "r")
lst = []
numberSum = 0

for line in file:
    digits = re.findall('[0-9]+', line)
    if len(digits) > 0:
        lst.extend(digits)
for i in lst:
    numberSum += int(i)
print(numberSum)


