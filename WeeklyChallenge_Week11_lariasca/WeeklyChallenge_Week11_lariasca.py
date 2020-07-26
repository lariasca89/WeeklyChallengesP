
# CX Programming Club
# Weekly Challenge 11
# lariasca

import re


def search_regex(pattern, lines, group):
    result = []
    for string in lines:
        match = re.search(pattern, string)
        if match:
            result.append(match.group(group))
    return result


def open_file(file):
    data = open(file, 'r')
    lines = []
    for line in data:
        if len(line) > 1:
            lines.append(line.strip())
    data.close()
    return lines


print("\nLog format should be MM/DD/YYYY XX:XX:XX [SEVERITY] MSSG\n")

# Open log file to parse information into lines.

lines = open_file("Weekly_Challenge_11_log_sample.log")

print("Analyzing Log File provided...\n")

# Collecting timestamp of first warning message.

timestamps = search_regex(r"(?P<timestamp>(\d{1,2}/){2}\d+\s(\d{1,2}:){2}\d+)\s\WWARNING\W(\s.*)", lines, "timestamp")

print(f'When did the first Warning occurred?\n -Occurred at {timestamps[0]}.\n')

# Collecting logs that doesn´t match the standard format.

logs = search_regex(r"(?P<logs>((\d{1,2}/){2}\d+\s(\d{1,2}:){2}\d+)\s[^[\w]+.*)", lines, "logs")

print(f'Printing logs which doesn´t match the standard format:\n -{" ".join(logs)}\n')

# List different severities and its appearance count.

severities = search_regex(r"((\d{1,2}/){2}\d+\s(\d{1,2}:){2}\d+)\s\[(?P<severities>\w+)\]\s(.*)", lines, "severities")

w, e, i, d = 0, 0, 0, 0

for sev in severities:
    if sev == "WARNING":
        w += 1
    elif sev == "ERROR":
        e += 1
    elif sev == "INFO":
        i += 1
    elif sev == "DEBUG":
        d += 1

print(f'''List different severities and its appearance count:
        [WARNING] ==> {w}
        [ERROR]   ==> {e}
        [INFO]    ==> {i}
        [DEBUG]   ==> {d}
        ''')
