import pandas as pd

employees={
    "name":["Aditya","Rohan","Priya","Neha","Aman"],
    "department":["Engineering","Engineering","HR","Finance","Engineering"],
    "salary":[100000,120000,80000,90000,110000],
    "company": [
    "Google",
    "Microsoft",
    "TCS",
    "JP Morgan",
    "Google"
    ]
}

df=pd.DataFrame(employees)

# print(df)
# print(df.shape)
# print(df.columns)
# print(df[["name","salary"]])

# print(df[df["salary"]> 100000])

# print(df.sort_values(
#     by="salary",
#     ascending=False
# ))

# df["salary"].mean()
# df["salary"].max()

# print(df.describe())



print(df.groupby("department")["salary"].mean())

print(df.groupby("company")["salary"].mean())
print(df.loc[df["salary"].idxmax()])

print(df[df["department"]=="Engineering"])

print(
    df.groupby("department")["salary"].agg(
    ["count", "mean", "min", "max"]
)
)