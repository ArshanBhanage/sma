import pandas as pd

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('negative_sentiment_analysis.csv')
print(df.head)
# Define the keywords to search for
keywords = ['audio', 'quality', 'jack', 'bluetooth', 'sound', 'pain']

# Initialize a dictionary to hold the comments for each keyword
comments_by_keyword = {keyword: [] for keyword in keywords}

# Loop through each row in the DataFrame and add the comment to the appropriate keyword list
for index, row in df.iterrows():
    comment = row['review'].lower()
    for keyword in keywords:
        if keyword in comment:
            comments_by_keyword[keyword].append(comment)

# Export the comments for each keyword to a separate CSV file
for keyword in keywords:
    comments_df = pd.DataFrame({keyword: comments_by_keyword[keyword]})
    #print(comments_df)
    comments_df.to_csv(f'{keyword}_comments.csv', index=False)
