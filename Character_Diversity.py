import string
def read_passwords_from_file(filename):
    """
    Reads passwords from a text file and returns them as a list of strings.
    """
    try:
        with open(filename, 'r') as file:
            passwords = [line.strip() for line in file if line.strip()]
        print(f"Successfully read {len(passwords)} passwords from {filename}.")
        return passwords
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return []
def calculate_character_diversity(passwords):
    """
    Calculates character diversity for a list of passwords.
    Returns a dictionary with percentages of lowercase, uppercase, numbers, and special characters.
    """
    char_types = {
        'lowercase': string.ascii_lowercase,
        'uppercase': string.ascii_uppercase,
        'digits': string.digits,
        'special': string.punctuation
    }
    char_type_count = {key: 0 for key in char_types}
    for pwd in passwords:
        for char in pwd:
            if char in char_types['lowercase']:
                char_type_count['lowercase'] += 1
            elif char in char_types['uppercase']:
                char_type_count['uppercase'] += 1
            elif char in char_types['digits']:
                char_type_count['digits'] += 1
            elif char in char_types['special']:
                char_type_count['special'] += 1
    total_chars = sum(char_type_count.values())
    if total_chars == 0:
        return {key: 0 for key in char_types}
    char_type_percentage = {key: (count / total_chars) * 100 for key, count in char_type_count.items()}
    return char_type_percentage
def calculate_diversity_by_length(passwords):
    """
    Calculates average character diversity grouped by password length.
    """
    passwords_by_length = {}
    for pwd in passwords:
        pwd_length = len(pwd)
        if pwd_length not in passwords_by_length:
            passwords_by_length[pwd_length] = []
        passwords_by_length[pwd_length].append(pwd)
    diversity_by_length = {}
    for length, pwd_list in passwords_by_length.items():
        if pwd_list:
            diversity_by_length[length] = calculate_character_diversity(pwd_list)
        else:
            diversity_by_length[length] = {key: 0 for key in string.ascii_lowercase}
    return diversity_by_length
def print_diversity_results(diversity_results):
    """
    Prints the character diversity results.
    """
    for length, avg_diversity in sorted(diversity_results.items()):
        print(f"Password length {length}:")
        for char_type, percentage in avg_diversity.items():
            print(f"  {char_type.capitalize()}: {percentage:.2f}%")
        print("")
if __name__ == "__main__":
    plain_password_file = "plain_passwords.txt"
    bcrypt_file = "bcrypt_hashed_passwords.txt"
    argon2_file = "argon2_hashed_passwords.txt"
    plain_passwords = read_passwords_from_file(plain_password_file)
    bcrypt_passwords = read_passwords_from_file(bcrypt_file)
    argon2_passwords = read_passwords_from_file(argon2_file)
    print("\nPlain Password Diversity:")
    plain_diversity = calculate_diversity_by_length(plain_passwords)
    print_diversity_results(plain_diversity)
    print("\nBcrypt Hashed Password Diversity:")
    bcrypt_diversity = calculate_diversity_by_length(bcrypt_passwords)
    print_diversity_results(bcrypt_diversity)
    print("\nArgon2 Hashed Password Diversity:")
    argon2_diversity = calculate_diversity_by_length(argon2_passwords)
    print_diversity_results(argon2_diversity)
