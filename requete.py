import mysql.connector

# Connexion à MySQL
conn = mysql.connector.connect(
    host="127.0.0.1",  
    user="root",      
    password="123456",  
)

cursor = conn.cursor()

# Création de la base de données
cursor.execute("CREATE DATABASE IF NOT EXISTS Budget_Buddy;")
cursor.execute("USE Budget_Buddy;")

# Création de la table Users
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        id_user INT AUTO_INCREMENT PRIMARY KEY,
        lastname VARCHAR(255) NOT NULL,
        firstname VARCHAR(255) NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL
    );
""")

# Tentative d'insertion d'un utilisateur
try:
    cursor.execute("""
        INSERT INTO Users (lastname, firstname, email, password) 
        VALUES (%s, %s, %s, %s)
    """, ('Doe', 'John', 'john.doe@gmail.com', '123456_Abb'))
    
    # Valider l'insertion
    conn.commit()
    print("Utilisateur inséré avec succès.")
except mysql.connector.Error as err:
    print(f"Erreur lors de l'insertion : {err}")
    conn.rollback()  # Annuler l'insertion si une erreur se produit

# Vérification de l'insertion en récupérant les données
cursor.execute("SELECT * FROM Users;")
users = cursor.fetchall()

# Afficher les utilisateurs récupérés
for user in users:
    print(user)

# Fermer la connexion
cursor.close()
conn.close()
