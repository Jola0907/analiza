import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import shapiro, kruskal

# Przygotowanie danych
data = {
    "user": ["user1", "user2", "user3", "user4", "user5", "user6", "user7", "user8", "user9", "user10"],
    "Q1": ["Nigdy", "Często", "Czasami", "Nigdy", "Rzadko", "Czasami", "Nigdy", "Często", "Czasami", "Nigdy"],
    "Q2": ["Często", "Czasami", "Często", "Rzadko", "Czasami", "Czasami", "Nigdy", "Nigdy", "Często", "Nigdy"],
    "Q3": ["Czasami", "Czasami", "Czasami", "Nigdy", "Nigdy", "Czasami", "Nigdy", "Często", "Czasami", "Czasami"],
    "Q4": ["Często", "Czasami", "Często", "Nigdy", "Rzadko", "Nigdy", "Czasami", "Często", "Czasami", "Czasami"],
    "Q5": ["Często", "Nigdy", "Rzadko", "Nigdy", "Nigdy", "Nigdy", "Nigdy", "Nigdy", "Rzadko", "Nigdy"],
    "Q6": ["Nigdy", "Często", "Czasami", "Często", "Często", "Często", "Czasami", "Często", "Często", "Rzadko"],
    "Q7": ["Często", "Rzadko", "Nigdy", "Czasami", "Często", "Rzadko", "Czasami", "Czasami", "Nigdy", "Często"],
    "Q8": ["Rzadko", "Czasami", "Często", "Nigdy", "Czasami", "Czasami", "Często", "Często", "Często", "Czasami"],
    "Q9": ["Nigdy", "Często", "Rzadko", "Czasami", "Nigdy", "Często", "Rzadko", "Nigdy", "Czasami", "Rzadko"],
    "Q10": ["Często", "Często", "Często", "Często", "Często", "Często", "Często", "Często", "Rzadko", "Często"],
    "Q11": ["Czasami", "Rzadko", "Czasami", "Rzadko", "Rzadko", "Czasami", "Rzadko", "Rzadko", "Często", "Czasami"],
    "Q12": ["Nigdy", "Często", "Nigdy", "Czasami", "Często", "Często", "Rzadko", "Często", "Nigdy", "Często"],
    "Q13": ["Często", "Nigdy", "Czasami", "Często", "Nigdy", "Nigdy", "Czasami", "Rzadko", "Czasami", "Nigdy"],
    "Q14": ["Rzadko", "Rzadko", "Często", "Czasami", "Często", "Rzadko", "Czasami", "Czasami", "Rzadko", "Często"],
    "Q15": ["Czasami", "Często", "Często", "Rzadko", "Często", "Rzadko", "Często", "Czasami", "Rzadko", "Często"],
}

df = pd.DataFrame(data)

# Konwersja odpowiedzi na numeryczne z uwzględnieniem "Bardzo często"
conversion = {
    "Nigdy": 1,
    "Rzadko": 2,
    "Czasami": 3,
    "Często": 4,
    "Bardzo często": 5
}

# Zastosowanie konwersji
for col in df.columns[1:]:
    df[col] = df[col].map(conversion)

# Sprawdzenie normalności rozkładów
normality_results = {}
for col in df.columns[1:]:
    stat, p = shapiro(df[col])
    normality_results[col] = (stat, p)

# Test Kruskala-Wallisa
kruskal_results = {}
for col in df.columns[1:]:
    kruskal_stat, kruskal_p = kruskal(*[df[col][df['user'] == user] for user in df['user']])
    kruskal_results[col] = (kruskal_stat, kruskal_p)

# Wykresy
plt.figure(figsize=(20, 15))
for i, col in enumerate(df.columns[1:], 1):
    plt.subplot(4, 4, i)
    sns.countplot(x=df[col], palette="pastel", order=[1, 2, 3, 4, 5])
    plt.title(f'Wykres dla {col}', fontsize=16)
    plt.xlabel('Odpowiedzi (1-5)', fontsize=14)
    plt.ylabel('Liczba odpowiedzi', fontsize=14)
    plt.xticks(ticks=[0, 1, 2, 3, 4], labels=[1, 2, 3, 4, 5], rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

# Wyświetlenie wyników analizy normalności i Kruskala-Wallisa
print("Wyniki testu normalności (Shapiro-Wilk):")
for col, (stat, p) in normality_results.items():
    print(f"{col}: Statystyka = {stat:.4f}, Wartość p = {p:.4f}")

print("\nWyniki testu Kruskala-Wallisa:")
for col, (stat, p) in kruskal_results.items():
    print(f"{col}: Statystyka H = {stat:.4f}, Wartość p = {p:.4f}")
