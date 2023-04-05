import pandas as pd





# Create a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Ed'],
        'Age': [25, 32, 18, 47, 22],
        'Country': ['USA', 'Canada', 'France', 'USA', 'Canada']}
df = pd.DataFrame(data)

# Access a column in the DataFrame
print(df['Name'])  
# Access a row in the DataFrame
print(df.loc[2])  

# Access a cell in the DataFrame
print(df.loc[2, 'Age']) 
# Index the DataFrame using a column label
print(df['Age'])  

# Slice the DataFrame using a range of rows
print(df[1:4])  

# Index the DataFrame using .loc[] and a row label
print(df.loc[2])  

# Slice the DataFrame using .loc[] and a range of row labels
print(df.loc[1:3, 'Age':'Country'])  

# Group the DataFrame by the 'Country' column and calculate the mean age
grouped = df.groupby('Country')
print(grouped['Age'].mean()) 

# Add a new column to the DataFrame
df['Gender'] = ['F', 'M', 'M', 'M', 'F']
print(df) 

# Remove a column from the DataFrame
df = df.drop(columns=['Country'])
print(df) 



# Create two DataFrames
data1 = {'Name': ['Arisha', 'Bilal', 'Charlie'],
         'Age': [25, 32, 18]}
df1 = pd.DataFrame(data1)

data2 = {'Name': ['Arisha', 'Bilal', 'Dave'],
         'Country': ['USA', 'Canada', 'USA']}
df2 = pd.DataFrame(data2)

# Merge the DataFrames on the 'Name' column
merged = pd.merge(df1, df2, on='Name')
print(merged)



# Create a Series from a list
data = [1, 2, 3, 4, 5]
s = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])

# Access an element in the Series
print(s[2]) 

# Index the Series using a label
print(s['c'])  

# Index the Series using a list of labels
print(s[['a', 'c', 'e']]) 

# Slice the Series using a range of labels
print(s['b':'d'])  

# Slice the Series using a range of integer positions
print(s[1:4])  








