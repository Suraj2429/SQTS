import pandas as pd
import matplotlib.pyplot as plt

#Loading the dataset
data = pd.read_csv('data.csv')

#Displaying the dataset
print("Dataset\n", data)

#Basic Info
print("\nAverage Marks: ", data['marks'].mean())
print("Max Marks: ",data['marks'].max())
print("Min Marks: ",data['marks'].min())

#Plotting the data
plt.bar(data['name'], data['marks'])
plt.title('Marks of Students')
plt.xlabel('Name')
plt.ylabel('Marks')

plt.show()