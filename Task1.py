"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# create a set that will hold all the distint numbers from both lists
unique_Num = set()


# loop through the intire text list
for t in texts:
    # add all the texters and recievers to the set
    unique_Num.add(t[0])
    unique_Num.add(t[1])
for c in calls:
    # add all the texters and receivers to the set
    unique_Num.add(c[1])
    unique_Num.add(c[0])

# print the lenght of the set, hence the total amount of different numbers from both lists
print("There are {} different telephone numbers in the record" .format(len(unique_Num)))


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
