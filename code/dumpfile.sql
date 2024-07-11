-- MySQL dump 10.13  Distrib 8.0.35, for Linux (x86_64)
--
-- Host: localhost    Database: Election_Database
-- ------------------------------------------------------
-- Server version	8.0.35-0ubuntu0.23.04.1

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
-- Table structure for table `Ballots`
--

DROP TABLE IF EXISTS `Ballots`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Ballots` (
  `Ballot_ID` char(4) NOT NULL,
  `Election_event` varchar(255) NOT NULL,
  `Station_ID` char(4) NOT NULL,
  PRIMARY KEY (`Ballot_ID`),
  KEY `Station_ID` (`Station_ID`),
  CONSTRAINT `Ballots_ibfk_1` FOREIGN KEY (`Station_ID`) REFERENCES `Polling_Stations` (`Station_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Ballots`
--

LOCK TABLES `Ballots` WRITE;
/*!40000 ALTER TABLE `Ballots` DISABLE KEYS */;
INSERT INTO `Ballots` VALUES ('1221','TS Assembly Election 2023','1196'),('1231','TS Assembly Election 2023','1098'),('1234','TS Assembly Election 2023','1107'),('1252','TS Assembly Election 2023','1107'),('1421','TS Assembly Election 2023','1196');
/*!40000 ALTER TABLE `Ballots` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Campaign_finance`
--

