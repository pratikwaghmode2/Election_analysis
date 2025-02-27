import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the election data
file_path = "election_results_2024.csv"
df = pd.read_csv(file_path)

# Convert Margin to numeric (handling '-' and removing commas if any)
df['Margin'] = df['Margin'].astype(str).str.replace(',', '')
df['Margin'] = pd.to_numeric(df['Margin'], errors='coerce').fillna(0)

# Party-wise seat count
party_counts = df['Leading Party'].value_counts()
plt.figure(figsize=(12, 6))
sns.barplot(x=party_counts.index, y=party_counts.values, palette='viridis')
plt.xticks(rotation=90)
plt.xlabel("Political Party")
plt.ylabel("Number of Seats Won")
plt.title("Party-wise Seat Distribution")
plt.show()
plt.savefig("Party-wise seat count")

# Party-wise number of constituencies contested
contested_counts = df['Leading Party'].value_counts()
plt.figure(figsize=(12, 6))
sns.barplot(x=contested_counts.index, y=contested_counts.values, palette='coolwarm')
plt.xticks(rotation=90)
plt.xlabel("Political Party")
plt.ylabel("Number of Constituencies Contested")
plt.title("Party-wise Constituencies Contested")
plt.show()
plt.savefig("Party-wise number of constituencies contested")

# Top 10 Closest Fights
closest_fights = df.nsmallest(10, 'Margin')
print("Top 10 Closest Contests:")
print(closest_fights[['Constituency', 'Leading Candidate', 'Leading Party', 'Trailing Candidate', 'Trailing Party', 'Margin']])

# Top 10 Biggest Margins
biggest_margins = df.nlargest(10, 'Margin')
print("Top 10 Largest Victory Margins:")
print(biggest_margins[['Constituency', 'Leading Candidate', 'Leading Party', 'Margin']])

# Visualizing Margin Distribution
plt.figure(figsize=(10, 5))
sns.histplot(df['Margin'], bins=30, kde=True, color='blue')
plt.xlabel("Winning Margin")
plt.ylabel("Number of Constituencies")
plt.title("Distribution of Winning Margins")
plt.show()
plt.savefig("Distribution of Winning Margins")