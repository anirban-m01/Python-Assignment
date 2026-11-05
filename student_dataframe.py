import pandas as pd

data = {
"roll": [1,2, 3,4, 5],
"name":["Ani", "Mehu","Mehuli", "Manta","Anirban"],
"dept": ["ESE","IT", None,"ESE", None],
"marks":[90, None,80, 85,95]
}
df = pd.DataFrame(data)
print(df)

# columns with null values
print(df.isnull().sum())

# filling mehuli's null dept with cse
df.loc[df['name']=='Mehuli', 'dept']= df.loc[df['name'] == 'Mehuli', 'dept'].fillna("CSE")

# deleting anirban's null row
df= df.dropna(subset=['dept'])

# updating manta's dept
df.loc[df['name'] =='Manta', 'dept']= "NIST"

print(df)