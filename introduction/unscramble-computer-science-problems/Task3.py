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

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
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

def is_080_in_record_src(record):
    return True if '(080)' in record[0] else False

def is_dst_mobile(record):
    return True if '(' in record[1] else False

def is_dst_fixed_line(record):
    return True if ' ' in record[1] else False

def is_080_in_record_dst(record):
    return True if '(080)' in record[1] else False



def task_a():
    uniq_code_and_prefixes = []
    count = 0

    for item in calls:
        if is_080_in_record_src(item):
            if is_dst_mobile(item):
                code_area = item[1][1:4]
                if code_area not in uniq_code_and_prefixes:
                    uniq_code_and_prefixes.append(code_area)
            elif is_dst_fixed_line(item):
                mobile_prefix = item[1][:4]
                if mobile_prefix not in uniq_code_and_prefixes:
                    uniq_code_and_prefixes.append(mobile_prefix)
            if is_080_in_record_dst(item):
                count += 1
    print(f'The numbers called by people in Bangalore have codes:')
    print(*sorted(uniq_code_and_prefixes),sep='\n')
    return count
            


if __name__ == '__main__':
    bangalore_to_bangalore = task_a()
    print(
        f'{round((bangalore_to_bangalore / len(calls)) * 100, 2)} '
        'percent of calls from fixed lines in Bangalore are calls '
        'to other fixed lines in Bangalore.'
    )
