#Histogram for Age Distribution........

import matplotlib.pyplot as plt

ages = [23, 45, 22, 34, 45, 23, 36, 27, 29, 40, 41, 22, 23, 25, 30, 31, 35, 36, 37, 38]

plt.hist(ages, bins=5, color='skyblue', edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')
plt.show()


#Bar Chart for Gender Distribution.........

import matplotlib.pyplot as plt

# Example categorical data
genders = ['Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female']
gender_counts = {'Male': genders.count('Male'), 'Female': genders.count('Female')}

plt.bar(gender_counts.keys(), gender_counts.values(), color=['blue', 'pink'])
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Gender Distribution')
plt.show()