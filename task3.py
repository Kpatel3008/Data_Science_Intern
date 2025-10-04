import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score

# Check if the dataset is available
if not os.path.exists('bank.csv'):
    print("File 'bank.csv' not found. Please download and place it in the folder.")
    exit()
# Load dataset (assumes headers and semicolon separator)
df = pd.read_csv('bank.csv', sep=';')
# Convert categorical variables to numeric
df = pd.get_dummies(df, drop_first=True)

# Identify target column
target_col = 'y_yes' if 'y_yes' in df.columns else 'y'

# Remove rows with missing target values
df = df.dropna(subset=[target_col])

# Features and target
X = df.drop(target_col, axis=1)
y = df[target_col]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build decision tree classifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Predict
y_pred = clf.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))