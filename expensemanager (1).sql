-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 17, 2021 at 07:58 AM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 7.4.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `expensemanager`
--

-- --------------------------------------------------------

--
-- Table structure for table `budget`
--

CREATE TABLE `budget` (
  `id` int(11) NOT NULL,
  `amount` int(11) NOT NULL,
  `budgetdate` varchar(255) NOT NULL,
  `emailId` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `budget`
--

INSERT INTO `budget` (`id`, `amount`, `budgetdate`, `emailId`) VALUES
(2, 5000, '6/22/19', 'admin@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `ID` int(11) NOT NULL,
  `categoryName` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL,
  `emailId` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`ID`, `categoryName`, `description`, `type`, `emailId`) VALUES
(2, 'personal', 'personal expences.\n', 'Cash', 'admin@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `expences`
--

CREATE TABLE `expences` (
  `id` int(11) NOT NULL,
  `amount` int(11) NOT NULL,
  `payee` varchar(255) NOT NULL,
  `remarks` varchar(255) NOT NULL,
  `category` varchar(255) NOT NULL,
  `TransectionType` varchar(255) NOT NULL,
  `emailid` varchar(255) NOT NULL,
  `date` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `expences`
--

INSERT INTO `expences` (`id`, `amount`, `payee`, `remarks`, `category`, `TransectionType`, `emailid`, `date`) VALUES
(2, 5000, 'amazon', 'personal\n', 'Personal', 'Cash', 'admin@gmail.com', '2021-08-14'),
(3, 5000, 'amazone', 'personal\n', 'Personal', 'Credit Card', 'admin@gmail.com', '2021-08-14'),
(5, 5000, 'das', 'asdf\n', 'Entertainment', 'Check', 'admin@gmail.com', '16/08/21'),
(6, 50000, 'u', 'dj\n', 'Family', 'Cash', 'admin@gmail.com', '16/08/21'),
(7, 10000, 'adf', 'asdf\n', 'Entertainment', 'Check', 'admin@gmail.com', '16/08/21'),
(8, 6000, 'df', 'dasf\n', 'Family', 'Check', 'admin@gmail.com', '16/08/21');

-- --------------------------------------------------------

--
-- Table structure for table `income`
--

CREATE TABLE `income` (
  `id` int(11) NOT NULL,
  `amount` varchar(255) NOT NULL,
  `payer` varchar(255) NOT NULL,
  `remarks` varchar(255) NOT NULL,
  `category` varchar(255) NOT NULL,
  `transectiontype` varchar(255) NOT NULL,
  `emailID` varchar(255) NOT NULL,
  `date` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `income`
--

INSERT INTO `income` (`id`, `amount`, `payer`, `remarks`, `category`, `transectiontype`, `emailID`, `date`) VALUES
(1, '140000', '', 'salary\n', '', 'Bank', 'admin@gmail.com', ''),
(3, '5000', '.!toplevel.!entry2', 'salary\n', 'Salary', 'Bank', 'admin@gmail.com', '');

-- --------------------------------------------------------

--
-- Table structure for table `transection`
--

CREATE TABLE `transection` (
  `TransectionID` int(11) NOT NULL,
  `amount` int(11) NOT NULL,
  `remarks` varchar(255) NOT NULL,
  `category` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `transection`
--

INSERT INTO `transection` (`TransectionID`, `amount`, `remarks`, `category`) VALUES
(3, 500, 'personal\n', 2);

-- --------------------------------------------------------

--
-- Table structure for table `userdata`
--

CREATE TABLE `userdata` (
  `email` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `mobile` varchar(255) NOT NULL,
  `Password` varchar(255) NOT NULL,
  `PAN` varchar(255) DEFAULT NULL,
  `fathersName` varchar(255) DEFAULT NULL,
  `aadhaar` int(11) DEFAULT NULL,
  `photo` varchar(255) DEFAULT NULL,
  `lastLogin` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `userdata`
--

INSERT INTO `userdata` (`email`, `name`, `mobile`, `Password`, `PAN`, `fathersName`, `aadhaar`, `photo`, `lastLogin`) VALUES
('admin@gmail.com', 'admin', '123456789', '98765', NULL, NULL, NULL, NULL, '2021-08-16 16:48:49');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `budget`
--
ALTER TABLE `budget`
  ADD PRIMARY KEY (`id`),
  ADD KEY `emailId` (`emailId`);

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `expences`
--
ALTER TABLE `expences`
  ADD PRIMARY KEY (`id`),
  ADD KEY `expences_ibfk_1` (`emailid`);

--
-- Indexes for table `income`
--
ALTER TABLE `income`
  ADD PRIMARY KEY (`id`),
  ADD KEY `emailID` (`emailID`);

--
-- Indexes for table `transection`
--
ALTER TABLE `transection`
  ADD PRIMARY KEY (`TransectionID`),
  ADD KEY `category` (`category`);

--
-- Indexes for table `userdata`
--
ALTER TABLE `userdata`
  ADD PRIMARY KEY (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `budget`
--
ALTER TABLE `budget`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `expences`
--
ALTER TABLE `expences`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `income`
--
ALTER TABLE `income`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `transection`
--
ALTER TABLE `transection`
  MODIFY `TransectionID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `budget`
--
ALTER TABLE `budget`
  ADD CONSTRAINT `budget_ibfk_1` FOREIGN KEY (`emailId`) REFERENCES `userdata` (`email`);

--
-- Constraints for table `expences`
--
ALTER TABLE `expences`
  ADD CONSTRAINT `expences_ibfk_1` FOREIGN KEY (`emailid`) REFERENCES `userdata` (`email`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `income`
--
ALTER TABLE `income`
  ADD CONSTRAINT `income_ibfk_1` FOREIGN KEY (`emailID`) REFERENCES `userdata` (`email`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `transection`
--
ALTER TABLE `transection`
  ADD CONSTRAINT `transection_ibfk_1` FOREIGN KEY (`category`) REFERENCES `category` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
