###Assignment 7

##MySql Database

Make sure your database has a user 'root' with password: admin.

To your database, add the following schema:

'CREATE SCHEMA `test_storage` ;'

Add the following tables:

'''
CREATE TABLE `product_info` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` varchar(1000) NOT NULL,
  `normal_price` decimal(6,0) NOT NULL,
  `bonus_price` decimal(6,0) DEFAULT NULL,
  `photo` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
);
'''

'''
CREATE TABLE `order_items` (
  `order_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `qt` int(11) NOT NULL
);
'''

'''
CREATE TABLE `order_head` (
  `order_id` int(11) NOT NULL,
  `fname` varchar(45) NOT NULL,
  `lname` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `phone` int(11) NOT NULL,
  `street` varchar(45) NOT NULL,
  `postcode` int(11) NOT NULL,
  `city` varchar(45) NOT NULL,
  PRIMARY KEY (`order_id`));
'''

#This program is only able to run locally: 'localhost'