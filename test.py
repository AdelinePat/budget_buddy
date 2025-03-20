from model.server import ServerDatabase

account = 'jolyne.mangeot@laplateforme.io'
current_session = 2

database = ServerDatabase()

my_database = database.database_connection()
account_id = 1

if my_database.is_connected():
    cursor = my_database.cursor()
#     cursor.execute("SELECT balance FROM bank_account "
#                     "JOIN Users u USING(id_user) "
#                     f"WHERE id_account = (SELECT MIN(id_account) FROM bank_account WHERE id_user = {current_session});")           
#     print(cursor.fetchone()[0])


# number = 'bn'
# new_value = float(number)
# print(new_value)

    balance_query = f"SELECT balance FROM Bank_account WHERE id_account = {account_id};"
    cursor.execute(balance_query)
    print(cursor.fetchone()[0])