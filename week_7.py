import pandas as pd

Names = ["Selin", "Emre", "Mert", "Bahar"]

records = pd.DataFrame(Names)
print(records)
print(type(records))



info = {"Names":["Selin", "Emre", "Mert", "Bahar"],
        "Id": [2343,5345,63123,42345],
        "Gpa": [3.5,3.3,4.0,2.5]}
info_records = pd.DataFrame(info)
print(info_records)

print(info_records["Names"][2])
print(info_records.loc[1]) # show exact row

print("-----------")

data_csv = pd.read_csv("employees_info.csv")
print(data_csv)
print(data_csv["employ_id"][4])


print("---------------------")
data_excel = pd.read_excel("INF100_raw.xlsx")
print(data_excel)
