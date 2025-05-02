import pandas as pd

df = pd.DataFrame({
    'A': [1,2,3,1,2,3],
    'B': [1,1,1,2,2,2],
    'C': [5,6,7,8,9,10]
})

pv_table = pd.pivot_table(df, index='A', columns='B', values='C', aggfunc='sum')
print(pv_table)

print(df.groupby(['A', 'B'])['C'].sum())