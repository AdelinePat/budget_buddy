from model.server import ServerDatabase

account = 'jolyne.mangeot@laplateforme.io'
current_session = 2

database = ServerDatabase()

my_database = database.database_connection()

if my_database.is_connected():
    cursor = my_database.cursor()
    cursor.execute("SELECT balance FROM bank_account "
                    "JOIN Users u USING(id_user) "
                    f"WHERE id_account = (SELECT MIN(id_account) FROM bank_account WHERE id_user = {current_session});")           
    print(cursor.fetchone()[0])


    