import pdb
import scipy.stats as stats
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Dane do konwersji
data = [
    ['Nigdy', 'Często', 'Często', 'Bardzo często', 'Często', 'Czasami', 'Czasami', 'Nigdy', 'Nigdy', 'Czasami', 'Bardzo często', 'Bardzo często', 'Nigdy', 'Bardzo często'],
    ['Często', 'Czasami', 'Czasami', 'Czasami', 'Nigdy', 'Rzadko', 'Czasami', 'Nigdy', 'Rzadko', 'Nigdy', 'Nigdy', 'Nigdy', 'Nigdy', 'Nigdy', 'Nigdy'],
    ['Czasami', 'Często', 'Czasami', 'Często', 'Rzadko', 'Często', 'Czasami', 'Czasami', 'Czasami', 'Czasami', 'Czasami', 'Czasami', 'Często', 'Czasami', 'Czasami'],
    ['Nigdy', 'Rzadko', 'Nigdy', 'Nigdy', 'Nigdy', 'Nigdy', 'Nigdy', 'Nigdy', 'Nigdy', 'Rzadko', 'Nigdy', 'Nigdy', 'Nigdy', 'Nigdy', 'Nigdy'],
    ['Rzadko', 'Czasami', 'Nigdy', 'Rzadko', 'Nigdy', 'Czasami', 'Nigdy', 'Nigdy', 'Nigdy', 'Rzadko', 'Nigdy', 'Nigdy', 'Nigdy', 'Nigdy', 'Rzadko'],
    ['Czasami', 'Czasami', 'Czasami', 'Nigdy', 'Nigdy', 'Nigdy', 'Nigdy', 'Nigdy', 'Nigdy', 'Nigdy', 'Nigdy', 'Nigdy', 'Czasami', 'Nigdy', 'Czasami'],
    ['Nigdy', 'Nigdy', 'Nigdy', 'Czasami', 'Nigdy', 'Nigdy', 'Czasami', 'Nigdy', 'Nigdy', 'Rzadko', 'Nigdy', 'Nigdy', 'Czasami', 'Nigdy', 'Nigdy'],
    ['Często', 'Nigdy', 'Często', 'Często', 'Nigdy', 'Często', 'Często', 'Nigdy', 'Rzadko', 'Nigdy', 'Nigdy', 'Nigdy', 'Nigdy', 'Nigdy', 'Bardzo często'],
    ['Czasami', 'Często', 'Czasami', 'Czasami', 'Rzadko', 'Nigdy', 'Czasami', 'Nigdy', 'Rzadko', 'Często', 'Czasami', 'Czasami', 'Czasami', 'Nigdy', 'Czasami'],
    ['Nigdy', 'Nigdy', 'Czasami', 'Czasami', 'Nigdy', 'Czasami', 'Często', 'Rzadko', 'Rzadko', 'Czasami', 'Nigdy', 'Rzadko', 'Rzadko', 'Nigdy', 'Bardzo często'],
]

# Mapa konwersji wartości na liczby
conversion_map = {
    'Nigdy': 0,
    'Rzadko': 1,
    'Czasami': 2,
    'Często': 3,
    'Bardzo często': 4
}


numeric_data = [[conversion_map[response] for response in row] for row in data]

# Wyświetlanie wyników
for row in numeric_data:
    print(row)


df = pd.DataFrame(data)

# Wyświetl dane
print(df)

def count_responses(df):
    return df.apply(pd.Series.value_counts).fillna(0)

response_counts = count_responses(df)
print(response_counts)
#