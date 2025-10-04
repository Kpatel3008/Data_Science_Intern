import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('accidents.csv')  # Update with your file name

# Basic data cleaning
df = df.dropna(subset=['Road_Surface_Conditions', 'Weather_Conditions', 'Time', 'Latitude', 'Longitude'])

# Convert 'Time' to hour if needed
df['Hour'] = pd.to_datetime(df['Time'], errors='coerce').dt.hour

# Accident counts by road condition
plt.figure(figsize=(8,4))
sns.countplot(x='Road_Surface_Conditions', data=df)
plt.title('Accidents by Road Condition')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Accident counts by weather
plt.figure(figsize=(8,4))
sns.countplot(x='Weather_Conditions', data=df)
plt.title('Accidents by Weather')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Accident counts by hour of day
plt.figure(figsize=(8,4))
sns.countplot(x='Hour', data=df)
plt.title('Accidents by Hour of Day')
plt.tight_layout()
plt.show()

# Accident hotspots (scatter plot)
plt.figure(figsize=(8,6))
plt.scatter(df['Longitude'], df['Latitude'], alpha=0.3)
plt.title('Accident Hotspots')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.tight_layout()
plt.show()

print(df.columns)