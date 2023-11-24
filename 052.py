def check_exist(number, factor):
    if len(str(number)) == len(str(6*number)):
        for i in str(number):
            if i not in str(factor * number):
                return False
        return True
    else:
        return False

def check_all(number):
    checks = []
    for i in range(1,7):
        checks.append(check_exist(number, i))
    return all(checks)

number = 1
match_found = False
while not match_found:
    if check_all(number):
        match_found = True
        magic_number = number
    number += 1

print('Answer:', magic_number)
