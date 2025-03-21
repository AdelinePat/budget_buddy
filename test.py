from model.server import ServerDatabase
from datetime import datetime

account = 'jolyne.mangeot@laplateforme.io'
current_session = 2

database = ServerDatabase()

my_database = database.database_connection()
account_id = 1

if my_database.is_connected():
    cursor = my_database.cursor()
    query = "SELECT deal_date FROM Transactions WHERE id_account_emitter = 2;"
    cursor.execute(query)
    dates = cursor.fetchall()

    final_dates = []
    # for index, date in enumerate(dates):
    #     print(index)
    #     print(date)
    #     final_dates.append(str(date[0]))
    #     # date = str(date[0])
    #     # date = date[0]    
    # print(final_dates)

    # datetime_str = '2024-06-09'

    # dateobject = datetime.strptime(datetime_str, '%y-%m-%d')
    # print(dateobject)

    now = datetime.now() # current date and time

    year = now.strftime("%y-%m-%d")
    print("year:", year)


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