DROP TABLE IF EXISTS `Campaign_finance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Campaign_finance` (
  `Transaction_ID` char(10) NOT NULL,
  `Amount` int DEFAULT NULL,
  `Candidate_ID` char(7) NOT NULL,
  `Date_campaign` date NOT NULL,
  PRIMARY KEY (`Transaction_ID`),
  KEY `Candidate_ID` (`Candidate_ID`),
  CONSTRAINT `Campaign_finance_ibfk_1` FOREIGN KEY (`Candidate_ID`) REFERENCES `Candidates` (`Candidate_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Campaign_finance`
--

LOCK TABLES `Campaign_finance` WRITE;
/*!40000 ALTER TABLE `Campaign_finance` DISABLE KEYS */;
INSERT INTO `Campaign_finance` VALUES ('3771772772',14369,'1252323','2023-01-31'),('3771772773',35600,'1252324','2023-01-31'),('3771772774',90000,'1252327','2023-01-31'),('3771772775',132867,'1252325','2023-01-31'),('3771772776',696969,'1252328','2023-01-31'),('3771772777',696969,'1252328','2023-01-31');
/*!40000 ALTER TABLE `Campaign_finance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Candidates`
--

DROP TABLE IF EXISTS `Candidates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Candidates` (
  `Candidate_ID` char(7) NOT NULL,
  `Fname` varchar(255) NOT NULL,
  `Lname` varchar(255) NOT NULL,
  `Phone_Number` char(10) NOT NULL,
  `Email_ID` varchar(255) DEFAULT NULL,
  `Party_Affiliation` varchar(255) NOT NULL,
  `Candidate_exp` int NOT NULL,
  `Event_ID` char(12) NOT NULL,
  PRIMARY KEY (`Candidate_ID`),
  KEY `Event_ID` (`Event_ID`),
  CONSTRAINT `Candidates_ibfk_1` FOREIGN KEY (`Event_ID`) REFERENCES `Election_events` (`Event_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Candidates`
--

LOCK TABLES `Candidates` WRITE;
/*!40000 ALTER TABLE `Candidates` DISABLE KEYS */;
INSERT INTO `Candidates` VALUES ('1252323','Vivek','Kavuri','7980099505','kavuri.hryday@tscd.in','BJP',14369,'202311300129'),('1252324','Kriti','Madumadukala','8196365369','kriti.m@tscd.in','BRS',35600,'202311300129'),('1252325','Chandana','Yalamanchili','8169367369','chandana.y@tsvoter.in','TDP',132867,'202311300129'),('1252327','Jahnavi','Venkamsetty','7989666498','jahnavi.vv@tscd.in','Janasena',90000,'202311300129'),('1252328','Sohan','Mupparapu','8363369369','karthik.ch@tsvoter.in','YSRCP',696969,'202311300129');
/*!40000 ALTER TABLE `Candidates` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Demographic_Information`
--

DROP TABLE IF EXISTS `Demographic_Information`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Demographic_Information` (
  `Voter_ID` char(8) NOT NULL,
  `Age` int DEFAULT NULL,
  `Gender` varchar(255) DEFAULT NULL,
  `Ethnicity` varchar(255) DEFAULT NULL,
  `Education_level` varchar(255) DEFAULT NULL,
  `Income_level` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Voter_ID`),
  CONSTRAINT `Demographic_Information_ibfk_1` FOREIGN KEY (`Voter_ID`) REFERENCES `Voters` (`Voter_ID`) ON DELETE CASCADE,
  CONSTRAINT `Demographic_Information_chk_1` CHECK ((`Age` >= 18))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Demographic_Information`
--

LOCK TABLES `Demographic_Information` WRITE;
/*!40000 ALTER TABLE `Demographic_Information` DISABLE KEYS */;
INSERT INTO `Demographic_Information` VALUES ('29110011',18,'Male','Hindu','Intermediate','No Income'),('29110019',19,'Male','Muslim','Pre-Primary','No Income'),('29110039',19,'Male','Hindu','Intermediate','No Income'),('29112343',19,'Male','Parsi','SSC','No Income'),('29112369',19,'Male','Jain','SSC','No Income');
/*!40000 ALTER TABLE `Demographic_Information` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Election_Officials`
--

DROP TABLE IF EXISTS `Election_Officials`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Election_Officials` (
  `Official_ID` char(5) NOT NULL,
  `Fname` varchar(255) NOT NULL,
  `Lname` varchar(255) NOT NULL,
  `Phone_number` char(10) NOT NULL,
  `Email_ID` varchar(255) DEFAULT NULL,
  `Role_official` varchar(255) NOT NULL,
  `Event_ID` char(12) NOT NULL,
  PRIMARY KEY (`Official_ID`),
  KEY `Event_ID` (`Event_ID`),
  CONSTRAINT `Election_Officials_ibfk_1` FOREIGN KEY (`Event_ID`) REFERENCES `Election_events` (`Event_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Election_Officials`
--

LOCK TABLES `Election_Officials` WRITE;
/*!40000 ALTER TABLE `Election_Officials` DISABLE KEYS */;
INSERT INTO `Election_Officials` VALUES ('23231','Praneeth','Bommana','6344345394','praneeth.b@tsec.in','executive','202311300129'),('23232','Mitra','Somayaji','9344545342','mitra.somayaji@tsec.in','supervisor','202311300129'),('23233','Nijesh','Raghava','8919211702','nijesh.r@tsec.in','polling officer','202311300129'),('23234','Deekshitha','Sagiraju','9473145648','deekshitha.sagiraju@tsec.in','preceding officer','202311300129'),('23235','Vysistya','Karanam','7349345344','vysh.karanam@tsec.in','sub-executive','202311300129');
/*!40000 ALTER TABLE `Election_Officials` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Election_events`
--

DROP TABLE IF EXISTS `Election_events`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Election_events` (
  `Event_ID` char(12) NOT NULL,
  `Date_of_event` date NOT NULL,
  `Type_event` varchar(255) NOT NULL,
  `Election_Type` varchar(255) NOT NULL,
  PRIMARY KEY (`Event_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Election_events`
--

LOCK TABLES `Election_events` WRITE;
/*!40000 ALTER TABLE `Election_events` DISABLE KEYS */;
INSERT INTO `Election_events` VALUES ('198001060013','1980-01-06','Parliment','General'),('201708231028','2017-08-23','Assembly','By Election'),('201905150021','2019-05-15','Parliment','General'),('202211031129','2022-11-03','Assembly','By Election'),('202311300129','2023-11-30','Assembly','General');
/*!40000 ALTER TABLE `Election_events` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Event_station`
--

DROP TABLE IF EXISTS `Event_station`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Event_station` (
  `Station_ID` char(4) NOT NULL,
  `Event_ID` char(12) NOT NULL,
  PRIMARY KEY (`Station_ID`,`Event_ID`),
  KEY `Event_ID` (`Event_ID`),
  CONSTRAINT `Event_station_ibfk_1` FOREIGN KEY (`Event_ID`) REFERENCES `Election_Officials` (`Event_ID`) ON DELETE CASCADE,
  CONSTRAINT `Event_station_ibfk_2` FOREIGN KEY (`Station_ID`) REFERENCES `Polling_Stations` (`Station_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Event_station`
--

LOCK TABLES `Event_station` WRITE;
/*!40000 ALTER TABLE `Event_station` DISABLE KEYS */;
INSERT INTO `Event_station` VALUES ('1098','202311300129'),('1102','202311300129'),('1104','202311300129'),('1107','202311300129'),('1196','202311300129');
/*!40000 ALTER TABLE `Event_station` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Historical_Data`
--

DROP TABLE IF EXISTS `Historical_Data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Historical_Data` (
  `Event_ID` char(12) NOT NULL,
  `Date_of_event` date NOT NULL,
  `Election_type` varchar(255) NOT NULL,
  `Total_Votes` int NOT NULL,
  `Fname` varchar(255) NOT NULL,
  `Lname` varchar(255) NOT NULL,
  `Turnout_rate` int NOT NULL,
  PRIMARY KEY (`Event_ID`),
  CONSTRAINT `Historical_Data_ibfk_1` FOREIGN KEY (`Event_ID`) REFERENCES `Election_events` (`Event_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Historical_Data`
--

LOCK TABLES `Historical_Data` WRITE;
/*!40000 ALTER TABLE `Historical_Data` DISABLE KEYS */;
INSERT INTO `Historical_Data` VALUES ('198001060013','1980-01-06','General',65,'Vivek','Kavuri',77),('201708231028','2017-08-23','By Election',80,'Kriti','Madumadukala',78),('201905150021','2019-05-15','General',5,'Vivek','Kavuri',78),('202211031129','2022-11-03','By Election',100,'Kriti','Madumadukala',75),('202311300129','2023-11-30','General',150,'Vivek','Kavuri',44);
/*!40000 ALTER TABLE `Historical_Data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `List_of_candidates`
--

DROP TABLE IF EXISTS `List_of_candidates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `List_of_candidates` (
  `Candidate_Name` varchar(255) NOT NULL,
  `Ballot_ID` char(4) NOT NULL,
  PRIMARY KEY (`Candidate_Name`),
  KEY `Ballot_ID` (`Ballot_ID`),
  CONSTRAINT `List_of_candidates_ibfk_1` FOREIGN KEY (`Ballot_ID`) REFERENCES `Ballots` (`Ballot_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `List_of_candidates`
--

LOCK TABLES `List_of_candidates` WRITE;
/*!40000 ALTER TABLE `List_of_candidates` DISABLE KEYS */;
INSERT INTO `List_of_candidates` VALUES ('Kriti Madumadukala','1231'),('Vivek Kavuri','1231'),('Chandana Yalamanchili','1234'),('Sohan Mupparapau','1234'),('Jahnavi Venkamsetty','1252');
/*!40000 ALTER TABLE `List_of_candidates` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `List_of_parties`
--

DROP TABLE IF EXISTS `List_of_parties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `List_of_parties` (
  `Ballot_ID` char(4) NOT NULL,
  `Party_Name` varchar(255) NOT NULL,
  PRIMARY KEY (`Ballot_ID`,`Party_Name`),
  CONSTRAINT `List_of_parties_ibfk_1` FOREIGN KEY (`Ballot_ID`) REFERENCES `Ballots` (`Ballot_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `List_of_parties`
--

LOCK TABLES `List_of_parties` WRITE;
/*!40000 ALTER TABLE `List_of_parties` DISABLE KEYS */;
INSERT INTO `List_of_parties` VALUES ('1231','BRS'),('1234','BRS'),('1252','BJP'),('1252','BRS'),('1252','TDP');
/*!40000 ALTER TABLE `List_of_parties` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Polling_Stations`
--

DROP TABLE IF EXISTS `Polling_Stations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Polling_Stations` (
  `Station_ID` char(4) NOT NULL,
  `Address_station` varchar(255) NOT NULL,
  `Phone_Number` char(10) NOT NULL,
  `Email_ID` varchar(255) DEFAULT NULL,
  `Event_ID` char(12) NOT NULL,
  PRIMARY KEY (`Station_ID`),
  KEY `Event_ID` (`Event_ID`),
  CONSTRAINT `Polling_Stations_ibfk_1` FOREIGN KEY (`Event_ID`) REFERENCES `Election_events` (`Event_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Polling_Stations`
--

LOCK TABLES `Polling_Stations` WRITE;
/*!40000 ALTER TABLE `Polling_Stations` DISABLE KEYS */;
INSERT INTO `Polling_Stations` VALUES ('1098','1-9-322P/4,VNR Nagar,Secunderabad South,Telangana','7369586969','spyka.sec@tselc.in','202311300129'),('1102','5-502-1361/21/1,Pulivendhula,Kadapa West,Telangana','9169136901','rps.hyd.@tselc.in','202311300129'),('1104','10-2-2/4,Samatha Nagar,Ongole East,Telangana','8013066985','vb.mayuri@tselc.in','202311300129'),('1107','15-8-1000/2/1/G,Khammam North,Telangana','6916969571','dps.mamta@tselc.in','202311300129'),('1196','143-143-420/404/301,Erragutta Centre,Telangana','7702733269','rit.gutta@tselc.in','202311300129');
/*!40000 ALTER TABLE `Polling_Stations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Vote_Status`
--

DROP TABLE IF EXISTS `Vote_Status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Vote_Status` (
  `Voter_ID` char(8) NOT NULL,
  `Status_of_vote` varchar(255) NOT NULL,
  `Voted_on` date NOT NULL,
  PRIMARY KEY (`Voter_ID`),
  CONSTRAINT `Vote_Status_ibfk_1` FOREIGN KEY (`Voter_ID`) REFERENCES `Voters` (`Voter_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Vote_Status`
--

LOCK TABLES `Vote_Status` WRITE;
/*!40000 ALTER TABLE `Vote_Status` DISABLE KEYS */;
INSERT INTO `Vote_Status` VALUES ('29110011','YES','2023-11-30'),('29110019','NO','2023-11-30'),('29110039','NO','2023-11-30'),('29112343','YES','2023-11-30'),('29112369','YES','2023-11-30');
/*!40000 ALTER TABLE `Vote_Status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Voters`
--

DROP TABLE IF EXISTS `Voters`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Voters` (
  `Voter_ID` char(8) NOT NULL,
  `Fname` varchar(255) NOT NULL,
  `Lname` varchar(255) NOT NULL,
  `Phone_Number` char(10) DEFAULT NULL,
  `Email_ID` varchar(255) DEFAULT NULL,
  `DOB` date NOT NULL,
  `Address_voter` varchar(255) NOT NULL,
  `Station_ID` char(4) DEFAULT NULL,
  `Event_ID` char(12) NOT NULL,
  PRIMARY KEY (`Voter_ID`,`Event_ID`),
  KEY `Station_ID` (`Station_ID`),
  KEY `Event_ID` (`Event_ID`),
  CONSTRAINT `Voters_ibfk_1` FOREIGN KEY (`Station_ID`) REFERENCES `Polling_Stations` (`Station_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Voters_ibfk_2` FOREIGN KEY (`Event_ID`) REFERENCES `Election_events` (`Event_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Voters`
--

LOCK TABLES `Voters` WRITE;
/*!40000 ALTER TABLE `Voters` DISABLE KEYS */;
INSERT INTO `Voters` VALUES ('29110011','Yashwanth','Duggi','7989099505','yashwanth.duggi@tsvoter.in','2004-12-12','15-8-1003/2/1/G,Khammam North,Telangana','1107','202311300129'),('29110019','Krishna','Koushik','8156365369','krishna.koushik@tsvoter.in','2004-09-09','1-9-320P/4,VNR Nagar,Secunderabad South,Telangana','1098','202311300129'),('29110039','Sudhan','Kunapareddy','7989036498','sudhan.k@tsvoter.in','2004-05-03','1-9-312P/4,VNR Nagar,Secunderabad South,Telangana','1098','202311300129'),('29112343','Vamseedhar','Vanarasi','8169369369','vamseedhar.vanarasi@tsvoter.in','2004-01-24','143-143-410/404/301,Erragutta Centre,Telangana','1196','202311300129'),('29112369','Karthikeya','Chaganti','8365369369','karthik.ch@tsvoter.in','2004-05-11','123-143-410/404/301,Erragutta Centre,Telangana','1196','202311300129');
/*!40000 ALTER TABLE `Voters` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-02 14:23:40
