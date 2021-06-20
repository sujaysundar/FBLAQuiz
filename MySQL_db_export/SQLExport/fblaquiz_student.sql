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
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `student_id` int NOT NULL,
  `student_name` varchar(255) NOT NULL,
  `student_grade` int NOT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (2343,'Philip',10),(3456,'Samuel',10),(10010,'John Smith',10),(10101,'Jack',11),(20202,'Carly',11),(20203,'Philip',11),(22222,'Sundar',11),(22223,'John',11),(23232,'George',11),(23400,'James Smith',10),(23444,'Sanjay',11),(23532,'Sanjay',11),(23593,'Sujay Sundar',10),(23594,'Jasmine Samadi',12),(23595,'Allison Lee',12),(23596,'Sujay Alluri',12),(23597,'Bryant Chen',11),(23598,'Pranav Nair',12),(23599,'Pranav Denudukuri',12),(23600,'Vishnu Nair',10),(23601,'Anshul Vemuri',12),(23602,'Juliann Lo',12),(23603,'Ty Josephy',12),(23604,'Tiffany Chen',12),(23605,'Jason Suh',12),(23606,'Aaron Marasia',12),(23607,'Jake Kupferman',12),(23608,'Janice Rateshwar',12),(23609,'Elina Ng',10),(23610,'Elaine Zhao',10),(23611,'Kevin Zhu',10),(23612,'Ada Chen',10),(23613,'Ryan Berger',10),(23614,'Jeff Bao',10),(23615,'Sholly Babalola',11),(23616,'Rishab Bhatia',10),(23617,'Sylas Chacko',11),(23618,'David Salmonson',10),(23619,'Davesh Valagolam',10),(23620,'Matt Laddy',10),(23621,'Selena Pan',10),(23622,'Zara Qisilbash',10),(23623,'Elisa Ng',10),(23624,'Enson Pan',10),(23625,'Josh Dong',10),(23626,'Blake Mayourian',10),(23627,'Jeremy Rothman',12),(23628,'Michael Pecorara',11),(23629,'Emma Schwarzwald',10),(23630,'Omari Motta',10),(23631,'Gloria Cheng',10),(23632,'Laura Zhou',9),(23633,'Min Yoon',9),(23634,'Josh Abbas',9),(23635,'Alli Pearlman',9),(23636,'Jasmine Chen',9),(23637,'Maddy Lansberg',10),(23638,'Andrew Chodes',10),(23639,'Lily Glickman',11),(23640,'Max Volynets',12),(23641,'Sophia Chen',12),(23642,'Judy Zhou',12),(23643,'Andrew Lennenberg',10),(23644,'Harrison Berger',11),(24242,'Jack',10),(24442,'Johnny',10),(24542,'John',11),(24562,'Phil',11),(25252,'Saila',9),(25552,'John Sundar',11),(29292,'Sujay',10),(30033,'John',9),(30303,'Fiona',10),(32323,'Jacques',11),(34343,'Sujay',10),(43587,'Zack',11),(54343,'Sanjay',10),(90909,'Dan',12),(134567,'Jay',12),(233324,'Sunjay',11),(234323,'Sujay',10),(234543,'Sahana',12),(432345,'Sam',10),(435645,'Jessica',10),(1453267,'John ',11),(2343434,'Sanjay',10),(4565434,'Jack',10),(23434567,'Samantha',12),(23435675,'Sujay',11),(34564321,'Sam',9),(232324534,'Sujay',11),(234543234,'John',10);
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-19 22:15:00
