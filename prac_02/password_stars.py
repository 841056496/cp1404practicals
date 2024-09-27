"""
Pseudocode:
main function:
    password = get_password(min_length)
    print_asterisks(password)

get_password function:
    Get password
    while len(password)<min_length:
        print error
        Get password
    return password

print_asterisks() function:
    print('*' * len(password))

main()
"""
min_length = 8
def main():
    password = get_password(min_length)
    print_asterisks(password)
def get_password(min_length):
    password = input("Please enter password: ")
    while len(password) < min_length:
        print("Too short! Enter again!")
        password = input("Please enter password: ")
    return password

def print_asterisks(password):
    print('*' * len(password))

main()
