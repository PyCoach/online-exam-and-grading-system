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
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students` (
  `student_id` varchar(50) NOT NULL,
  `name` varchar(100) NOT NULL,
  `class_name` varchar(255) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `dob` date DEFAULT NULL,
  `address` text,
  `phone_no` char(12) DEFAULT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES ('ST0001','Arjun Sharma','10','arjun.sharma@gmail.com','2007-05-12','45, Laxmi Bazar, Haldwani','9876543210'),('ST0002','Priya Reddy','12','priya.reddy@yahoo.com','2005-10-22','12, Kathgodam, Haldwani','9845123456'),('ST0003','Rahul Patil','11','rahul.patil@outlook.com','2006-08-19','23, Kusumkhera, Haldwani','9822011122'),('ST0004','Ananya Iyer','9','ananya.iyer@gmail.com','2008-02-05','67, Rampur Road, Haldwani','9988776655'),('ST0005','Kunal Mehta','12','kunal.mehta@mail.com','2005-12-15','56, Tikonia, Haldwani','9812345678'),('ST0006','Sneha Gupta','10','sneha.gupta@gmail.com','2007-03-11','78, Subhash Nagar, Haldwani','9001234567'),('ST0007','Vikram Singh','11','vikram.singh@yahoo.com','2006-06-15','21, Mukhani, Haldwani','9811223344'),('ST0008','Neha Verma','9','neha.verma@mail.com','2008-08-23','33, Kamluaganja, Haldwani','9876547890'),('ST0009','Aakash Nair','12','aakash.nair@outlook.com','2005-07-09','77, Nawabi Road, Haldwani','9090909090'),('ST0010','Isha Joshi','10','isha.joshi@gmail.com','2007-01-01','89, Gaulapar, Haldwani','9911223344'),('ST0011','Devansh Rao','11','devansh.rao@yahoo.com','2006-04-18','90, Nainital Road, Haldwani','9871234560'),('ST0012','Riya Saxena','12','riya.saxena@mail.com','2005-09-05','11, Rajpura, Haldwani','9008765432'),('ST0013','Tarun Kumar','9','tarun.kumar@gmail.com','2008-12-30','25, HMT, Haldwani','9823421222'),('ST0014','Divya Pillai','10','divya.pillai@outlook.com','2007-02-22','46, Indira Nagar, Haldwani','9911122233'),('ST0015','Sarthak Kapoor','12','sarthak.kapoor@mail.com','2005-06-08','56, Arya Nagar, Haldwani','9933221100'),('ST0016','Anjali Rajput','11','anjali.rajput@gmail.com','2006-07-15','99, Keshav Vihar, Haldwani','9444443333'),('ST0017','Yash Thakur','10','yash.thakur@outlook.com','2007-03-10','12, Shastri Nagar, Haldwani','9765543322'),('ST0018','Shruti Banerjee','12','shruti.banerjee@gmail.com','2005-08-11','23, Bhawanipur, Haldwani','8899121212'),('ST0019','Kabir Dutta','11','kabir.dutta@yahoo.com','2006-09-19','45, Kaladhungi Road, Haldwani','9811112233'),('ST0020','Pooja Rathi','9','pooja.rathi@mail.com','2008-04-01','56, Dev Nagar, Haldwani','9098123456'),('ST0021','Aryan Malhotra','12','aryan.malhotra@gmail.com','2005-03-14','67, Durga Colony, Haldwani','9872233344'),('ST0022','Ishaan Menon','10','ishaan.menon@outlook.com','2007-11-25','78, Bhotia Parao, Haldwani','9445512233'),('ST0023','Meera Desai','11','meera.desai@yahoo.com','2006-02-28','89, Budh Bazar, Haldwani','9911225555'),('ST0024','Akshay Khanna','9','akshay.khanna@mail.com','2008-10-10','90, Jawahar Nagar, Haldwani','9988771234'),('ST0025','Tanya Sinha','12','tanya.sinha@gmail.com','2005-04-20','23, Banbhoolpura, Haldwani','9812348800'),('ST0026','Vivek Jain','10','vivek.jain@yahoo.com','2007-06-13','44, Kisan Market, Haldwani','8822113344'),('ST0027','Kriti Goel','11','kriti.goel@mail.com','2006-07-17','55, Bareilly Road, Haldwani','9879982211'),('ST0028','Ankur Chatterjee','12','ankur.chat@gmail.com','2005-05-08','66, Bhujia Ghat, Haldwani','9711223344'),('ST0029','Jiya Thomas','9','jiya.thomas@outlook.com','2008-09-12','77, Bhuna, Haldwani','9445566778'),('ST0030','Aditya Shetty','10','aditya.shetty@gmail.com','2007-10-07','88, Vinayak Colony, Haldwani','9876651234');
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
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
