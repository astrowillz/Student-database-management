-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 19, 2023 at 02:10 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mypartproject_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `students_guidb`
--

CREATE TABLE `students_guidb` (
  `MatricNo` int(225) DEFAULT NULL,
  `Firstname` varchar(225) DEFAULT NULL,
  `Lastname` varchar(225) DEFAULT NULL,
  `Email` varchar(225) DEFAULT NULL,
  `Mobilenumber` int(255) DEFAULT NULL,
  `Yearofentry` int(255) DEFAULT NULL,
  `Gender` char(10) DEFAULT NULL,
  `DOB` varchar(255) DEFAULT NULL,
  `DEPARTMENT` varchar(255) DEFAULT NULL,
  `FACULTY` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `students_guidb`
--

INSERT INTO `students_guidb` (`MatricNo`, `Firstname`, `Lastname`, `Email`, `Mobilenumber`, `Yearofentry`, `Gender`, `DOB`, `DEPARTMENT`, `FACULTY`) VALUES
(23456, 'fghjk', 'vghjm,', 'dfghjkl@gmail.com', 67845678, 2001, 'Male', '12-12-12', 'vghjkl', 'dfhjk'),
(67890, 'ghjkl', 'fghjk', 'cvbnm@gmail.com', 6789, 2002, 'Female', '12-12-12', 'sdfghjk', 'cghj');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
