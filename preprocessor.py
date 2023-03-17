# import re
# import pandas as pd

# def preprocess(data):
#     # pattern = '\d{1,2}/\d{1,2}/\d{2},\b\d{1,2}:\d{2}\b-\s'

#     # pattern='\d{1,2}/\d{1,2}/\d{2}, '+'(1[012]|[1-9]):'+'[0-5][0-9](\\s)'+"?(?i)(am|pm)"
#     # pattern='\d{1,2}/\d{1,2}/\d{2},'
#     pattern='\d{1,2}/\d{1,2}/\d{1,2},\s\d{1,2}:\d{1,2}\s\w[A-Ma-m]\s-'

#     # pattern='\d{1,2}/\d{1,2}/\d{2}, \d{1,2}:\d{1,2} -'
#     # pattern='\d{1,2}/\d{1,2}/\d{2},\b\d{1,2}:\d{2}\b[A|P][M]\b-'

#     messages = re.split(pattern, data)[1:]
#     dates = re.findall(pattern, data)
#     print(messages,dates)

#     df = pd.DataFrame({'user_message': messages, 'message_date': dates})
#     # convert message_date type
#     df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%Y, %H:%M - ')

#     df.rename(columns={'message_date': 'date'}, inplace=True)

#     users = []
#     messages = []
#     for message in df['user_message']:
#         entry = re.split('([\w\W]+?):\s', message)
#         if entry[1:]:  # user name
#             users.append(entry[1])
#             messages.append(" ".join(entry[2:]))
#         else:
#             users.append('group_notification')
#             messages.append(entry[0])

#     df['user'] = users
#     df['message'] = messages
#     df.drop(columns=['user_message'], inplace=True)

#     df['only_date'] = df['date'].dt.date
#     df['year'] = df['date'].dt.year
#     df['month_num'] = df['date'].dt.month
#     df['month'] = df['date'].dt.month_name()
#     df['day'] = df['date'].dt.day
#     df['day_name'] = df['date'].dt.day_name()
#     df['hour'] = df['date'].dt.hour
#     df['minute'] = df['date'].dt.minute

#     period = []
#     for hour in df[['day_name', 'hour']]['hour']:
#         if hour == 23:
#             period.append(str(hour) + "-" + str('00'))
#         elif hour == 0:
#             period.append(str('00') + "-" + str(hour + 1))
#         else:
#             period.append(str(hour) + "-" + str(hour + 1))

#     df['period'] = period

#     return df



# data=''
# file=open('demo.txt','r',encoding='utf-8')
# data=file.read()

# print(preprocess(data))


# # str='3/3/23, 2:41 PM - +91 94054 77556: <Media omitted>'
# # # pattern='\d{1,2}/\d{1,2}/\d{2}, '+'(1[012]|[1-9]):'+'[0-5][0-9](\\s)'+"?(?i)(am|pm)"#'  #\s\d{1,2}:\d{2}\s-\s       \d{1,2}:\d{2}
# # # pattern='\d{1,2}:\d{2}'

# # # pattern='\d{1,2}/\d{1,2}/\d{2},\d{1,2}:\d{1,2} -'
# # pattern='\d{1,2}/\d{1,2}/\d{2},\W\d{1,2}:\d{2}\W'
# # # pattern=''

# # # pattern = '\d{1,2}/\d{1,2}/\d{2},'+'\b\d{1,2}:\d{2}\b-'
# # # pattern='\d{1,2}/\d{1,2}/\d{2},\b\d{1,2}:\d{2}\b[A|P][M]\b-'  # version 2
# # # pattern='(1[012]|[1-9]):'+'[0-5][0-9](\\s)'+"?(?i)(am|pm)";   #version 3
# # # day=re.split('-',str)
# # day=re.findall(pattern,data)
# # message=re.split(pattern,data)

# # new=[]
# # for i in day:
# #     new.append(i.encode('ascii','ignore'))
# # print(new,message)
# # str2='1/29/22, 1:32\u202f'
# # print(str2.encode('ascii','ignore'))



import re 
import pandas as pd
# f=open('chat.txt','r',encoding='utf-8')

# data=f.read()
# print(type(data))

def preprocess(data):
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

    # print(df.shape)
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

    # print(df['message_date'])
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
    # df['dates']=dates
    # df['time']=time
    df['date_time']=dateTime
    df.drop(columns=['message_date'], inplace=True)

    df['date']=pd.to_datetime(df['date_time'])
    # print(df.head())

    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute
    print(df.head())
    return df

# preprocessor(data)