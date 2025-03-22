from model.server import ServerDatabase
from datetime import datetime
from model.transactioninfo import TransactionInfo
import re
from model.customexception import TransactionException

test = TransactionInfo(1, 1, "Retrait", "2025-06-97", 1, None, "Ceci est une description", "Pot-de-vin", 42.45)
database = ServerDatabase()
user_id = 1

try:
    email = 'sachalarcher@gmail.com'
    email_regex = r"^[\w\.\+-]+@[a-zA-Z0-9\.\-]+\.[a-zA-Z]{2,}$"
    result = re.match(email_regex, email)
    if result == None:
        error_message = "Email invalide. Format attendu : exemple@domaine.com"
        raise TransactionException(error_message)
    final_result = result.group()
    print(final_result)
except TransactionException as e:
    print(e)

    

# database = database.database_connection()
# if database.is_connected():
#     cursor = database.cursor()
#     accounts_query = "SELECT id_account, account_type FROM Bank_account WHERE id_user =%s;"

#     cursor.execute(accounts_query, (user_id, ))
#     accounts = cursor.fetchall()
#     cursor.close()
# database.close()
# # print(accounts)

# account_str_list = []
# for account in accounts:
#     string = f"[{str(account[0])}] {account[1]}"
#     account_str_list.append(string)

# print(account_str_list)

# for account in account_str_list:
#     # print(account)
#     data = re.search("^(\[(\d)+\])", account)
#     account_id = re.search("(\d)+", data.group())
#     final_amount = account_id.group()
#     # print(account_id)
#     print(final_amount)



# account = 'jolyne.mangeot@laplateforme.io'
# current_session = 2


# account_id = 1

# if my_database.is_connected():
#     cursor = my_database.cursor()
#     query = "SELECT deal_date FROM Transactions WHERE id_account_emitter = 2;"
#     cursor.execute(query)
#     dates = cursor.fetchall()

#     final_dates = []
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

    # now = datetime.now() # current date and time

    # year = now.strftime("%y-%m-%d")
    # print("year:", year)


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