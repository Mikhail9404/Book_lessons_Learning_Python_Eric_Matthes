filename = 'learning_python.txt'
with open(filename) as file_object:
    lines = file_object.read()


print(lines)
lines = lines.replace('Python', 'C')
print(f"\n{lines}")