import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# PAGE SETTINGS
st.set_page_config(page_title="Movie Ratings Dashboard", layout="wide")

# TITLE
st.title("🎬 Movie Ratings Dashboard")
st.write("Analyzing and Visualizing Movie Ratings")

# LOAD DATA
df = pd.read_csv("movies.csv")

# SHOW DATA
st.subheader("Dataset Preview")
st.dataframe(df.head())

# SUMMARY STATS
st.subheader("Summary Statistics")

rating_col = "Rating"   # change if your column name differs

mean_rating = df[rating_col].mean()
median_rating = df[rating_col].median()
max_rating = df[rating_col].max()

col1, col2, col3 = st.columns(3)

col1.metric("Average Rating", round(mean_rating, 2))
col2.metric("Median Rating", round(median_rating, 2))
col3.metric("Highest Rating", max_rating)

# HISTOGRAM
st.subheader("Ratings Distribution")

fig, ax = plt.subplots(figsize=(8, 4))
sns.histplot(df[rating_col], bins=10, kde=True, ax=ax)

st.pyplot(fig)

# TOP MOVIES
st.subheader("Top Rated Movies")

top_movies = df.sort_values(by=rating_col, ascending=False).head(10)

st.dataframe(top_movies)

# GENRE ANALYSIS
if "Genre" in df.columns:

    st.subheader("Average Rating by Genre")

    genre_avg = df.groupby("Genre")[rating_col].mean().sort_values(ascending=False)

    fig2, ax2 = plt.subplots(figsize=(10, 5))

    genre_avg.plot(kind="bar", ax=ax2)

    plt.xticks(rotation=45)

    st.pyplot(fig2)

# BOXPLOT
st.subheader("Box Plot of Ratings")

fig3, ax3 = plt.subplots(figsize=(8, 2))

sns.boxplot(x=df[rating_col], ax=ax3)

st.pyplot(fig3)

# FOOTER
st.success("Dashboard Loaded Successfully ✅")
