# https://leetcode.com/problems/valid-phone-numbers/
# 2022年04月04日 21:28:02

# Read from the file file.txt and output all valid phone numbers to stdout.

# v1
cat file.txt | grep -P '^((\d{3}-\d{3}-\d{4})|(\(\d{3}\) \d{3}-\d{4}))$'

# v2 better
grep -P '^((\d{3}-\d{3}-\d{4})|(\(\d{3}\) \d{3}-\d{4}))$' file.txt
