# Load libraries
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('cleaned_dataset.csv')

# Create the plot
print(data.columns)
sns.boxplot(x='aggregated_pin_data_saves', data=data)

# Create a histogram of the aggregated_pin_data_saves variable
sns.displot(data.aggregated_pin_data_saves, bins=50, kde=False)
plt.figure()
# Create a barplot of the counts in the board_name variable
# The palette parameter will set the color scheme for the plot
# Create the first plot (bar plot)
sns.countplot(x='board_name', data=data)
plt.title('Board Name Counts')

# Create the second plot (pie chart)
board_name_labels = ["Afternoon Treats", "The Third B", "What we love", "Porch party", "Sweet breakfasts",
                     "Savory breakfasts", "Upkeep!"]
sizes = data.board_name.value_counts().values
plt.figure()
plt.pie(sizes, labels=board_name_labels)
plt.title('Board Name Proportions')

# Display the plots side by side
plt.subplots_adjust(wspace=0.5)
plt.figure()
# multivariate
# Create a box plot of the image_width variable relative to image_width
sns.boxplot(x='image_height', y='image_width', data=data, palette='Accent')

plt.show()
