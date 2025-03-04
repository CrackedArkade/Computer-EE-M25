import pandas as pd
import matplotlib.pyplot as plt
file_path = 'entropy_comparison_results.txt'
cleaned_file_path = 'cleaned_entropy_data.csv'
with open(file_path, 'r') as infile, open(cleaned_file_path, 'w') as outfile:
    header_found = False
    for line in infile:
        stripped_line = line.strip()
        if not header_found and stripped_line.startswith("Length") and "Plain" in stripped_line:
            header_found = True
            outfile.write(stripped_line + '\n')
        elif header_found:
            outfile.write(stripped_line + '\n')
try:
    data = pd.read_csv(cleaned_file_path)
    data.columns = data.columns.str.strip()
except Exception as e:
    print(f"Error reading the cleaned file: {e}")
    exit()
required_columns = ['Length', 'Plain', 'Bcrypt', 'Argon2']
if not all(col in data.columns for col in required_columns):
    print(f"Error: Missing one or more required columns: {required_columns}")
    exit()
data['Change_Argon2'] = data['Argon2'] - data['Plain']
data['Change_Bcrypt'] = data['Bcrypt'] - data['Plain']
plt.figure(figsize=(10, 6))
plt.plot(data['Length'], data['Change_Argon2'], label='Change in Entropy (Argon2)', marker='o')
plt.plot(data['Length'], data['Change_Bcrypt'], label='Change in Entropy (Bcrypt)', marker='o')
plt.xlabel('Password Length')
plt.ylabel('Change in Entropy')
plt.title('Password Length vs Change in Entropy (Hashed Passwords)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('password_entropy_change_comparison.png')
plt.show()
