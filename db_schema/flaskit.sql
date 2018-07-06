-- MySQL dump 10.13  Distrib 8.0.11, for Win64 (x86_64)
--
-- Host: localhost    Database: flaskit
-- ------------------------------------------------------
-- Server version	8.0.11

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
create database if not exists flaskit;
USE flaskit;
--
-- Table structure for table `dh_account`
--

DROP TABLE IF EXISTS `dh_account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `dh_account` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `email` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `salt` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `reg_time` datetime DEFAULT NULL,
  `groups` varchar(128) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT '[]',
  PRIMARY KEY (`id`),
  UNIQUE KEY `username_UNIQUE` (`username`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dh_account`
--

LOCK TABLES `dh_account` WRITE;
/*!40000 ALTER TABLE `dh_account` DISABLE KEYS */;
INSERT INTO `dh_account` VALUES (1,'admin','admin@example.com','$2b$12$PR/CudpuKzmsJIdr.T6F1.gYyCJ8iw/79HEgwTGQzf6WXrRlPfIQK','81a4a1e1151208c1317cb25cb1dc2197b81e12e3','2017-09-14 15:58:31','[1]');
/*!40000 ALTER TABLE `dh_account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dh_menu`
--

DROP TABLE IF EXISTS `dh_menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `dh_menu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `show_name` varchar(20) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `icon` varchar(20) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `parent` int(11) DEFAULT NULL,
  `level` smallint(6) DEFAULT NULL,
  `url` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dh_menu`
--

LOCK TABLES `dh_menu` WRITE;
/*!40000 ALTER TABLE `dh_menu` DISABLE KEYS */;
INSERT INTO `dh_menu` VALUES (1,'项目说明','dashboard',NULL,0,'dashboard.dashboard'),(10,'账号权限管理','user',NULL,0,NULL),(11,'用户管理',NULL,10,1,'account.index'),(12,'组管理',NULL,10,1,'account.group'),(13,'Devops维护','wrench',NULL,0,NULL),(14,'平台权限管理',NULL,13,1,'menu.menu_list');
/*!40000 ALTER TABLE `dh_menu` ENABLE KEYS */;
UNLOCK TABLES;


--
-- Table structure for table `dh_group`
--

DROP TABLE IF EXISTS `dh_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `dh_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_name` varchar(20) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `menu_ids` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `desc` text CHARACTER SET utf8 COLLATE utf8_bin,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dh_group`
--

LOCK TABLES `dh_group` WRITE;
/*!40000 ALTER TABLE `dh_group` DISABLE KEYS */;
INSERT INTO `dh_group` VALUES (1,'管理员','[1,11,12,14]','绝对的权力'),(2,'一线','[1]','正面战场的勇士'),(3,'二线','[1]','魔法师般的决策者'),(4,'支撑','[1]','我是大内总管');
/*!40000 ALTER TABLE `dh_group` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-06-10 17:55:58
