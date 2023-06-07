DROP TABLE IF EXISTS `juser`;
CREATE TABLE `juser` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_juser_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOCK TABLES `juser` WRITE;
INSERT INTO `juser` VALUES (2,'string','string','2023-04-21 11:48:44','2023-04-21 11:48:44');
UNLOCK TABLES;
