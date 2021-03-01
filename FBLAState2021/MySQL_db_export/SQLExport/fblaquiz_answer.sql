CREATE DATABASE  IF NOT EXISTS `fblaquiz` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `fblaquiz`;
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
-- Table structure for table `answer`
--

DROP TABLE IF EXISTS `answer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `answer` (
  `answer_id` int NOT NULL AUTO_INCREMENT,
  `question_Id` int NOT NULL,
  `answer_text` text NOT NULL,
  `correct` char(1) DEFAULT NULL,
  PRIMARY KEY (`answer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=151 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `answer`
--

LOCK TABLES `answer` WRITE;
/*!40000 ALTER TABLE `answer` DISABLE KEYS */;
INSERT INTO `answer` VALUES (1,1,'250000','Y'),(2,2,'13000','Y'),(3,3,'February','Y'),(4,4,'1937','Y'),(5,5,'1942','Y'),(6,6,'1958','Y'),(7,7,'1987','Y'),(8,8,'1994','Y'),(9,9,'2001','Y'),(10,10,'75','Y'),(11,11,'New York','N'),(12,11,'Maine','N'),(13,11,'Iowa','Y'),(14,11,'Texas','N'),(15,12,'Atlanta, GA','N'),(16,12,'Reston, VA','Y'),(17,12,'Dallas, TX','N'),(18,12,'Richmond, VA','N'),(19,13,'Blue and gold','Y'),(20,13,'Blue and green','N'),(21,13,'Yellow and red','N'),(22,13,'Red, blue and white','N'),(23,14,'2002','N'),(24,14,'1949','N'),(25,14,'1969','Y'),(26,14,'1965','N'),(27,15,'$150','N'),(28,15,'$10','N'),(29,15,'$6','Y'),(30,15,'$8','N'),(31,16,'Twice','Y'),(32,16,'Three times','N'),(33,16,'Once','N'),(34,16,'Five times','N'),(35,17,'Hamden Forkner','N'),(36,17,'Hollis and Kitty Guy','Y'),(37,17,'Dorothy Travis','N'),(38,17,'Jean Buckley','N'),(39,18,'Blue and gold','N'),(40,18,'Lorraine Missling','N'),(41,18,'Hamden Forkner','N'),(42,18,'Dorothy L. Travis','Y'),(43,19,'5','Y'),(44,19,'7','N'),(45,19,'9','N'),(46,19,'3','N'),(47,20,'Service, Leadership, and Prosperity','N'),(48,20,'Service, Education, and Progress','Y'),(49,20,'Progress, Leadership, and Education','N'),(50,20,'Service, Education, and Leadership','N'),(51,21,'Engineers','N'),(52,21,'Alumni','Y'),(53,21,'Businesspersons','Y'),(54,21,'Doctors','N'),(55,22,'6','Y'),(56,22,'7','Y'),(57,22,'9','Y'),(58,22,'10','N'),(59,23,'COO','N'),(60,23,'CEO','Y'),(61,23,'CIO','N'),(62,23,'President','Y'),(63,24,'Vice President','N'),(64,24,'President','Y'),(65,24,'CEO','Y'),(66,24,'CMO','N'),(67,25,'Beta','Y'),(68,25,'Phi','Y'),(69,25,'Business','N'),(70,25,'Lambda','Y'),(71,26,'Indiana','Y'),(72,26,'Ohio','Y'),(73,26,'Texas','N'),(74,26,'California','N'),(75,27,'National','Y'),(76,27,'Education','Y'),(77,27,'Association','Y'),(78,27,'Center','Y'),(79,28,'NLC','Y'),(80,28,'IFL','Y'),(81,28,'NFLC','Y'),(82,28,'FBLA','N'),(83,29,'Local level','Y'),(84,29,'National level','Y'),(85,29,'District level','N'),(86,29,'State level','Y'),(87,30,'Local Teachers','Y'),(88,30,'State Educators','Y'),(89,30,'Business Leaders','Y'),(90,30,'Division Presidents','Y'),(91,31,'True','Y'),(92,31,'False','N'),(93,32,'True','Y'),(94,32,'False','N'),(95,33,'True','N'),(96,33,'False','Y'),(97,34,'True','Y'),(98,34,'False','N'),(99,35,'True','Y'),(100,35,'False','N'),(101,36,'True','N'),(102,36,'False','Y'),(103,37,'True','Y'),(104,37,'False','N'),(105,38,'True','N'),(106,38,'False','Y'),(107,39,'True','Y'),(108,39,'False','N'),(109,40,'True','N'),(110,40,'False','Y'),(111,41,'Yale','N'),(112,41,'Berkeley','N'),(113,41,'Columbia','Y'),(114,41,'Princeton','N'),(115,42,'1941','N'),(116,42,'1940','Y'),(117,42,'1943','N'),(118,42,'1944','N'),(119,43,'Science Hill High','Y'),(120,43,'Jericho High','N'),(121,43,'Syosset High','N'),(122,43,'Westbury High','N'),(123,44,'GE','N'),(124,44,'Hilton','N'),(125,44,'UBEA','Y'),(126,44,'UCLA','N'),(127,45,'New York City','N'),(128,45,'St. Albans','Y'),(129,45,'Chicago','N'),(130,45,'Walnut Creek','N'),(131,46,'41','N'),(132,46,'39','Y'),(133,46,'42','N'),(134,46,'37','N'),(135,47,'Boston','N'),(136,47,'Salt Lake City','N'),(137,47,'Washington DC','Y'),(138,47,'Orlando','N'),(139,48,'1951','N'),(140,48,'1967','N'),(141,48,'1969','Y'),(142,48,'1987','N'),(143,49,'1971','N'),(144,49,'1975','N'),(145,49,'1981','N'),(146,49,'1979','Y'),(147,50,'Ford','N'),(148,50,'Conrad N. Hilton','Y'),(149,50,'Reagan','N'),(150,50,'Rockefeller','N');
/*!40000 ALTER TABLE `answer` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-28 23:08:29
