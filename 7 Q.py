# Empty dictionary

records = {}

# Taking input from user

n = int(input("How many students? "))

for i in range(n):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    records[name] = marks

# Display records
print("Student Records:")
for name in records:
    print(name, ":", records[name])