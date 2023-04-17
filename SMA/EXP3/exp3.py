import pandas as pd
import numpy as np

data = pd.read_csv('dataset_pinterest-crawler_2023-02-16_07-03-21-692.csv')
print("\nLocating missing data")

print(data.isnull().head(10))
print("")
print("")
print(data.isnull().sum().head(10))

remove = ['product_pin_data', 'embed', 'alt_text', 'insertion_id', 'promoted_lead_form', 'promoter',
          'promoter/ads_only_profile_site', 'promoter/full_name', 'promoter/id', 'promoter/image_large_url',
          'promoter/image_small_url', 'promoter/is_ads_only_profile', 'promoter/username', 'repin_count',
          'video_status_message', 'videos', 'title', 'video_status', 'story_pin_data_id', 'story_pin_data']
print("\n\nDrop the data")
print("")
print(data.drop(remove, inplace=True, axis=1))

print("\nInput missing data")
print("")
data['grid_title'] = data['grid_title'].fillna('No gird_title')
data['link'] = data['link'].fillna('No link')
print(data.duplicated().head(10))

print("\nCheck for Duplicates")
print("")
print(data.drop_duplicates().head(10))

print("\nDetect Outliers")
print("")
print(data['aggregated_pin_data/saves'].describe().head(10))
data.loc[10, 'aggregated_pin_data/saves'] = 1
data['domain'] = data['domain'].str.lower()
print("\nNormalize Casing")
print("")
print(data['domain'].head(10))

data['grid_description'] = data['grid_description'].str.title()
print("")
print("")
print(data['grid_description'].head(10))


data.to_csv('cleaned_dataset_exp3.csv', index=False)