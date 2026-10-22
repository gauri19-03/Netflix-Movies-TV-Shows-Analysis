
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("netflix_titles.csv")

print(df.head())

print(df.info())

print(df.isnull().sum())

df = df.drop_duplicates()

sns.countplot(data=df, x="type")
plt.title("Movies vs TV Shows")
plt.show()

genres = df["listed_in"].str.split(", ").explode()
genres.value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Genres")
plt.show()

df["rating"].value_counts().plot(kind="bar")
plt.title("Content Ratings")
plt.show()


df["release_year"].value_counts().sort_index().plot()
plt.title("Netflix Titles by Release Year")
plt.show()


countries = df["country"].dropna().str.split(", ").explode()
countries.value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Countries")
plt.show()

df.to_csv("netflix_cleaned.csv", index=False)

movies = df[df["type"] == "Movie"]

duration = movies["duration"].str.extract(r"(\d+)")[0]
duration = pd.to_numeric(duration, errors="coerce")

duration.dropna().plot(kind="hist", bins=20)
plt.title("Movie Duration Distribution")
plt.xlabel("Duration (minutes)")
plt.show()
print(df["type"].value_counts(normalize=True) * 100)
print("Analysis completed!")

