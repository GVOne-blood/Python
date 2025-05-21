import pandas as pd
l = [
    [1, 'Alice', 25, 'HR', 50000],
    [2, 'Bob', 30, 'IT', 60000],
    [3, 'Charlie', 35, 'IT', 70000],
    [4, 'David', 28, 'IT', 80000],
    [5, 'Eva', 39, 'HR', 90000]
]

columns = ['EmployeeID', 'Name', 'Age', 'Department', 'Salary']

df = pd.DataFrame(l, columns=columns)
print(df)

print('Finding Frank in dataframe...')
if 'Frank' in df['Name']:
    print('Frank is already exist in this DF')
else:
    df.loc[len(df)] = [6, 'Frank', 28, 'MAR', 65000]
    print(f'Add completed: \nNew dataframe : \n {df}')

print('Editing emp 3...')
df.loc[df['EmployeeID'] == 3, ['Department', 'Salary']] = ['HR', 75000]
print(f'Insert complete \nNew dataframe : \n {df}')

print('Deleting emp 4 from df...')
df = df.drop(df[df['EmployeeID'] == 4].index)
df = df.reset_index(drop=True)
print(f'Delete completed \nNew dataframe : \n {df}')
a = df.loc[df['Department'] == 'HR']
b = df.loc[df['Salary'] > 60000]
c = df.loc[(df['Age'] >= 30) & (df['Department'] == 'IT')]
print('Filter : ')
print(f'a - \n{a}')
print(f'b - \n{b}')
print(f'c - \n{c}')

avg = df.loc[df['Department'] == 'IT', ['Age']]
res = sum(avg['Age']) / len(avg['Age'])
print(f'Avg of age in IT department : {res}')
