--
-- MySQL 5.5.5
-- Tue, 20 Oct 2020 06:48:29 +0000
--

CREATE TABLE `testapi` (
   `id` int not null auto_increment,
   `name` varchar(100),
   'age' int,
   'phone' int, 
   'username' varchar(100) not null,
   'password' varchar(100) not null,
   'Address' varchar(500) not null,
   'City' varchar(100) not null,
   'State' varchar (100) not null,
   'BodyTemperature' float,
   'RunnyNose' int,
   'BodyAche' int,
   'DifficultyinBreathing' int,
   'DryCough' int, 
   'InfectionProbab' float,
   PRIMARY KEY (`phone`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4