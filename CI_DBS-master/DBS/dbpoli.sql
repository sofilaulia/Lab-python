-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 13, 2021 at 06:58 PM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.3.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbpoli`
--

-- --------------------------------------------------------

--
-- Table structure for table `bmi_pasien`
--

CREATE TABLE `bmi_pasien` (
  `id` int(11) NOT NULL,
  `tanggal` date DEFAULT NULL,
  `berat` double DEFAULT NULL,
  `tinggi` double DEFAULT NULL,
  `bmi` double DEFAULT NULL,
  `status_bmi` varchar(45) DEFAULT NULL,
  `catatan` varchar(100) DEFAULT NULL,
  `pasien_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bmi_pasien`
--

INSERT INTO `bmi_pasien` (`id`, `tanggal`, `berat`, `tinggi`, `bmi`, `status_bmi`, `catatan`, `pasien_id`) VALUES
(1, '2020-11-02', 57.5, 150, 25.5555556, 'Kelebihan Berat Badan', 'tetap semangat', 1),
(2, '2021-01-02', 79.3, 173, 26.4960406, 'Kelebihan Berat Badan', 'ayo olahraga!', 2),
(3, '2021-02-03', 90, 160, 28.125, 'Kelebihan Berat Badan', 'harus olahraga rutin nih', 3);

-- --------------------------------------------------------

--
-- Table structure for table `pasien`
--

CREATE TABLE `pasien` (
  `id` int(11) NOT NULL,
  `kode` varchar(6) NOT NULL,
  `nama` varchar(40) NOT NULL,
  `gender` char(1) DEFAULT NULL,
  `tmpt_lahir` varchar(30) DEFAULT NULL,
  `tgl_lahir` date DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `pasien`
--

INSERT INTO `pasien` (`id`, `kode`, `nama`, `gender`, `tmpt_lahir`, `tgl_lahir`, `email`) VALUES
(1, 'P00001', 'Dewi Gita', 'P', 'Jakarta', '2000-04-03', 'dewi.gita@gmail.com'),
(2, 'P00003', 'Armand Maulana', 'L', 'Jakarta', '1976-11-03', 'armina@gmail.com'),
(3, 'P00004', 'Anton', 'L', 'Semarang', '2001-10-03', 'anton@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bmi_pasien`
--
ALTER TABLE `bmi_pasien`
  ADD PRIMARY KEY (`id`),
  ADD KEY `pasien_id` (`pasien_id`);

--
-- Indexes for table `pasien`
--
ALTER TABLE `pasien`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `kode` (`kode`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bmi_pasien`
--
ALTER TABLE `bmi_pasien`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `pasien`
--
ALTER TABLE `pasien`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `bmi_pasien`
--
ALTER TABLE `bmi_pasien`
  ADD CONSTRAINT `pasien_id` FOREIGN KEY (`pasien_id`) REFERENCES `pasien` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
