"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

d = dict()
largest_Call = 0;
phone_Number =""

# Loop through the list of calls
for n in calls:
    # if the caller or the receiver (will be the keys) are in the dict then add the time spent (values)
    if n[0] in d:
        d[n[0]] += int(n[3])
    if n[1] in d:
        d[n[1]] += int(n[3])
    # if they caller and reciever are not in the list the current value with the old value
    if n[0] not in d:
        d[n[0]] = int(n[3])
    if n[1] not in d:
        d[n[1]] = int(n[3])


"""The reason why we must assume that the value is in the dictionary is beacause there
are only 500 different numbers and 5000+ lines of code, if we assume they are in the dictionary
then they most certainty will be by the 1000th iteration of the loop. In conclusion we will only
do one comparison instead of 2 and therefore a more efficient algorithm."""

# loop through the dict to find the number with the largest call
for x, y in d.items():
    # if the current value is greater than the value that largest_Call is holding
    # then the current value will be the value of the largest_Call
    # and the current key will be the value of the phone_Number
    if y > largest_Call:
        largest_Call = y
        phone_Number = x
# print the phone_Number and the largest call
print ("{} spent the longest time, {} seconds, on the phone during September 2016" .format(phone_Number, largest_Call))

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
