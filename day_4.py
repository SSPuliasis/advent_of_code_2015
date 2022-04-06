import hashlib

#Part1
def part_1(input_string):
    potential_number = 0
    secret_code = input_string+str(potential_number)
    hexi = hashlib.md5(secret_code.encode())
    while hexi.hexdigest()[0:5] != '00000':
        potential_number += 1
        secret_code = input_string+str(potential_number)
        hexi = hashlib.md5(secret_code.encode())  
    else:
        print(potential_number)
        
#Part 2
def part_2(input_string):
    potential_number = 0
    secret_code = input_string+str(potential_number)
    hexi = hashlib.md5(secret_code.encode())
    while hexi.hexdigest()[0:6] != '000000':
        potential_number += 1
        secret_code = input_string+str(potential_number)
        hexi = hashlib.md5(secret_code.encode())  
    else:
        print(potential_number)
