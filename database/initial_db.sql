CREATE TABLE `customers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`));
  
INSERT INTO `customers` VALUES (1,'Firstname1 Lastname1','Hyderabad'),(2,'Firstname2 Lastname2','Delhi'),(3,'Firstname3 Lastname3','Mumbai');


CREATE TABLE `accounts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` int DEFAULT NULL,
  `customerID` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `customerID` FOREIGN KEY (`customerID`) REFERENCES `customers` (`id`));
  
INSERT INTO `accounts` VALUES (1,1234567,1),(2,09876544,2),(3,567889877,2);