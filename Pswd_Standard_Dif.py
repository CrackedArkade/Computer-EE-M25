import math
data = {
    "plain": {
        8: {'Lowercase': 28.06, 'Uppercase': 27.61, 'Digits': 10.48, 'Special': 33.86},
        9: {'Lowercase': 27.61, 'Uppercase': 27.39, 'Digits': 10.74, 'Special': 34.26},
        10: {'Lowercase': 27.66, 'Uppercase': 27.87, 'Digits': 10.61, 'Special': 33.86},
        11: {'Lowercase': 27.83, 'Uppercase': 27.49, 'Digits': 10.63, 'Special': 34.05},
        12: {'Lowercase': 27.56, 'Uppercase': 27.44, 'Digits': 10.82, 'Special': 34.18}
    },
    "bcrypt": {
        60: {'Lowercase': 37.65, 'Uppercase': 35.55, 'Digits': 18.64, 'Special': 8.15}
    },
    "argon2": {
        97: {'Lowercase': 38.69, 'Uppercase': 27.32, 'Digits': 20.63, 'Special': 13.37}
    }
}
def calculate_overall_std_deviation(data, group):
    """
    Calculates the overall mean and standard deviation across all character types for a given group.
    """
    char_types = ['Lowercase', 'Uppercase', 'Digits', 'Special']
    all_percentages = []
    for values in data[group].values():
        all_percentages.extend([values[char_type] for char_type in char_types])
    mean = sum(all_percentages) / len(all_percentages)
    variance = sum((x - mean) ** 2 for x in all_percentages) / len(all_percentages)
    std_dev = math.sqrt(variance)
    return mean, std_dev
plain_mean, plain_std_dev = calculate_overall_std_deviation(data, "plain")
bcrypt_mean, bcrypt_std_dev = calculate_overall_std_deviation(data, "bcrypt")
argon2_mean, argon2_std_dev = calculate_overall_std_deviation(data, "argon2")
print(f"Plain Passwords:\n  Mean: {plain_mean:.2f}%\n  Standard Deviation: {plain_std_dev:.2f}%")
print(f"Bcrypt Hashed Passwords:\n  Mean: {bcrypt_mean:.2f}%\n  Standard Deviation: {bcrypt_std_dev:.2f}%")
print(f"Argon2 Hashed Passwords:\n  Mean: {argon2_mean:.2f}%\n  Standard Deviation: {argon2_std_dev:.2f}%")
