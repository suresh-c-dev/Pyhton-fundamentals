    # Program 1: players - slice, append, insert, extend, remove, pop, del


players = ["Ravi", "Amit", "Kiran", "Sonu", "Raj", "Dev"]
print(players[0:3])
print(players[-1])
players.append("Neha")
players.insert(2,"Arun")
players.extend(["Mani","Joy"])
players.remove("Amit")
player=players.pop()
print("Out:",player)
del players[0]
print(players,"\nlength of the list: ",len(players))


    # Program 2: marks - count, index, copy, sort, comprehension, range loop, nested list

marks = [45, 82, 67, 90, 33, 82, 58]
print(marks.count(82))
print(marks.index(90))
original=marks.copy()
marks.sort(reverse=True)
print(marks)
passed=[x for x in marks if x >= 50]
print(passed)
bonus=[a+5 for a in passed ]
print(bonus)
for i in range(len(bonus)):
    print(i,"->",bonus[i])
report=[original,passed,bonus]
print(report[2][0])
print(len(report))
print(original)

    # Program 3: student result - lists, index, remove, del, copy, comprehension, sort, nested list

students = ["Ravi", "Amit", "Kiran", "Sonu", "Raj"]
marks = [72, 38, 91, 45, 60]
students.append("Neha")
marks.append(85)
marks[1]=48
i = students.index("Raj")
students.remove("Raj")
del marks[i]
originalmarks=marks.copy()
top=[x for x in marks if x>=60]

for i in range(len(students)):
    print(i,"->",students[i],":",marks[i])
marks.sort(reverse=True)
print(marks)
result=[students,originalmarks]
print(result[1][0],"\n",len(result))
print(top)
print(marks[0])
