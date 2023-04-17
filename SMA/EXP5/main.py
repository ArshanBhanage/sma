import pandas as pd
import matplotlib.pyplot as plt

# Load movie trailer comments data
comments_data = pd.read_csv('sentiment_analysis.csv')

# Plot the sentiment distribution
plt.hist(comments_data['sentiment_polarity'], bins=20)
plt.xlabel('Sentiment Polarity')
plt.ylabel('Frequency')
plt.title('Sentiment Distribution of Movie Trailer Comments')
plt.show()

# Plot the sentiment labels distribution
labels = comments_data['sentiment_label'].value_counts().index.tolist()
sizes = comments_data['sentiment_label'].value_counts().tolist()
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Sentiment Label Distribution of Movie Trailer Comments')
plt.show()