file = open("./input.txt")

lines = file.readlines()
elfCalories = [0]
index = 0;

for line in lines:
    if not line.strip():
        index += 1
        elfCalories.append(0)
        continue
    
    elfCalories[index] += int(line.strip())

# Answer for first challenge
print(max(elfCalories))

elfCalories.sort(reverse=True)

# Answer for second challenge
print(elfCalories[0] + elfCalories[1] + elfCalories[2])
