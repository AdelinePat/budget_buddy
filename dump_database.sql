-- MySQL dump 10.13  Distrib 8.0.41, for Linux (x86_64)
--
-- Host: localhost    Database: budget_buddy
-- ------------------------------------------------------
-- Server version	8.0.41

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Bank_account`
--

DROP TABLE IF EXISTS `Bank_account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Bank_account` (
  `id_account` int NOT NULL AUTO_INCREMENT,
  `id_user` int NOT NULL,
  `account_type` varchar(100) NOT NULL,
  `account_name` varchar(100) DEFAULT NULL,
  `balance` decimal(13,2) NOT NULL,
  `min_balance` int unsigned NOT NULL,
  PRIMARY KEY (`id_account`),
  KEY `id_user` (`id_user`),
  CONSTRAINT `Bank_account_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `Users` (`id_user`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Bank_account`
--

LOCK TABLES `Bank_account` WRITE;
/*!40000 ALTER TABLE `Bank_account` DISABLE KEYS */;
INSERT INTO `Bank_account` VALUES (1,1,'Compte courant',NULL,328.00,0),(2,2,'Compte courant',NULL,1068.00,0),(3,3,'Compte courant',NULL,100.00,0),(4,1,'Compte courant',NULL,100.00,0),(5,2,'Compte courant',NULL,100.00,0),(6,3,'Compte courant',NULL,100.00,0);
/*!40000 ALTER TABLE `Bank_account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Transactions`
--

DROP TABLE IF EXISTS `Transactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Transactions` (
  `id_transaction` int NOT NULL AUTO_INCREMENT,
  `id_account_emitter` int DEFAULT NULL,
  `id_account_receiver` int DEFAULT NULL,
  `deal_description` varchar(100) NOT NULL,
  `amount` decimal(13,2) unsigned NOT NULL,
  `deal_date` date NOT NULL,
  `deal_type` varchar(100) NOT NULL,
  `frequency` int unsigned DEFAULT NULL,
  `category` varchar(100) DEFAULT NULL,
  `charges` decimal(13,2) DEFAULT NULL,
  PRIMARY KEY (`id_transaction`),
  KEY `id_account_emitter` (`id_account_emitter`),
  KEY `id_account_receiver` (`id_account_receiver`),
  CONSTRAINT `Transactions_ibfk_1` FOREIGN KEY (`id_account_emitter`) REFERENCES `Bank_account` (`id_account`),
  CONSTRAINT `Transactions_ibfk_2` FOREIGN KEY (`id_account_receiver`) REFERENCES `Bank_account` (`id_account`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Transactions`
--

LOCK TABLES `Transactions` WRITE;
/*!40000 ALTER TABLE `Transactions` DISABLE KEYS */;
INSERT INTO `Transactions` VALUES (1,1,NULL,'Retrait en prévision de mon achat de coke en cash',50.00,'2025-03-22','retrait',1,'dealing de drogue',NULL),(2,NULL,3,'Dépôt parce que je suis l\'emincence of shadow',10000.00,'2025-03-01','dépôt',1,'pot de vin',NULL),(3,2,1,'J\'ai de la peine pour les drogués mais je commence à être pauvre',20.00,'2025-03-18','transfert',1,'peuchère',NULL),(4,2,NULL,'Je donne de l\'argent à ma maman en cash pour qu\'elle ne soit pas imposable',50000.00,'2025-03-18','retrait',1,'dealing en famille',NULL),(5,1,3,'Eminence est mon nouveau dealing, je peux payer par transfert!',100.00,'2025-03-09','transfert',1,'dealing de drogue',NULL),(6,3,NULL,'Je m\'achète des trucs de luxe parce que ça fait classe',15000.00,'2025-03-14','retrait',1,'loisir',NULL),(7,NULL,2,'On m\'aime, je sais pas qui mais merci',2000.00,'2025-03-18','dépôt',1,'donation envers ma personne',NULL);
/*!40000 ALTER TABLE `Transactions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Users` (
  `id_user` int NOT NULL AUTO_INCREMENT,
  `lastname` varchar(255) NOT NULL,
  `firstname` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id_user`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` VALUES (1,'Doe','John','john.doe@gmail.com','123456_Abb'),(2,'Mangeot','Jolyne','jolyne.mangeot@laplateforme.io','123456_Abb'),(3,'Eminence','Shadow','eminenceofshadow@shadowgarden.com','123456_Abb');
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-21  7:51:34
