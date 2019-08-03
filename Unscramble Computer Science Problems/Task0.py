"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
# CSV stands for "comma separated values" followed by a new line for each entry
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

#Once we converted each file into a list of records we must know manipulate the lists to obtain the first row located at index 0
# We can find the last row checking the last row located in index [-1] if we don't know the length of the list
# Pass the rows into a new list of texts and calls holding just the first and last row, respectively
first_Record_Texts = texts[0]
last_Record_Calls = calls[-1]

message = "First record of texts, {} texts {} at time {}".format(*first_Record_Texts)
print(message)
#Overwrite the message a print a new one
message = "Last record of calls, {} calls {} at time {}, lasting {} seconds" .format(*last_Record_Calls)
print(message)
"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
