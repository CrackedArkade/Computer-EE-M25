import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr
password_lengths = [8, 9, 10, 11, 12]
plain_entropies = [2.9239, 3.0855, 3.2300, 3.3559, 3.4673]
bcrypt_entropies = [5.1043, 5.1004, 5.1036, 5.1042, 5.1059]
argon2_entropies = [5.4595, 5.4584, 5.4519, 5.4567, 5.4573]
bcrypt_gain = np.array(bcrypt_entropies) - np.array(plain_entropies)
argon2_gain = np.array(argon2_entropies) - np.array(plain_entropies)
bcrypt_corr, _ = pearsonr(password_lengths, bcrypt_gain)
argon2_corr, _ = pearsonr(password_lengths, argon2_gain)
print(f"Correlation between length and bcrypt entropy gain: {bcrypt_corr:.4f}")
print(f"Correlation between length and Argon2 entropy gain: {argon2_corr:.4f}")
plt.figure(figsize=(10, 6))
plt.scatter(password_lengths, bcrypt_gain, color='orange', label='Bcrypt Gain')
plt.scatter(password_lengths, argon2_gain, color='green', label='Argon2 Gain')
z1 = np.polyfit(password_lengths, bcrypt_gain, 1)
z2 = np.polyfit(password_lengths, argon2_gain, 1)
plt.plot(password_lengths, np.poly1d(z1)(password_lengths), color='orange', linestyle='--')
plt.plot(password_lengths, np.poly1d(z2)(password_lengths), color='green', linestyle='--')
plt.xlabel('Password Length', fontsize=12)
plt.ylabel('Entropy Gain', fontsize=12)
plt.title('Entropy Gain vs. Password Length', fontsize=14)
plt.legend(fontsize=10)
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig("entropy_gain_vs_length.png")
plt.show()
