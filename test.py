from model.server import ServerDatabase
from datetime import datetime, date

# account = 'jolyne.mangeot@laplateforme.io'
# current_session = 2

# database = ServerDatabase()

# my_database = database.database_connection()
# account_id = 1

# if my_database.is_connected():
#     cursor = my_database.cursor()
#     query = "SELECT deal_date FROM Transactions WHERE id_account_emitter = 2;"
#     cursor.execute(query)
#     dates = cursor.fetchall()

#     final_dates = []
#     for index, date in enumerate(dates):
#         print(index)
#         print(date)
#         final_dates.append(str(date[0]))
#         # date = str(date[0])
#         # date = date[0]    
#     print(final_dates)

#     datetime_str = '2024-06-09'

#     dateobject = datetime.strptime(datetime_str, '%y-%m-%d')
#     print(dateobject)


    # datetime_str = '09/19/22 13:55:26'

    # datetime_object = datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')

    # print(type(datetime_object))
    # print(datetime_object) 


    # emitter = 2
    # receiver = 1
    # description = "ceci est un test"
    # amount = 13
    # deal_date = "2025-05-07"
    # deal_type = "Transfert"
    # category = "Activités Illicites"
    # print(emitter, receiver, description, amount, deal_date, deal_type, category)


    # cursor.execute("INSERT INTO Transactions " +
    # "(id_account_emitter, id_account_receiver, " +
    # "deal_description, amount, " +
    # "deal_date, deal_type, " +
    # "category) " +
    # "VALUES " +
    # f"({emitter}, {receiver}, " +
    # f"{description}, {amount }, " +
    # f"{deal_date}, {deal_type}, " +
    # f"{category});")

date = "2025-03-03"
date_string = date.split("-")
year = int(date_string[0])
month = int(date_string[1])
day = int(date_string[2])

print(year)
print(month)
print(day)

current_time = datetime.now().strftime('%Y-%m-%d').split("-")
print(current_time)

if year < int(current_time[0]):
    print("yata")
else:
    if month < int(current_time[1]):
        print("yattaaa")
    else:
        if day < int(current_time[2]):
            print("YATTA")

# print(f"{current_time.year}-{current_time.month}-{current_time.day}")