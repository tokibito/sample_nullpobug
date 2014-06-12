DROP TABLE IF EXISTS `bundle`;
CREATE TABLE `bundle` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bundle_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `bundle_item`;
CREATE TABLE `bundle_item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bundle_id` int(11) NOT NULL,
  `item_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `item`;
CREATE TABLE `item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) NOT NULL,
  `name` varchar(100) NOT NULL,
  `price` int(11) DEFAULT NULL,
  `category` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

LOCK TABLES `item` WRITE;
INSERT INTO `item` VALUES 
  (1,'001','りんご',100,'fruit'),
  (2,'002','みかん',50,'fruit'),
  (3,'003','じゃがいも',80,'vegetable'),
  (4,'004','にんじん',90,'vegetable'),
  (5,'005','たまねぎ',60,'vegetable');
UNLOCK TABLES;
