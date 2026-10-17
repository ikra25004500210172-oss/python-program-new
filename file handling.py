file = open("sample.txt", "w")
file.write("Hello! Welcome to Python File Handling.")
file.close()

print("Data written successfully.")


file = open("sample.txt", "r")
data = file.read()
print(data)
file.close()



file = open("sample.txt", "a")
file.write("\nThis is appended text.")
file.close()

print("Data appended successfully.")





with open("sample.txt", "r") as file:
    lines = file.readlines()

print("Total lines:", len(lines))


with open("sample.txt", "r") as file:
    data = file.read()

words = data.split()

print("Total words:", len(words))