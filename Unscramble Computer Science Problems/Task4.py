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

tele_outCall =set()
tele_inCall = set()
tele_outText = set()
tele_inText = set()
#create an empty set of telemarketers
print("These numbers could be telemarketers")
#traverse the list of calls
for nums in calls:
    #tele_outCall is a variable that holds the current val of nums[0]; first column of the list
    tele_outCall.add(nums[0])
    #tele_inCall is a variable that holds the current val of nums[1]; second column of the list
    tele_inCall.add(nums[1])
for text in texts:
    #tele_outText is a variable that holds the current val of text[0]; first column of the list
    tele_inText.add(text[0])
    #tele_inText is a variable that holds the current val of nums[1]; second column of the list
    tele_inText.add(text[1])

#new_set is the substraction of all the sets using operators in lexicographic order
new_set = sorted(tele_outCall - tele_inCall - tele_outText - tele_inText)
for n in new_set:
    print (n)


"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
