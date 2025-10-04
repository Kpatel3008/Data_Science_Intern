import os
import pandas as pd
import matplotlib.pyplot as plt

# Check if the dataset is available
if not os.path.exists('titanic.csv'):
    print("File 'titanic.csv' not found. Please download and place it in the folder.")
else:
    # Load dataset (download 'titanic.csv' from Kaggle and place in your folder)
    df = pd.read_csv('titanic.csv')

    # Data Cleaning
    df = df.drop_duplicates()           
    df = df.dropna(subset=['Age'])     
    df['Sex'] = df['Sex'].fillna('Unknown')  

    # EDA: Summary statistics
    print(df.describe())
    print(df['Sex'].value_counts())

    # EDA: Survival rate by gender
    survival_by_gender = df.groupby('Sex')['Survived'].mean()
    print(survival_by_gender)

    # Plot: Age distribution
    plt.hist(df['Age'], bins=20, color='skyblue', edgecolor='black')
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.title('Age Distribution')
    plt.show()

    # Plot: Survival by gender
    plt.bar(survival_by_gender.index, survival_by_gender.values, color=['blue', 'pink'])
    plt.xlabel('Gender')
    plt.ylabel('Survival Rate')
    plt.title('Survival Rate by Gender')
    plt.show()