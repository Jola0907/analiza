import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pymongo

# Dane
data = {
    'Limit': [25] * 10 + [15] * 10,
    'AVRO': [72.222, 72.193, 70.176, 69.438, 67.192, 64.076, 66.846, 75.598, 81.261, 83.557,
             58.937, 56.286, 57.101, 68.286, 62.384, 61.322, 59.884, 61.344, 58.823, 61.903],
    'ORC': [72.188, 74.19, 70.805, 69.66, 71.589, 69.515, 77.655, 67.998, 71.79, 73.981,
             41.611, 42.634, 42.533, 40.838, 40.953, 44.648, 41.354, 40.476, 40.468, 40.248],
    'PARQUET': [60.212, 60.192, 64.188, 58.183, 66.348, 64.988, 64.343, 64.76, 64.755, 88.99,
                 46.397, 41.888, 43.06, 47.3, 42.59, 41.878, 39.696, 42.125, 41.625, 45.887],
    'TXT': [56.736, 59.225, 56.29, 54.543, 54.726, 57.643, 54.471, 54.64, 53.356, 57.59,
             44.909, 43.949, 42.84, 41.86, 41.76, 42.66, 41.622, 41.77, 41.652, 44.682]
}

# Tworzenie DataFrame
df = pd.DataFrame(data)

# Wyłuskanie unikalnych formatów
unique_formats = df.columns[1:].tolist()

# Obliczanie średnich czasów i odchyleń standardowych
mean_times = df[unique_formats].mean().values
std_devs = df[unique_formats].std().values

df_limit_25 = df[df['Limit'] == 25]
df_limit_15 = df[df['Limit'] == 15]
# Średnie czasy i odchylenia standardowe dla każdego limitu
mean_times_limit_25 = df_limit_25[unique_formats].mean().values
std_devs_limit_25 = df_limit_25[unique_formats].std().values

mean_times_limit_15 = df_limit_15[unique_formats].mean().values
std_devs_limit_15 = df_limit_15[unique_formats].std().values

# Wykres porównawczy dla średnich czasów - Limit 15 i 25
plt.figure(figsize=(12, 5))
x = np.arange(len(unique_formats))
width = 0.35

plt.bar(x - width/2, mean_times_limit_25, width, yerr=std_devs_limit_25, capsize=5, label='Limit 25')
plt.bar(x + width/2, mean_times_limit_15, width, yerr=std_devs_limit_15, capsize=5, label='Limit 15')

plt.xlabel('Format danych')
plt.ylabel('Średni czas (ms)')
plt.title('Porównanie średnich czasów dla limitów 15 i 25')
plt.xticks(x, unique_formats)
plt.legend()
plt.grid(axis='y')
plt.show()

# Wykres porównawczy odchyleń standardowych - Limit 15 i 25
plt.figure(figsize=(12, 5))
plt.bar(x - width/2, std_devs_limit_25, width, label='Limit 25')
plt.bar(x + width/2, std_devs_limit_15, width, label='Limit 15')

plt.xlabel('Format danych')
plt.ylabel('Odchylenie standardowe (ms)')
plt.title('Porównanie odchyleń standardowych dla limitów 15 i 25')
plt.xticks(x, unique_formats)
plt.legend()
plt.grid(axis='y')
plt.show()

# Wykresy boxplot dla limitów 15 i 25
plt.figure(figsize=(12, 5))
plt.boxplot([df_limit_25[fmt].values for fmt in unique_formats], tick_labels=unique_formats, whis=1.5)
plt.xlabel('Format pliku')
plt.ylabel('Czas odpowiedzi (ms)')
plt.title('Czasy odpowiedzi dla limitu 25')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

plt.figure(figsize=(12, 5))
plt.boxplot([df_limit_15[fmt].values for fmt in unique_formats], tick_labels=unique_formats, whis=1.5)
plt.xlabel('Format pliku')
plt.ylabel('Czas odpowiedzi (ms)')
plt.title('Czasy odpowiedzi dla limitu 15')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# Wykres średniego czasu odpowiedzi dla limitów 15 i 25
plt.figure(figsize=(12, 5))
plt.plot(unique_formats, mean_times_limit_25, marker='o', label='Limit 25')
plt.plot(unique_formats, mean_times_limit_15, marker='o', label='Limit 15')

