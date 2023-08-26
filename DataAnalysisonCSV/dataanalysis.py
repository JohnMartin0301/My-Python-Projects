import pandas as pd
import numpy as np

# Load the CSV file into a Pandas DataFrame
csv_file = ''
df = pd.read_csv(csv_file)

# Display basic information about the dataset
print("Basic Information about the Dataset:")
print(df.info())

# Display the first few rows of the dataset
print("\nFirst few rows of the dataset:")
print(df.head())

# Calculate and display summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Calculate and display the average of a specific column (e.g., 'column_name')
column_name = 'your_column_name'
average_value = df[column_name].mean()
print(f"\nAverage {column_name}: {average_value}")

# Filter data based on a condition (e.g., filtering rows where a column value is greater than a threshold)
threshold = 50
filtered_data = df[df[column_name] > threshold]
print(f"\nData where {column_name} > {threshold}:")
print(filtered_data)

# Additional data manipulation and analysis
# Calculate the median of another column (e.g., 'another_column_name')
another_column_name = 'another_column_name'
median_value = df[another_column_name].median()
print(f"\nMedian {another_column_name}: {median_value}")

# Create a new column based on a transformation of existing data
# For example, let's create a new column that squares the values in 'another_column_name'
df['squared_values'] = df[another_column_name] ** 2

# Display the updated DataFrame
print("\nUpdated DataFrame with a new column:")
print(df.head())

# Save the manipulated data to a new CSV file
filtered_data.to_csv('filtered_data.csv', index=False)

# Save the entire DataFrame with the new column to a different CSV file
df.to_csv('manipulated_data.csv', index=False)