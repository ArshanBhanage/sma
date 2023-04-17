import pandas as pd
import matplotlib.pyplot as plt

# Read the Samsung tweets dataset
samsung_data = pd.read_csv('sentiment_analysis_samsung.csv', nrows=500)

# Read the Apple tweets dataset
apple_data = pd.read_csv('sentiment_analysis_apple.csv', nrows=500)

# Group the tweets by sentiment_label and count the number of tweets
samsung_sentiments = samsung_data.groupby('sentiment_label')['comment_text'].count()
apple_sentiments = apple_data.groupby('sentiment_label')['comment_text'].count()

# Define color codes for each bar
colors = ['#FFC300', '#FF5733', '#C70039']

# Plot a bar chart to visualize the sentiment distribution
fig, ax = plt.subplots()
samsung_sentiments.plot(kind='bar', ax=ax, position=0, width=0.4, label='Samsung', color=colors[0])
apple_sentiments.plot(kind='bar', ax=ax, position=1, width=0.4, label='Apple', color=colors[1])
ax.set_xlabel('Sentiment Label')
ax.set_ylabel('Number of Tweets')
ax.legend()
plt.show()
