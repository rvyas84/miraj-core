import csv

with open('test.txt', 'r') as file: # Make sure 'test.txt' exists in the same directory
    content = file.read()
    print(content)

with open('output.txt', 'w') as file: # This will create a new file or overwrite an existing file
    file.write('This is a test output.\n')
    file.write('Writing to files in Python is easy!\n')

with open('output.txt', 'a', newline='') as file:
    file.write('Appending a new line to the existing file.\n')

with open('data.csv', mode = 'w', newline='') as csvfile: # This will create a new CSV file
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Name', 'Age', 'City'])
    csvwriter.writerow(['Alice', 30, 'New York'])
    csvwriter.writerow(['Bob', 25, 'Los Angeles'])

with open('data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print(row)