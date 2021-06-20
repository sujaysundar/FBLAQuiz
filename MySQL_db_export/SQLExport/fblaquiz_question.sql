-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: fblaquiz
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `question`
--

DROP TABLE IF EXISTS `question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `question` (
  `question_id` int NOT NULL AUTO_INCREMENT,
  `question_text` text NOT NULL,
  `question_type` varchar(50) NOT NULL,
  `question_score` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`question_id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question`
--

LOCK TABLES `question` WRITE;
/*!40000 ALTER TABLE `question` DISABLE KEYS */;
INSERT INTO `question` VALUES (1,'How many members does FBLA-PBL involve?','TEXT',20),(2,'How many chartered chapters are there in the USA?','TEXT',20),(3,'Which month is the FBLA-PBL Week held each year?','TEXT',20),(4,'What year was FBLA founded?','TEXT',20),(5,'Year an experimental chapter was chartered?','TEXT',20),(6,'Year the Phi Beta Lambda (PBL) was created?','TEXT',20),(7,'Year FBLA annual membership topped 200,000 for the first time?','TEXT',20),(8,'Year FBLA–Middle Level division is formed?','TEXT',20),(9,'Year FBLA-PBL National Center mortgage is retired?','TEXT',20),(10,'How many years did FBLA-PBL celebrate in 2016?','TEXT',20),(11,'Which state had the first FBLA chapter?','LIST',20),(12,'Where is the FBLA_PBL National Center located?','LIST',20),(13,'What are the official colors of FBLA-PBL?','LIST',20),(14,'Year FBLA-PBL granted status as a non-profit?','LIST',20),(15,'How much are FBLA national dues?','LIST',20),(16,'In debate, how many times can a member speak on a motion?','LIST',20),(17,'The Gold Seal award is named after?','LIST',20),(18,'The Parliamentary procedure event is named after?','LIST',20),(19,'How many administrative regions is FBLA-PBL divided into?','LIST',20),(20,'Three words on the FBLA and PBL emblems?','LIST',20),(21,'FBLA Professional Division includes?','MULTIPLE',20),(22,'The FBLA–Middle Level division includes grades?','MULTIPLE',20),(23,'Edward D. Miller retired as?','MULTIPLE',20),(24,'Jean Buckley retired as?','MULTIPLE',20),(25,'PBL includes the words?','MULTIPLE',20),(26,'2nd and 3rd FBLA state chapters to open?','MULTIPLE',20),(27,'The expanded form of NEAC includes?','MULTIPLE',20),(28,'Conferences organized by FBLA-PBL?','MULTIPLE',20),(29,'FBLA-PBL is organized at?','MULTIPLE',20),(30,'The National board of directors is comprised of?','MULTIPLE',20),(31,'www.fbla-pbl.org is FBLA\'s official national website?','BINARY',20),(32,'First FBLA local chapter was organized in Johnson city?','BINARY',20),(33,'FBLA Middle level membership open to students in grades 7-12?','BINARY',20),(34,'American Enterprise day is on Nov 15?','BINARY',20),(35,'Chapter President presides over and conducts meetings?','BINARY',20),(36,'Alexander T. Graham appointed president in 2017?','BINARY',20),(37,'Jean Buckley appointed president and CEO in 1997?','BINARY',20),(38,'Grand opening of the FBLA-PBL National Center was in 1995?','BINARY',20),(39,'Groundbreaking for the FBLA-PBL National Center was in 1990?','BINARY',20),(40,'Professional businesspersons aren\'t included in Professional Division?','BINARY',20),(41,'Professor Forkner developed the FBLA concept while at?','SINGLE',20),(42,'The name “Future Business Leaders of America” was selected in?','SINGLE',20),(43,'Experimental FBLA chapter was chartered at?','SINGLE',20),(44,'Who sponsors FBLA?','SINGLE',20),(45,'The second FBLA chapter was started in?','SINGLE',20),(46,'No. of FBLA chapters by the end of 1942?','SINGLE',20),(47,'In 1946, Headquarters office for FBLA was located at?','SINGLE',20),(48,'FBLA-PBL was granted 501(c)(3) status in?','SINGLE',20),(49,'FBLA-PBL Alumni Division was established in?','SINGLE',20),(50,'Foundation that helped purchase land for the National Center?','SINGLE',20);
/*!40000 ALTER TABLE `question` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-19 22:14:59