plt.xlabel('Format danych')
plt.ylabel('Średni czas odpowiedzi (ms)')
plt.title('Średni czas odpowiedzi dla limitów 15 i 25')
plt.grid(axis='y')
plt.legend()
plt.show()

# Wykresy średnich czasów dla każdego formatu danych
plt.figure(figsize=(12, 5))
plt.bar(unique_formats, mean_times, yerr=std_devs, capsize=5)
plt.xlabel('Format danych')
plt.ylabel('Średni czas (ms)')
plt.title('Średni czas wykonania zapytań w różnych formatach danych')
plt.grid(axis='y')
plt.show()

# Tworzenie wykresu boxplot dla wszystkich danych
all_times_flat = df[unique_formats].values.flatten()
group_labels = np.concatenate([[fmt]*len(df) for fmt in unique_formats])

plt.figure(figsize=(12, 5))
plt.boxplot([df[fmt].values for fmt in unique_formats], tick_labels=unique_formats, whis=1.5)
plt.xlabel('Format pliku')
plt.ylabel('Czas odpowiedzi (ms)')
plt.title('Czasy odpowiedzi dla różnych formatów danych')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# Uśrednienie wartości dla całej doby
mean_times_all_day = mean_times
std_devs_all_day = std_devs

# Wykres średniego czasu odpowiedzi z całej doby
plt.figure(figsize=(12, 5))
plt.bar(unique_formats, mean_times_all_day)
plt.xlabel('Format danych')
plt.ylabel('Średni czas z całej doby (ms)')
plt.title('Średni czas odpowiedzi z całej doby')
plt.grid(axis='y')
plt.show()

# Wykres odchyleń standardowych z całej doby
plt.figure(figsize=(12, 5))
plt.bar(unique_formats, std_devs_all_day)
plt.xlabel('Format danych')
plt.ylabel('Odchylenie standardowe z całej doby (ms)')
plt.title('Odchylenie standardowe z całej doby')
plt.grid(axis='y')
plt.show()






# Połączenie z MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['formaty']  # Zamień 'formaty' na nazwę swojej bazy danych
collection = db['data']  # Zamień 'data' na nazwę swojej kolekcji

# Pobieranie danych z MongoDB
data_cursor = collection.find()  # Pobieranie wszystkich dokumentów z kolekcji
data_list = list(data_cursor)  # Konwertowanie kursora na listę

# Tworzenie DataFrame z danych
df = pd.DataFrame(data_list)

# Zakładam, że kolumny zawierają listy wartości
def calculate_mean(series):
    # Spłaszczenie listy i obliczenie średniej
    return series.apply(lambda x: np.mean(x) if isinstance(x, list) and len(x) > 0 else 0)

# Obliczanie średnich dla każdej kolumny
mean_avro = calculate_mean(df['AVRO'])
mean_orc = calculate_mean(df['ORC'])
mean_parquet = calculate_mean(df['PARQUET'])
mean_text = calculate_mean(df['TEXT'])

# Wyświetlanie wyników
print("Średnie czasy AVRO:", mean_avro.mean())
print("Średnie czasy ORC:", mean_orc.mean())
print("Średnie czasy PARQUET:", mean_parquet.mean())
print("Średnie czasy TEXT:", mean_text.mean())

# Dodanie unikalnych formatów do listy
unique_formats = ['AVRO', 'ORC', 'PARQUET', 'TEXT']

# Obliczanie średnich czasów i odchyleń standardowych dla każdego zapytania
mean_times_limit_25 = df[unique_formats].apply(lambda col: np.mean([np.mean(x) for x in col if isinstance(x, list) and len(x) > 0]), axis=0)
std_devs_limit_25 = df[unique_formats].apply(lambda col: np.std([np.mean(x) for x in col if isinstance(x, list) and len(x) > 0]), axis=0)

mean_times_limit_15 = df[unique_formats].apply(lambda col: np.mean([np.mean(x) for x in col if isinstance(x, list) and len(x) > 0]), axis=0)
std_devs_limit_15 = df[unique_formats].apply(lambda col: np.std([np.mean(x) for x in col if isinstance(x, list) and len(x) > 0]), axis=0)

# Uśrednienie wartości dla całej doby
mean_times_all_day = mean_times_limit_25  # Dla zapytania limit 25
std_devs_all_day = std_devs_limit_25  # Dla zapytania limit 25
