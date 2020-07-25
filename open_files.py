data = open("Weekly_Challenge_9.csv", 'r')
lines = []
for line in data:
    if len(line) > 1:
        lines.append(line.strip().split(','))
data.close()
print(lines)


# Create new output file with .csv extension
with open('Cisco_Phone_Output.csv', 'w') as file_handler:
    for line in lines:
        parameters_as_int = [int(item) for item in line[1:]]
        result = functions[line[0]](*parameters_as_int)
        file_handler.write(f'{line[0]}{*parameters_as_int,} => {result}\n')
print("Done!")

