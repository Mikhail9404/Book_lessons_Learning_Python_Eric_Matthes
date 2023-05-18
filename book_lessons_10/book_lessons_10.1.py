filename = 'learning_python.txt'
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

print('\n')
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())


print('\n')
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line

print(pi_string)
