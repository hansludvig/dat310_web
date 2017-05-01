
DROP TABLE IF EXISTS `order_head`;

CREATE TABLE `order_head` (
  `order_id` int(11) NOT NULL,
  `fname` varchar(45) NOT NULL,
  `lname` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `phone` int(11) NOT NULL,
  `street` varchar(45) NOT NULL,
  `postcode` int(11) NOT NULL,
  `city` varchar(45) NOT NULL,
  `order_date` datetime NOT NULL,
  PRIMARY KEY (`order_id`)
);

--
-- Dumping data for table `order_head`
--

INSERT INTO `order_head` VALUES (101,'Hans Ludvig','Kleivdal','hans@me.com',98488415,'Kamepen 8',4024,'Stavanger','2017-05-01 04:31:01'),(102,'Erlend','rekve','reck@me.com',12341234,'Løkke 5',1234,'Stavanger','2017-05-01 04:47:19'),(103,'Andreas','Kvist','akvi@kvist.no',73292398,'Ullandh 5',5432,'Brokeland','2017-05-01 04:36:11'),(104,'Voggie','vugar','vog@vu.com',12341234,'Pavligjon 5',5433,'Uis','2017-05-01 04:48:01'),(105,'Mats','Net','mat@net.com',98761234,'Stokka 55',9087,'Stokka','2017-05-01 04:48:43'),(106,'Ivan','Lui','ivan@luv.com',9875323,'Ullanhaug 65',2345,'Brustad','2017-05-01 04:49:39'),(107,'Lola','Lui','Lola@luv.com',23453456,'Ullanhaug 65',2345,'Brustad','2017-05-01 04:50:19'),(108,'Fredrik','Haugsand','fre@haug.com',98745438,'Uis 3',3453,'uis','2017-05-01 04:52:04'),(109,'Sondre','Hagen','son@hagen.com',98745438,'Uelands 3',1,'Oslo','2017-05-01 04:53:58'),(110,'Jørgen','Gran','Jorgen@me.com',64331234,'Lilly 34',3001,'Lillehammer','2017-05-01 04:54:42'),(111,'Nico','Jacobsen','nico@me.com',64321234,'Lilly 34',3001,'Lillehammer','2017-05-01 04:55:16'),(112,'Preben','Kirkholm','pre@me.com',69882345,'Moldeveien 34',6001,'Molde','2017-05-01 04:56:03'),(113,'Ola','Nordman','ola@norge.com',12345875,'Norge 34',6221,'NorgeBy','2017-05-01 04:56:52'),(114,'Kari','Nordman','kari@norge.com',12346875,'Norge 34',6221,'NorgeBy','2017-05-01 04:57:18'),(115,'Aleks','Slodebo','al@skod.com',65436245,'Kålsåsvein 4',4532,'Kålsås','2017-05-01 04:58:12'),(116,'Marianne','Moi','mr@moi.com',67436245,'Kålsåsvein 4',4532,'Kålsås','2017-05-01 04:58:37'),(117,'Martin','Brætt','mr@braa.com',67436245,'Hosleveine 49',5432,'Hosle','2017-05-01 04:59:26'),(118,'Frida','Holds','fr@hol.com',67736245,'Hosleveine 49',5432,'Hosle','2017-05-01 04:59:48'),(119,'Showman','Sho','showman@sho.com',67736745,'Uis 49',6542,'Stavanger','2017-05-01 05:00:54'),(120,'Marie','Kvist','marie@kvis.com',67736745,'Stokka 49',6542,'Stokka','2017-05-01 05:01:33'),(121,'Andreas','Hove','andreas@hove.com',67736745,'Nestunveien 49',6542,'Bergen','2017-05-01 05:02:14');

--
-- Table structure for table `order_items`
--

DROP TABLE IF EXISTS `order_items`;

CREATE TABLE `order_items` (
  `order_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `qt` int(11) NOT NULL
);
--
-- Dumping data for table `order_items`
--


INSERT INTO `order_items` VALUES (101,12,1),(102,11,4),(102,13,4),(102,14,6),(102,15,7),(103,14,1),(104,11,4),(104,13,1),(104,15,3),(105,13,3),(106,10,9),(106,14,3),(106,15,2),(107,11,2),(107,12,3),(107,13,3),(107,14,2),(107,15,1),(108,14,1),(109,13,10),(109,14,10),(110,10,1),(110,14,5),(111,15,2),(111,12,20),(111,13,2),(112,11,2),(112,15,4),(113,10,4),(113,13,1),(113,14,1),(114,14,4),(114,13,2),(115,12,2),(116,10,2),(116,13,3),(116,12,3),(117,12,3),(117,11,5),(118,11,5),(118,10,5),(118,12,5),(118,13,5),(118,15,5),(118,14,5),(119,14,2),(119,12,2),(120,12,2),(120,15,2),(121,11,20);

--
-- Table structure for table `product_info`
--

DROP TABLE IF EXISTS `product_info`;

CREATE TABLE `product_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` varchar(1000) NOT NULL,
  `normal_price` decimal(6,0) NOT NULL,
  `bonus_price` decimal(6,0) DEFAULT NULL,
  `photo` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
);

--
-- Dumping data for table `product_info`
--

INSERT INTO `product_info` VALUES (10,'Scuderia Ferrari Team T-Shirt Red','The Scuderia Ferrari Team T-shirt is the official replica of the item of clothing worn by the men of the Maranello team on the World F1 2014 race tracks, including the logo of the Team and of all the sponsors. \nThe unique details thus characterise this item of clothing such as the inserts in contrasting colour, the embroidered Puma logo and the design of the three-colour Italian flag on the right sleeve.\n100% Cotton',120,96,'../static/ferrari_Tshirt.png'),(11,'Mercedes AMG Petronas Lewis Hamilton 2014 World Champion T-Shirt','Mercedes AMG Petronas Lewis Hamilton 2014 World Champion T-Shirt',48,NULL,'../static/mercedes_Tshirt.png'),(12,'Lotus F1 Team Replica Rain Jacket','Lotus F1 Team Replica Rain Jacket',194,136,'../static/lotus_jacket.png'),(13,'Scuderia Ferrari Raikkonen Driver Cap','Scuderia Ferrari Raikkonen Driver Cap',48,16,'../static/ferrari_cap.png'),(14,'Scuderia Ferrari Beanie','Scuderia Ferrari Beanie',40,32,'../static/ferrari_beanie.png'),(15,'Mercedes AMG Petronas Rosberg Driver Cap','Mercedes AMG Petronas Rosberg Driver Cap',48,24,'../static/mercedes_cap.png');


--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `user_name` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`user_name`)
);

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
INSERT INTO `users` VALUES ('test','pbkdf2:sha1:1000$N3ofe7Rq$f5d0a5b2d15b566477fad2753ef0b3bd7ae3d072');
UNLOCK TABLES;

-- Dump completed on 2017-05-01  6:36:37
