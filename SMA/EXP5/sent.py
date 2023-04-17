# Import required libraries
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Load movie trailer comments data
comments_data = pd.read_csv('Dunkirk.csv')

# Randomly sample 1000 comments
comments_data = comments_data.sample(n=1000)

# Define the sentiment analyzer
sid = SentimentIntensityAnalyzer()


# Define function to calculate sentiment polarity using NLTK
def get_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    text_str = str(text)  # convert to string
    polarity_scores = sid.polarity_scores(text_str)
    sentiment = polarity_scores['compound']
    return sentiment


# Apply sentiment analysis to comments data
comments_data['sentiment_polarity'] = comments_data['comment_text'].apply(get_sentiment)

# Classify sentiment labels based on polarity score
comments_data['sentiment_label'] = comments_data['sentiment_polarity'].apply(
    lambda score: 'positive' if score > 0 else 'negative' if score < 0 else 'neutral')

# Export the sentiment analysis results to a csv file
comments_data[['comment_text', 'sentiment_polarity', 'sentiment_label']].to_csv('sentiment_analysis.csv', index=False)

# Display the sentiment analysis results
print(comments_data[['comment_text', 'sentiment_polarity', 'sentiment_label']])



