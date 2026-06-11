import pandas as pd
import matplotlib.pyplot as plt
import os

# Create images folder if not exists
os.makedirs("images", exist_ok=True)

# Load dataset
df = pd.read_csv("data/netflix_titles.csv")

print("=" * 60)
print("NETFLIX DATA ANALYSIS PROJECT")
print("=" * 60)

# Dataset Overview
print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

# --------------------------------------------------
# Movies vs TV Shows
# --------------------------------------------------

print("\nMovies vs TV Shows:")
print(df["type"].value_counts())

plt.figure(figsize=(6,4))
df["type"].value_counts().plot(kind="bar")
plt.title("Movies vs TV Shows")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("images/movies_vs_tvshows.png")
plt.show()

# --------------------------------------------------
# Top 10 Countries
# --------------------------------------------------

country_data = df["country"].dropna().str.split(", ").explode()

print("\nTop 10 Countries:")
print(country_data.value_counts().head(10))

plt.figure(figsize=(8,5))
country_data.value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Countries")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("images/top_countries.png")
plt.show()

# --------------------------------------------------
# Content Ratings
# --------------------------------------------------

print("\nTop Ratings:")
print(df["rating"].value_counts().head(10))

plt.figure(figsize=(8,5))
df["rating"].value_counts().head(10).plot(kind="bar")
plt.title("Content Ratings")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("images/content_ratings.png")
plt.show()

# --------------------------------------------------
# Content Added Per Year
# --------------------------------------------------

df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
df["year_added"] = df["date_added"].dt.year

plt.figure(figsize=(10,5))
df["year_added"].value_counts().sort_index().plot()
plt.title("Netflix Content Added By Year")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.savefig("images/content_by_year.png")
plt.show()

# --------------------------------------------------
# Top Genres
# --------------------------------------------------

genre_data = df["listed_in"].str.split(", ").explode()

print("\nTop Genres:")
print(genre_data.value_counts().head(10))

plt.figure(figsize=(10,5))
genre_data.value_counts().head(10).plot(kind="bar")
plt.title("Top Genres on Netflix")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("images/top_genres.png")
plt.show()

print("\nProject Completed Successfully!")
print("Graphs saved inside images folder.")