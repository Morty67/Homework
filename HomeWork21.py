import re
#
# # Task 1

my_str = "This is Rbr simple text Rbbr for example Rbbbr"
res = re.findall(r"[Rr]b+r", my_str)
print(res)

# # Task 2

def valid_bank_card(card):
    result = re.match('^([0-9]{4}[- ]?){3}[0-9]{4}$', card)
    if result:
        return "Valid"
    return "Failed"

print(valid_bank_card("4141-4949-5656-7878"))

#
# # Task 3
#
def valid_email(mail):
    result = '^[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+@[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$'
    if re.search(result, mail):
        return "Valid"
    return "Failed"

print(valid_email("gkarabetskii@gmail.com"))

# # Task 4

def valid_login(login):
    if re.fullmatch('^[A-Za-z0-9]{2,10}$', login):
        return "Valid"
    return "Failed"

print(valid_login("eazakmi777"))

