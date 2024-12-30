-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: project
-- ------------------------------------------------------
-- Server version	8.0.39

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
-- Table structure for table `student_responses`
--

DROP TABLE IF EXISTS `student_responses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_responses` (
  `student_id` varchar(255) NOT NULL,
  `exam_id` int NOT NULL,
  `question_id` int NOT NULL,
  `question_text` text,
  `response` text,
  `marks_awarded` float(5,2) DEFAULT '0.00',
  `Maximum_marks` float(5,2) DEFAULT NULL,
  `is_checked` tinyint(1) DEFAULT '0',
  `checkers` varchar(255) DEFAULT NULL,
  `class_name` varchar(45) NOT NULL,
  `subject` varchar(45) NOT NULL,
  `correct_answer` varchar(255) DEFAULT 'null'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_responses`
--

LOCK TABLES `student_responses` WRITE;
/*!40000 ALTER TABLE `student_responses` DISABLE KEYS */;
INSERT INTO `student_responses` VALUES ('ID0001',1124,1,'What is the square root of 144?','12',2.00,2.00,1,'automated','10th','Mathematics','12'),('ID0001',1124,2,'Solve for x: 2x + 3 = 11.','4',2.00,2.00,1,'TE1234','10th','Mathematics','4'),('ID0001',1124,3,'What is the value of π (pi) approximately?','3.14',1.00,1.00,1,'automated','10th','Mathematics','3.14'),('ID0001',1124,4,'Simplify: (2 + 3) × 4.','20',2.00,2.00,1,'automated','10th','Mathematics','20'),('ID0001',1124,5,'Define a prime number.','wdwd',2.00,2.00,1,'TE1234','10th','Mathematics','A number with only two divisors: 1 and itself.'),('ID0001',1124,6,'What is the perimeter of a square with side 5 cm?','20 cm',1.00,1.00,1,'automated','10th','Mathematics','20 cm'),('ID0001',1124,7,'Evaluate: 5^3.','125',2.00,2.00,1,'automated','10th','Mathematics','125'),('ID0001',1124,8,'Explain the Pythagorean Theorem.','defef',2.00,5.00,1,'TE1234','10th','Mathematics',NULL),('ID0003',1124,9,'What is the square root of 144?','12',2.00,2.00,1,'automated','10th','Mathematics','12'),('ID0003',1124,10,'Solve for x: 2x + 3 = 11.','4',2.00,2.00,1,'TE1234','10th','Mathematics','4'),('ID0003',1124,11,'What is the value of π (pi) approximately?','3.14',1.00,1.00,1,'automated','10th','Mathematics','3.14'),('ID0003',1124,12,'Simplify: (2 + 3) × 4.','20',2.00,2.00,1,'automated','10th','Mathematics','20'),('ID0003',1124,13,'Define a prime number.','',0.00,2.00,1,'TE1234','10th','Mathematics','A number with only two divisors: 1 and itself.'),('ID0003',1124,14,'What is the perimeter of a square with side 5 cm?','25 cm',0.00,1.00,1,'automated','10th','Mathematics','20 cm'),('ID0003',1124,15,'Evaluate: 5^3.',NULL,0.00,2.00,1,'automated','10th','Mathematics','125'),('ID0003',1124,16,'Explain the Pythagorean Theorem.','',0.00,5.00,1,'TE1234','10th','Mathematics',NULL),('ID0004',1124,17,'What is the square root of 144?','12',2.00,2.00,1,'automated','10th','Mathematics','12'),('ID0004',1124,18,'Solve for x: 2x + 3 = 11.','4',2.00,2.00,1,'TE1234','10th','Mathematics','4'),('ID0004',1124,19,'What is the value of π (pi) approximately?','3.14',1.00,1.00,1,'automated','10th','Mathematics','3.14'),('ID0004',1124,20,'Simplify: (2 + 3) × 4.','20',2.00,2.00,1,'automated','10th','Mathematics','20'),('ID0004',1124,21,'Define a prime number.','idk',2.00,2.00,1,'TE1234','10th','Mathematics','A number with only two divisors: 1 and itself.'),('ID0004',1124,22,'What is the perimeter of a square with side 5 cm?',NULL,0.00,1.00,1,'automated','10th','Mathematics','20 cm'),('ID0004',1124,23,'Evaluate: 5^3.',NULL,0.00,2.00,1,'automated','10th','Mathematics','125'),('ID0004',1124,24,'Explain the Pythagorean Theorem.','',2.00,5.00,1,'TE1234','10th','Mathematics',NULL);
/*!40000 ALTER TABLE `student_responses` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-26 16:30:57
