# Import required libraries
import nltk
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Load tweets data
comments_data = pd.read_csv('25k-twts_samsung-mobile_01Jan2011-31Dec2018_English.csv', encoding='ISO-8859-1')

# Filter tweets containing specific keywords
comments_data = comments_data[comments_data['comment_text'].str.contains('mobile|mobiles|phone|phones|Mobile|Mobiles'
                                                                         '|Phone|Phones')]

# Randomly sample 1000 tweets
comments_data = comments_data.sample(n=500)

# Define the sentiment analyzer
sid = SentimentIntensityAnalyzer()


# Define function to calculate sentiment polarity using NLTK
def get_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    text_str = str(text)  # convert to string
    polarity_scores = sid.polarity_scores(text_str)
    sentiment = polarity_scores['compound']
    return sentiment


# Apply sentiment analysis to tweets data
comments_data['sentiment_polarity'] = comments_data['comment_text'].apply(get_sentiment)

# Classify sentiment labels based on polarity score
comments_data['sentiment_label'] = comments_data['sentiment_polarity'].apply(
    lambda score: 'positive' if score > 0 else 'negative' if score < 0 else 'neutral')

# Export the sentiment analysis results to a csv file
comments_data[['comment_text', 'sentiment_polarity', 'sentiment_label']].to_csv('sentiment_analysis_apple.csv',
                                                                                index=False)

# Display the sentiment analysis results
print(comments_data[['comment_text', 'sentiment_polarity', 'sentiment_label']])
