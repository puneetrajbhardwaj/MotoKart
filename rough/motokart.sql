-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: localhost    Database: motokart
-- ------------------------------------------------------
-- Server version	8.0.25

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
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categories` (
  `categoryid` int NOT NULL AUTO_INCREMENT,
  `categoryname` varchar(45) NOT NULL,
  `cdescription` text,
  `categoryicon` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`categoryid`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES (1,'Cars','4 wheel LMVs','1d00f6d9-f7b4-404a-85a7-f73df17a392c.png'),(2,'Bikes','You will find various Subcategories of bikes inside Including sports bike & superbikes','60831a5d-e135-4acd-822b-a84707cf9bf9.jpg'),(12,'Trucks','Trucks','ee0aea67-c394-4548-8c0f-84a41bb5bc83.png'),(14,'three Wheel Car','cars','b6f5603a-5952-4e0b-b51c-a646782c7ec4.jpg');
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cities`
--

DROP TABLE IF EXISTS `cities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cities` (
  `stateid` int DEFAULT NULL,
  `cityid` int NOT NULL,
  `cityname` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`cityid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cities`
--

LOCK TABLES `cities` WRITE;
/*!40000 ALTER TABLE `cities` DISABLE KEYS */;
INSERT INTO `cities` VALUES (100,1,'Bhopal'),(100,2,'Gwalior'),(100,3,'Indore'),(200,4,'Agra'),(200,5,'Lucknow'),(200,6,'Kanpur'),(300,7,'Gurugram'),(300,8,'Rohtak'),(300,9,'Jind'),(400,10,'Ahemdabad'),(400,11,'Gandhinagar'),(500,12,'Goa'),(600,13,'Delhi');
/*!40000 ALTER TABLE `cities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `customerid` int NOT NULL AUTO_INCREMENT,
  `firstname` varchar(45) DEFAULT NULL,
  `lastname` varchar(45) DEFAULT NULL,
  `username` varchar(45) DEFAULT NULL,
  `customeremail` varchar(45) DEFAULT NULL,
  `customerphone` varchar(45) DEFAULT NULL,
  `gender` varchar(45) DEFAULT NULL,
  `stateid` int DEFAULT NULL,
  `cityid` int DEFAULT NULL,
  `address` varchar(45) DEFAULT NULL,
  `pincode` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`customerid`),
  UNIQUE KEY `username_UNIQUE` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES (1,'puneet','bhardwahj','puneet','puneetrajbhardwaj@gmail.com','8319937547','Male',100,2,'Agwalior hfhfjj','474020','Aabc@123'),(2,'Prakhar','Misra','prakhar','prakhar@gmail.com','1001001000','Male',600,13,'Agwalior hfhfj delhi','110033','Thanos@6969'),(3,'puneet','bhardwahj','lnknkmkk','prakhare@gmail.com','8909877890','Male',100,1,'Agwalior hfhfj','474020','Aabc@123'),(4,'puneett','bhardwahjj','lnknkmkkk','puneetrajjbhardwaj@gmail.com','7387282738','Male',200,4,'Agwalior hfhfj','110033','Aabc@123');
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employees` (
  `employeeid` int NOT NULL AUTO_INCREMENT,
  `employeename` varchar(45) DEFAULT NULL,
  `employeeemail` varchar(45) DEFAULT NULL,
  `employeephone` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`employeeid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES (1,'Puneet','abc@gmail.com','9876543210','Aabc@123'),(2,'Prakhar','prakharmisra975@gmail.com','1001001000','Prime@971');
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `categoryid` int DEFAULT NULL,
  `subcategoryid` int DEFAULT NULL,
  `productid` int NOT NULL AUTO_INCREMENT,
  `productname` varchar(45) DEFAULT NULL,
  `company` varchar(45) DEFAULT NULL,
  `price` varchar(45) DEFAULT NULL,
  `offer` varchar(45) DEFAULT NULL,
  `engine` varchar(45) DEFAULT NULL,
  `power` varchar(45) DEFAULT NULL,
  `displacement` varchar(45) DEFAULT NULL,
  `speedtransmission` varchar(45) DEFAULT NULL,
  `suspension` varchar(45) DEFAULT NULL,
  `weight` varchar(45) DEFAULT NULL,
  `topspeed` varchar(45) DEFAULT NULL,
  `shortdescription` text,
  `moredescription` text,
  `producticon` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`productid`),
  UNIQUE KEY `productname_UNIQUE` (`productname`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,1,10,'718 Cayman (grey)','porsche','3000000','3% Discount + insurance','2.0 L 4-cylinder, 4.0 L 6-cylinder','221 to 309 kW','10','Auto','14','1,495','150','Porsche 718 Cayman ','','c314ce1e-7c9c-40f7-93ff-8b7652073a4a.png'),(1,1,12,'NSX','Honda','76,00,000','3% Discount + insurance','V10','220 HP','10','9-speed dual-clutch automatic','14','1,495','250','The Honda NSX, marketed in North America as the Acura NSX, is a two-seat, mid-engine coupe sports car manufactured by Honda','','1baa569d-2200-439d-800e-2122793c1de0.png'),(1,1,15,'Nemesis RR','Trion','16,000,000','','552 cubic inch quad-cam V8.','2000 hp','10','8-speed sequential transmission','14','1500','250','The Trion Nemesis RR is a concept vehicle from Trion Supercars. The company is set to reveal a production version in 2021. Trion expects to start manufacturing process of the Nemesis by January 2021 and for the first vehicle to hit the streets in March 2021.','','b6a14248-12f0-43c3-929e-55a41af98fa6.png'),(1,2,16,'SP48 Unica','Ferrari','1,50,00,000','0% discount + insurance','3.9-liter twin-turbocharged V-8','710 hp',' 568 lb-ft of torque','7-speed dual-clutch automatic','N/a','2500','380','Ferrari SP48 Unica','','987791b3-955b-4adc-a872-0754fb7e8afc.png');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `states`
--

DROP TABLE IF EXISTS `states`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `states` (
  `stateid` int NOT NULL,
  `statename` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`stateid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `states`
--

LOCK TABLES `states` WRITE;
/*!40000 ALTER TABLE `states` DISABLE KEYS */;
INSERT INTO `states` VALUES (100,'Madhya Pradesh'),(200,'Uttar Pradesh'),(300,'Haryana'),(400,'Gujrat'),(500,'Goa'),(600,'Delhi');
/*!40000 ALTER TABLE `states` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subcategories`
--

DROP TABLE IF EXISTS `subcategories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `subcategories` (
  `categoryid` int DEFAULT NULL,
  `subcategoryid` int NOT NULL AUTO_INCREMENT,
  `subcategoryname` varchar(45) DEFAULT NULL,
  `scdescription` text,
  `subcategoryicon` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`subcategoryid`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subcategories`
--

LOCK TABLES `subcategories` WRITE;
/*!40000 ALTER TABLE `subcategories` DISABLE KEYS */;
INSERT INTO `subcategories` VALUES (1,1,'Sports Cars','View Sports Cars here','017fb4cb-e01f-4d6f-a9c7-7385910cfa1c.png'),(1,2,'Super cars','you will find some of the best supercars inside','aa988a8b-2217-4ceb-bd81-6317a8f5920b.png'),(1,3,'Vintage','You will find some of the best classic cars inside','225e5f56-c9cd-43f2-a055-76040495dccf.png'),(1,5,'Sedan','You will find some of the best Porsche inside','17f055cb-5bdf-4a43-819e-fb6f00b4dfcf.png'),(2,7,'sports bike','hey ! it is the fastest bike.................','a157f73f-a072-4a17-8247-abf5a6cbc713.png'),(7,8,'Regular','na','941b5259-ae0f-4490-9e64-8256626fe799.png'),(1,9,'SUV','SUVS','9fe42bd8-d8fc-4da4-a0d4-c2eebbdc4d8f.png'),(7,11,'heavy','na','d1ca7018-4071-4917-87e2-b21cea7bbe6c.jpg'),(2,14,'classic','na','c6f380c6-78a4-47c6-8fd2-0a9e492e4065.jpg');
/*!40000 ALTER TABLE `subcategories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wishlist`
--

DROP TABLE IF EXISTS `wishlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wishlist` (
  `customerid` int NOT NULL,
  `productid` int NOT NULL,
  PRIMARY KEY (`customerid`,`productid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wishlist`
--

LOCK TABLES `wishlist` WRITE;
/*!40000 ALTER TABLE `wishlist` DISABLE KEYS */;
/*!40000 ALTER TABLE `wishlist` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-08 16:47:21
