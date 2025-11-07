import pandas as pd
print(pd.__version__)

# ques 1

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
print(df)

#ques 2

S1 = pd.Series([100, 200, 300, 400, 500])
print(S1)
print(S1[1])  
print(S1[3]) 
S2 = pd.Series([10, 20, 30, 40, 50])
result = S1 + S2
print(result)

#ques 3
print(df[['Name', 'City']])
df['Salary'] = [50000, 60000, 70000]
print("Updated DataFrame")
print(df)
average_age = df['Age'].mean()
total_salary = df['Salary'].sum()

print(f"Average Age: {average_age}")
print(f"Total Salary: {total_salary}")

# ques 4
filtered_df = df[df['Age'] > 28]
print("filtered dataset",filtered_df)

df_indexed = df.set_index('Name')
print("\n4.2 DataFrame with 'Name' as index:")
print(df_indexed)

df_reset = df_indexed.reset_index()
print("\nDataFrame after resetting index:")
print(df_reset)

# ques 5

df = pd.read_csv('employees.csv')

print("5.1 Contents of employees.csv:")
print(df)

filtered_df = df[df['Salary'] > 55000]
print("\n5.2 Filtered DataFrame (Salary > 55000):")
print(filtered_df[['Name', 'Department']])

# ques 6
avg_salary = df.groupby('Department')['Salary'].mean()

print("\n6.1 Average Salary by Department:")
print(avg_salary)
salary_stats = df.groupby('Department')['Salary'].agg(['min', 'max'])

print("\n6.2 Minimum and Maximum Salary by Department:")
print(salary_stats)

# ques 7
df1 = pd.DataFrame({
    'Name': ['John', 'Jane', 'Emily'],
    'Department': ['Sales', 'Marketing', 'HR']
})

df2 = pd.DataFrame({
    'Name': ['John', 'Jane', 'Emily'],
    'Experience (Years)': [5, 7, 3]
})

merged_df = pd.merge(df1, df2, on='Name')

print("\n7.1 Merged DataFrame:")
print(merged_df)

#ques 8

sorted_df = merged_df.sort_values(by='Experience (Years)', ascending=False)

print("8.1 DataFrame sorted by 'Experience (Years)' (descending):")
print(sorted_df)