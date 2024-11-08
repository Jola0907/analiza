import pyarrow.parquet as pq
import pyarrow.compute as pc
import pandas as pd
import time

# Mierzenie czasu przetwarzania
start_time = time.time()

# Odczyt danych z HDFS
movies = pq.read_table('/user/hive/warehouse/baza48239.db/movies_parquet/000000_0', filesystem='hdfs://31.193.99.136:9000')
ratings = pq.read_table('hdfs://31.193.99.136:9000/user/hive/warehouse/pk.db/ratings_pq')

# 1. Najpopularniejsze typy filmów (genres)
# Zakładam, że w tabeli movies znajduje się kolumna 'genres', która zawiera informacje o typach filmów
grouped_genres = movies.group_by("genres").aggregate([("movieid", "count")])  # Zakładam, że kolumna 'movieid' istnieje
top_10_genres = grouped_genres.sort_by([("movieid_count", "descending")]).slice(0, 10)  # 10 najpopularniejszych

print("Top 10 genres:")
print(top_10_genres)

# 2. Użytkownicy z najniższą średnią ocen, którzy ocenili co najmniej 15 filmów
movies_df = movies.to_pandas()
ratings_df = ratings.to_pandas()

# Grupowanie ocen po użytkownikach
user_ratings = ratings_df.groupby('userid').agg({'rating': ['mean', 'count']})
filtered_users = user_ratings[user_ratings[('rating', 'count')] >= 15]  # Filtruj użytkowników, którzy ocenili min. 15 filmów
lowest_avg_ratings = filtered_users.sort_values([('rating', 'mean')]).head(10)  # 10 użytkowników z najniższą średnią ocen

print("\nUsers with lowest average ratings (who rated at least 15 movies):")
print(lowest_avg_ratings)

# Mierzenie czasu przetwarzania
end_time = time.time()
print(f"\nProcessing time: {end_time - start_time} seconds")
