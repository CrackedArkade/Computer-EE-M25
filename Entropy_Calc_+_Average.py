import math
from collections import defaultdict
def calculate_entropy(password):
    """
    Calculate the Shannon entropy of a string.
    """
    if not password:
        return 0.0
    frequency = {}
    for char in password:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    length = len(password)
    entropy = 0.0
    for count in frequency.values():
        probability = count / length
        entropy -= probability * math.log2(probability)
    return entropy
def process_passwords(plain_file, bcrypt_file, argon2_file, output_file):
    """
    Process the three input files and save entropy comparisons to an output file.
    """
    try:
        with open(plain_file, 'r') as pf, open(bcrypt_file, 'r') as bf, open(argon2_file, 'r') as af:
            plain_passwords = [line.strip() for line in pf if line.strip()]
            bcrypt_passwords = [line.strip() for line in bf if line.strip()]
            argon2_passwords = [line.strip() for line in af if line.strip()]
        if len(plain_passwords) != len(bcrypt_passwords) or len(plain_passwords) != len(argon2_passwords):
            raise ValueError("Mismatch in the number of passwords across files.")
        results = []
        length_groups = defaultdict(list)
        for i, plain_password in enumerate(plain_passwords):
            plain_entropy = calculate_entropy(plain_password)
            bcrypt_entropy = calculate_entropy(bcrypt_passwords[i])
            argon2_entropy = calculate_entropy(argon2_passwords[i])
            results.append(
                f"{i + 1}, {plain_entropy:.4f}, {bcrypt_entropy:.4f}, {argon2_entropy:.4f}"
            )
            password_length = len(plain_password)
            length_groups[password_length].append(
                (plain_entropy, bcrypt_entropy, argon2_entropy)
            )
        results.append("\nAverage Entropy by Password Length:")
        results.append("Length, Plain, Bcrypt, Argon2, Avg. Change (Bcrypt), Avg. Change (Argon2)")
        for length, entropies in sorted(length_groups.items()):
            avg_plain = sum(e[0] for e in entropies) / len(entropies)
            avg_bcrypt = sum(e[1] for e in entropies) / len(entropies)
            avg_argon2 = sum(e[2] for e in entropies) / len(entropies)
            avg_change_bcrypt = avg_bcrypt - avg_plain
            avg_change_argon2 = avg_argon2 - avg_plain

            results.append(
                f"{length}, {avg_plain:.4f}, {avg_bcrypt:.4f}, {avg_argon2:.4f}, {avg_change_bcrypt:.4f}, {avg_change_argon2:.4f}"
            )
        with open(output_file, 'w') as out_file:
            out_file.write("Password No., Original Entropy, Bcrypt Entropy, Argon2 Entropy\n")
            out_file.write("\n".join(results))
        print(f"Results saved to {output_file}")
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    plain_passwords_file = "plain_passwords.txt"
    bcrypt_hashed_passwords_file = "bcrypt_hashed_passwords.txt"
    argon2_hashed_passwords_file = "argon2_hashed_passwords.txt"
    output_results_file = "entropy_comparison_results.txt"
    process_passwords(
        plain_passwords_file, bcrypt_hashed_passwords_file,
        argon2_hashed_passwords_file, output_results_file
    )
