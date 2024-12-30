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
-- Table structure for table `questions`
--

DROP TABLE IF EXISTS `questions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questions` (
  `id` int DEFAULT NULL,
  `exam_name` varchar(255) NOT NULL,
  `subject` varchar(255) NOT NULL,
  `class_name` varchar(255) NOT NULL,
  `question_text` text NOT NULL,
  `question_type` enum('mcq','short','long') NOT NULL,
  `options` text,
  `correct_answer` text,
  `marks` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questions`
--

LOCK TABLES `questions` WRITE;
/*!40000 ALTER TABLE `questions` DISABLE KEYS */;
INSERT INTO `questions` VALUES (1124,'Midterm Exam','Mathematics','10th','What is the square root of 144?','mcq','10|12|14|16','12',2),(1124,'Midterm Exam','Mathematics','10th','Solve for x: 2x + 3 = 11.','short',NULL,'4',2),(1124,'Midterm Exam','Mathematics','10th','What is the value of π (pi) approximately?','mcq','3.14|3.15|3.16|3.17','3.14',1),(1124,'Midterm Exam','Mathematics','10th','Simplify: (2 + 3) × 4.','mcq','20|14|18|22','20',2),(1124,'Midterm Exam','Mathematics','10th','Define a prime number.','short',NULL,'A number with only two divisors: 1 and itself.',2),(1124,'Midterm Exam','Mathematics','10th','What is the perimeter of a square with side 5 cm?','mcq','10 cm|15 cm|20 cm|25 cm','20 cm',1),(1124,'Midterm Exam','Mathematics','10th','Evaluate: 5^3.','mcq','15|25|125|75','125',2),(1124,'Midterm Exam','Mathematics','10th','Explain the Pythagorean Theorem.','long',NULL,NULL,5),(1125,'Final Exam','Mathematics','11th','What is the derivative of x^2?','mcq','2x|x^2|x|1','2x',3),(1125,'Final Exam','Mathematics','11th','What is the integral of 2x dx?','mcq','x^2 + C|2x^2|x|None','x^2 + C',3),(1125,'Final Exam','Mathematics','11th','Prove that the sum of angles in a triangle is 180°.','long',NULL,NULL,5),(1125,'Final Exam','Mathematics','11th','Explain the concept of limits in calculus.','long',NULL,NULL,5),(2124,'Midterm Exam','Physics','10th','What is the unit of force?','mcq','Newton|Joule|Pascal|Watt','Newton',2),(2124,'Midterm Exam','Physics','10th','What is the speed of light in a vacuum?','mcq','3 × 10^6 m/s|3 × 10^8 m/s|3 × 10^5 m/s|3 × 10^7 m/s','3 × 10^8 m/s',2),(2124,'Midterm Exam','Physics','10th','Define Newton’s second law of motion.','short',NULL,'F = ma',3),(2124,'Midterm Exam','Physics','10th','State the law of conservation of energy.','short',NULL,'Energy cannot be created or destroyed, only transformed.',2),(2124,'Midterm Exam','Physics','10th','Explain the working principle of a lever.','long',NULL,NULL,5),(2124,'Midterm Exam','Physics','10th','What is the SI unit of power?','mcq','Joule|Watt|Pascal|Newton','Watt',1),(2125,'Final Exam','Physics','12th','What is the formula for kinetic energy?','mcq','1/2 mv^2|mv^2|mv|1/2 mv','1/2 mv^2',3),(2125,'Final Exam','Physics','12th','Explain the concept of gravitational potential energy.','long',NULL,NULL,5),(2125,'Final Exam','Physics','12th','What is the difference between speed and velocity?','short',NULL,'Speed is scalar; velocity is vector.',2),(3124,'Midterm Exam','History','10th','Who was the first President of India?','mcq','Jawaharlal Nehru|Dr. Rajendra Prasad|Mahatma Gandhi|Sardar Patel','Dr. Rajendra Prasad',2),(3124,'Midterm Exam','History','10th','In which year did India gain independence?','mcq','1945|1947|1950|1952','1947',1),(3124,'Midterm Exam','History','10th','Explain the significance of the Quit India Movement.','long',NULL,NULL,5),(3124,'Midterm Exam','History','10th','Who is known as the Father of the Indian Constitution?','mcq','Mahatma Gandhi|B. R. Ambedkar|Jawaharlal Nehru|Sardar Patel','B. R. Ambedkar',2),(4125,'Final Exam','Geography','12th','What is the capital of Australia?','mcq','Sydney|Canberra|Melbourne|Perth','Canberra',1),(4125,'Final Exam','Geography','12th','Explain the process of the water cycle.','long',NULL,NULL,5),(4125,'Final Exam','Geography','12th','What is the longest river in the world?','short',NULL,'Nile',2),(4125,'Final Exam','Geography','12th','What are the different layers of the Earth?','short',NULL,'Crust, Mantle, Core',2),(5124,'Midterm Exam','Computer Science','10th','What does HTML stand for?','mcq','Hyper Text Markup Language|Hyper Text Markdown Language|High Text Markup Language|Hyperlink Text Markup Language','Hyper Text Markup Language',1),(5124,'Midterm Exam','Computer Science','10th','What is the output of 2 + 3 * 4?','mcq','20|14|18|None of the above','14',2),(5124,'Midterm Exam','Computer Science','11th','Explain the difference between RAM and ROM.','short',NULL,'RAM is volatile; ROM is non-volatile.',3),(5125,'Final Exam','Computer Science','12th','Write a program to add two numbers in Python.','long',NULL,NULL,10),(5125,'Final Exam','Computer Science','12th','Explain the concept of a “for loop” in programming.','short',NULL,'It is used to iterate over a sequence.',3),(2155,'Annual Exam','Science','10th','How is current proportional to current acc. to ohm\'s law?','mcq','directly|inversesely|square inversely|None Of the above','A',1),(2155,'Annual Exam','Science','10th','Expalin heating effect of current.','short',NULL,NULL,1),(2155,'Annual Exam','Science','10th','Write the process of photosynthesis','short',NULL,NULL,1),(2155,'Annual Exam','Science','10th','Explain all ways in which pregnancy can be prevented.','long',NULL,NULL,1),(2155,'Annual Exam','Science','10th','Explain The formation of esters.','long',NULL,NULL,1);
/*!40000 ALTER TABLE `questions` ENABLE KEYS */;
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
