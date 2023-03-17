import re 
import pandas as pd
f=open('demo.txt','r',encoding='utf-8')

data=f.read()
print(type(data))

# pattern='\d{1,2}/\d{1,2}/\d{1,2},\s\d{1,2}:\d{2}\s-\s'
# data="Asit 1:78 AM kskj 56:45 AM njkjds 78:74 PM "
pattern='\d{1,2}/\d{1,2}/\d{1,2},\s\d{1,2}:\d{1,2}\s\w[A-M]\s-'
message=re.split(pattern,data)[1:]
dates=re.findall(pattern,data)
# print(message)
# for i in dates:
#     print(i,"")

df=pd.DataFrame({'user_message':message,'message_date':dates})
# print(df.head())
# df['message_date']=pd.to_datetime(df['message_date'],format='%m/%d/%Y, %H:%M - ')

print(df.shape)
df.head()

users = []
messages = []
for message in df['user_message']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:  # user name
            users.append(entry[1])
            messages.append(" ".join(entry[2:]))
        else:
            users.append('group_notification')
            messages.append(entry[0])

df['user'] = users
df['message'] = messages
df.drop(columns=['user_message'], inplace=True)
# print(df.head())

print(df['message_date'])
dates=[]
time=[]
dateTime=[]
for i in df['message_date']:
     temp=re.findall('\d{1,2}/\d{1,2}/\d{2}',i)
     temp2=re.findall('\s\d{1,2}:\d{1,2}\s',i)
     print(temp[0],temp2[0])
     dates.append(temp[0])
     time.append(temp2[0])
     dateTime.append(temp[0]+temp2[0])
df['dates']=dates
df['time']=time
df['date_time']=dateTime
df.drop(columns=['message_date'], inplace=True)

df['date']=pd.to_datetime(df['date_time'])
print(df.head())

df['only_date'] = df['date'].dt.date
df['year'] = df['date'].dt.year
df['month_num'] = df['date'].dt.month
df['month'] = df['date'].dt.month_name()
df['day'] = df['date'].dt.day
df['day_name'] = df['date'].dt.day_name()
df['hour'] = df['date'].dt.hour
df['minute'] = df['date'].dt.minute
print(df.head())