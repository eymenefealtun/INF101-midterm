def show(givenList):
    givenList = list(givenList)
    myString = ""
    for i in range(len(givenList)):
        myString += str(givenList[i])
        myString += " "
    print(myString)



#Q2) Store the file employees_info.csv at the same directory where your code resides
import pandas as ps
poor={}
df=ps.read_csv('employees_info.csv')
count=0
print(len(df))
print(len(df["salary"]))
for i in range(len(df['salary'])):
       if df['salary'][i]<3000:
              count+=1
              poor[count]=f"{df.loc[i]['first_name']} {df.loc[i]['last_name']}"
print(poor)