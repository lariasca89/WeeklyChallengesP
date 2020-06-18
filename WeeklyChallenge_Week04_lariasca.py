# Weekly Challenge 4
# CX Programming Club
# lariasca
print(">>>Hello! Please tell what you need to complete before your trip:")
tasks = []
for i in range(5):
    task = input(f"Task {i+1}: ")
    tasks.insert(i, task)
print(" ")
remember = int(input(">>>Which task you need help remembering? "))
print(f"You need to: {tasks[remember-1]}")
print(" ")
print(">>>You forgot an intermediate task.")
print(" ")
new_task = input("What was it? ")
print(" ")
new_index = int(input("What position should you do this task? "))
print(" ")
tasks.insert(new_index-1, new_task)
tasks.append("Use the restroom")
print(">>>And I will remind you to use the WC :)")
print(" ")
print(" ")
print(">>>Here is all you have to do before the trip:")
print(tasks)
print(" ")
tasks.pop(0)
tasks.pop(0)
print(">>>By the way, you already did the 1st and 2nd task. Let's forget about those:")
print(tasks)
print(" ")
print(" ")
print(">>>Tell me your name and passport number and I will keep them safe!")
name = input("Name: ")
passport = input("Pass: ")
id = (name, passport)
print("This will be safely stored: ", id)
print(" ")
print(" ")
print(">>>Here comes your friend...")
your_c = input("Countries you've been to: ")
fri_c = input("Countries your friend has been to: ")

your_c = set(your_c.split(" "))
fri_c = set(fri_c.split(" "))

friend_diff = fri_c.difference(your_c)
sep = " and "
answer1 = sep.join(friend_diff)
print(" ")
print(f"Your friend has gone to {answer1} but you haven't")
print(" ")
your_diff = your_c.difference(fri_c)

answer2 = sep.join(your_diff)
print(f"You have been to {answer2} but your friend hasn't")

both = fri_c.intersection(your_c)
sep1 = ", "
answer3 = sep1.join(both)
print(" ")
print(f"Both have been to {answer3}")

your_ticket = {"Seat": "12A", "Flight": "123"}
friend_ticket = {"Seat": "27D", "Flight": "1009"}
passenger = {"G123456": your_ticket, "G989494": friend_ticket}
print(">>>This is the system's information: ")
print(passenger)
