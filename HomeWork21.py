import re
#
# # Task 1 Write a regular expression that finds fragments in the text consisting of one letter R followed by one or more letters b followed by one r. 
# Take into account upper and lower case.

my_str = "This is Rbr simple text Rbbr for example Rbbbr"
res = re.findall(r"[Rr]b+r", my_str)
print(res)

# # Task 2  Write a function that validates a bank card number 

def valid_bank_card(card):
    result = re.match('^([0-9]{4}[- ]?){3}[0-9]{4}$', card)
    if result:
        return "Valid"
    return "Failed"

print(valid_bank_card("4141-4949-5656-7878"))

#
# # Task 3 Write a function that accepts string data and checks if it matches the email.
# Requirements:
# -Numbers (0-9).
# -Only Latin letters in uppercase (A-Z) and lowercase (a-z).
# -Only the characters "_" and "-" are allowed in the body of the email. But they cannot be the first character of the email.
# -The "-" character cannot be repeated.
#
def valid_email(mail):
    result = '^[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+@[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$'
    if re.search(result, mail):
        return "Valid"
    return "Failed"

print(valid_email("gkarabetskii@gmail.com"))

# # Task 4 Write a function that checks if the login is correct. A valid login is a string of 2 to 10 characters containing only letters and numbers.

def valid_login(login):
    if re.fullmatch('^[A-Za-z0-9]{2,10}$', login):
        return "Valid"
    return "Failed"

print(valid_login("eazakmi777"))

