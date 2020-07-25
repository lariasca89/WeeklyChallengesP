# CX Programming Club
# Week 09
# lariasca

import csv

# Open the file and parse the information
data = open("Weekly_Challenge_9.csv", 'r')
lines = []
for line in data:
    if len(line) > 1:
        lines.append(line.strip().split(','))
data.close()

new_header = ['extension', 'name', '#_line_buttons', '#_blfs_buttons', '#_speeddial_buttons', 'cisco_model']

new_file = []
new_line = []
new_file.append(new_header)

for line in lines[1:]:
    if line[4] != '':
        plk_count = int(line[4])
        line_count = 0
        blf_count = 0
        speed_count = 0
    else:
        if line[2] == 'Line (ring)':
            line_count += 1
            plk_count -= 1
        elif line[2] == 'BLF':
            blf_count += 1
            plk_count -= 1
        elif line[2] == 'Speed-dial':
            speed_count += 1
            plk_count -= 1
        else:
            plk_count -= 1

        if plk_count == 0:
            total_buttons = line_count + blf_count + speed_count
            new_line = [line[0], line[1], line_count, blf_count, speed_count]

            if total_buttons <= 5:
                new_line.insert(5, '8841')
            else:
                new_line.insert(5, '8851')

            new_file.append(new_line)
        else:
            print("Collecting data")

# Create new output file with .csv extension
with open('Cisco_Phone_Output.csv', 'w', newline='') as file_handler:
    write = csv.writer(file_handler)
    write.writerows(new_file)
print("Done!")
