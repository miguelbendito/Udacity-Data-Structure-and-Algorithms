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

#parse all the (080) callers first
Bangalore = ""
#parse all the different prefixes of receivers
prefix = ""
#This set will hold all the distint prefixes. We know that 080 could be a receiver as well so we pass that value as dummy data
set_of_Codes=set()
count_Bang = 0
recei_Bang = 0
print("The numbers called by people in Bangalore have codes")
for nums in calls:
    Bangalore = nums[0]
    if Bangalore[0:5] == "(080)":
        # increments the counter every time a Bangalore's substring equals (080)
        count_Bang += 1
        prefix = nums[1]
        if prefix[0:5] == "(080)":
            # incrementes every time the prefix's subtring equals (080)
            recei_Bang += 1
        # check if the number has area code
        if prefix[0:2] == "(0" :
            #find the index of the right parenthesis
            right_Paren = prefix.rfind(')')
            #add the prefix to the set if its different to the previously added prefixes
            set_of_Codes.add(prefix[1:right_Paren])
        #check if the number starts with 7, 8 or 9
        if  prefix[0:1] == "7" or prefix[0:1] == "8" or prefix[0:1] == "9":
            #find the index of the space between the digits
            space = prefix.rfind(' ')
            #add the prefix to the set if its different to the previously added prefixes
            set_of_Codes.add(prefix[0: space-1])



#print each item in the list, corresponds to a lexicographic order with no duplicates
for code in sorted(set_of_Codes):
    print(code)

# lets find the percertage of the calls to Bangalore lines
percentage = round((recei_Bang/count_Bang)*100,2)
print("{}% of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore".format(percentage))


#print(unique_list)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
