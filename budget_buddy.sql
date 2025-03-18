-- Active: 1741679024806@@127.0.0.1@3306@budget_buddy
CREATE DATABASE IF NOT EXISTS Budget_Buddy;
USE Budget_Buddy;
DROP TABLE IF EXISTS Users;
CREATE TABLE Users (
    id_user INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    lastname VARCHAR(255) NOT NULL,
    firstname VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
)

DROP TABLE IF EXISTS Bank_account;
CREATE TABLE Bank_account (
    id_account INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    id_user INT NOT NULL,
    account_type VARCHAR(100) NOT NULL,
    account_name VARCHAR(100) NULL,
    balance INT NOT NULL,
    min_balance INT UNSIGNED NOT NULL,
    FOREIGN KEY (id_user) REFERENCES Users(id_user)
)

DROP TABLE IF EXISTS Transactions;
CREATE TABLE Transactions (
    id_transaction INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    id_account_emitter INT NULL,
    id_account_receiver INT NULL,
    deal_description VARCHAR(100) NOT NULL,
    amount INT UNSIGNED NOT NULL,
    deal_date DATE NOT NULL,
    deal_type VARCHAR(100) NOT NULL,
    frequency INT UNSIGNED NOT NULL,
    category VARCHAR(100) NOT NULL,
    charges INT NULL,
    FOREIGN KEY (id_account_emitter) REFERENCES Bank_account(id_account),
    FOREIGN KEY (id_account_receiver) REFERENCES Bank_account(id_account)
)

INSERT INTO
    Users(lastname, firstname, email, password)
VALUES
    ('Doe', 'John', 'john.doe@gmail.com', '123456_Abb'),
    ('Mangeot', 'Jolyne', 'jolyne.mangeot@laplateforme.io', '123456_Abb'),
    ('Eminence', 'Shadow', 'eminenceofshadow@shadowgarden.com', '123456_Abb');

INSERT INTO
    Bank_account (id_user, account_type, balance, min_balance)
VALUES
    ((SELECT id_user FROM Users WHERE id_user = (SELECT MIN(id_user) FROM Users)),
    'Compte courant',
    100,
    0),
    ((SELECT id_user FROM Users WHERE id_user = (SELECT MIN(id_user) FROM Users))+1,
    'Compte courant',
    100,
    0),
    ((SELECT id_user FROM Users WHERE id_user = (SELECT MIN(id_user) FROM Users))+2,
    'Compte courant',
    100,
    0);

-- id_transaction INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
--     id_account_emitter INT NULL,
--     id_account_receiver INT NULL,
--     deal_description VARCHAR(100) NOT NULL,
--     amount INT UNSIGNED NOT NULL,
--     deal_date DATE NOT NULL,
--     deal_type VARCHAR(100) NOT NULL,
--     frequency INT UNSIGNED NOT NULL,
--     category VARCHAR(100) NOT NULL,
--     charges INT NULL,
INSERT INTO Transactions(
    id_account_emitter,
    id_account_receiver,
    deal_description,
    amount,
    deal_date,
    deal_type,
    frequency,
    category,
    charges)
VALUES
    (1, NULL, 'Retrait en prévision de mon achat de coke en cash', 50, '2025-03-22', 'retrait', 1, 'dealing de drogue', NULL),
    (NULL, 3, 'Dépôt parce que je suis l\'emincence of shadow', 10000, '2025-03-01', 'dépôt', 1, 'pot de vin', NULL),
    (2, 1, 'J\'ai de la peine pour les drogués mais je commence à être pauvre', 20, '2025-03-18', 'transfert', 1, 'peuchère', NULL),
    (2, NULL, 'Je donne de l\'argent à ma maman en cash pour qu\'elle ne soit pas imposable', 50000, '2025-03-18', 'retrait', 1, 'dealing en famille', NULL);


INSERT INTO Transactions(
    id_account_emitter,
    id_account_receiver,
    deal_description,
    amount,
    deal_date,
    deal_type,
    frequency,
    category,
    charges)
VALUES
    (1, 3, 'Eminence est mon nouveau dealing, je peux payer par transfert!', 100, '2025-03-09', 'transfert', 1, 'dealing de drogue', NULL),
    (3, NULL, 'Je m\'achète des trucs de luxe parce que ça fait classe', 15000, '2025-03-14', 'retrait', 1, 'loisir', NULL),
    (NULL, 2, 'On m\'aime, je sais pas qui mais merci', 2000, '2025-03-18', 'dépôt', 1, 'donation envers ma personne', NULL);
TABLE Users;
TABLE Bank_account;

TABLE Transactions;
DESCRIBE users;

-- DROP DATABASE Budget_Buddy;
