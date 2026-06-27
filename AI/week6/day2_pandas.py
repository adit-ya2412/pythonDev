import pandas as pd

# employees={
#     "name":["Aditya","Rohan","Priya","Neha","Aman"],
#     "department":["Engineering","Engineering","HR","Finance","Engineering"],
#     "salary":[100000,120000,80000,90000,110000],
#     "company": [
#     "Google",
#     "Microsoft",
#     "TCS",
#     "JP Morgan",
#     "Google"
#     ]
# }

# # df=pd.DataFrame(employees)

# # print(df)
# # print(df.shape)
# # print(df.columns)
# # print(df[["name","salary"]])

# # print(df[df["salary"]> 100000])

# # print(df.sort_values(
# #     by="salary",
# #     ascending=False
# # ))

# # df["salary"].mean()
# # df["salary"].max()

# # print(df.describe())



# # print(df.groupby("department")["salary"].mean())

# # print(df.groupby("company")["salary"].mean())
# # print(df.loc[df["salary"].idxmax()])

# # print(df[df["department"]=="Engineering"])

# # print(
# #     df.groupby("department")["salary"].agg(
# #     ["count", "mean", "min", "max"]
# # )
# # )

# # df=pd.read_csv("employees.csv")
# # print(df)

# # print(df.head())

# # print(df.head(2))

# # print(df.tail())

# # print(df.info())


# # #for missing values we use 
# # print(df.isnull())

# # print(df.isnull.sum())

# # print(df["salary"].fillna(0))
# # print(df["salary"].fillna(
# #     df["salary"].mean()
# # ))

# # print(df.dropna())

# employees1 = {
#     "name":["Aditya","Rohan","Priya","Neha"],
#     "salary":[100000,None,80000,None],
#     "department":["Engineering","Engineering",None,"Finance"]
# }

# df=pd.DataFrame(employees1)

# # print(df.info())

# # print(df.isnull())
# # print(df.isnull().sum())
# # df["salary"]=df["salary"].fillna(
# #     df["salary"].mean()
# # )

# # df["department"]=df["department"].fillna("Unknown")

# # print(df)

# # employees = pd.DataFrame({
# #     "employee_id":[1,2,3,4],
# #     "name":["Aditya","Rohan","Priya","Aman"]
# # })

# # departments = pd.DataFrame({
# #     "employee_id":[1,2,3],
# #     "department":["Engineering","Finance","HR"]
# # })

# # merged_df_inner=pd.merge(employees,departments,
# #          on="employee_id",
# #          how="inner")

# # merged_df_left=pd.merge(
# #     employees,
# #     departments,
# #     on="employee_id",
# #     how="right"
# # )

# # print(merged_df_inner)
# # print(merged_df_left)

# employees = pd.DataFrame({
#     "department": [
#         "Engineering",
#         "Engineering",
#         "HR",
#         "Finance",
#         "Engineering"
#     ],
#     "salary": [
#         100000,
#         120000,
#         80000,
#         90000,
#         110000
#     ]
# })

# result = (
#     employees.groupby("department")
#     .agg({
#         "salary":[
#             "count",
#             "mean",
#             "min",
#             "max",
#             "sum"
#         ]
#     })
# )

# employees["bonus"]=employees["salary"]*0.10

# employees["salary_in_lakhs"]= employees["salary"].apply(
#     lambda x:x/100000
# )
# df["name_upper"]=df["name"].str.upper()

# print(df)
# print(employees)
# print(result)
sales = pd.DataFrame({
    "date":[
        "2025-01-01",
        "2025-01-02",
        "2025-02-01",
        "2025-02-02"
    ],
    "department":[
        "Engineering",
        "Engineering",
        "HR",
        "Finance"
    ],
    "sales":[
        1000,
        1500,
        800,
        1200
    ]
})

sales["date"]=pd.to_datetime(sales["date"])

sales["year"]=sales["date"].dt.year
sales["month"]=sales["date"].dt.month
sales["day"]=sales["date"].dt.day

print(sales)
print(sales.pivot_table(
    values="sales",
    index="department",
    aggfunc="sum"
)
)