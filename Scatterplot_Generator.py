import matplotlib.pyplot as plt
def read_entropy_data(filename):
    """
    Reads entropy comparison data from a file and extracts relevant values.
    Skips invalid or non-numeric rows.
    """
    plain_entropy = []
    bcrypt_entropy = []
    argon2_entropy = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(", ")
                if parts[0].isdigit():
                    plain_entropy.append(float(parts[1]))
                    bcrypt_entropy.append(float(parts[2]))
                    argon2_entropy.append(float(parts[3]))
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None, None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None, None
    return plain_entropy, bcrypt_entropy, argon2_entropy
def plot_combined_entropy(plain_entropy, bcrypt_entropy, argon2_entropy, save_as):
    """
    Creates a scatter plot comparing plain password entropy to hashed password entropy
    for both bcrypt and Argon2 on the same graph.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(plain_entropy, bcrypt_entropy, alpha=0.6, label='Bcrypt Entropy', color='orange')
    plt.scatter(plain_entropy, argon2_entropy, alpha=0.6, label='Argon2 Entropy', color='green')
    plt.xlabel('Plain Password Entropy', fontsize=12)
    plt.ylabel('Hashed Password Entropy', fontsize=12)
    plt.title('Plain vs. Hashed Password Entropy (Bcrypt and Argon2)', fontsize=14)
    plt.legend(fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.savefig(save_as)
    plt.show()
if __name__ == "__main__":
    filename = "entropy_comparison_results.txt"
    plain_entropy, bcrypt_entropy, argon2_entropy = read_entropy_data(filename)
    if plain_entropy and bcrypt_entropy and argon2_entropy:
        plot_combined_entropy(plain_entropy, bcrypt_entropy, argon2_entropy, "combined_entropy_comparison.png")
