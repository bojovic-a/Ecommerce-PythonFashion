-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 24, 2023 at 02:41 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flask_eprod`
--

-- --------------------------------------------------------

--
-- Table structure for table `komentar`
--

CREATE TABLE `komentar` (
  `idKorisnik` int(11) NOT NULL,
  `idProizvod` int(11) NOT NULL,
  `tekst_komentara` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `komentar`
--

INSERT INTO `komentar` (`idKorisnik`, `idProizvod`, `tekst_komentara`) VALUES
(30, 9, 'Ovo je komentar'),
(30, 9, 'Ovo je isto komentar'),
(30, 9, 'TENGUUUUUU'),
(36, 6, 'Lep dzemper, ja sam ga kupila, kupite ga i vi!!! '),
(4, 4, 'Koristim ga danju i nocu jer radim za gradsku cistocu !!1!!!1!!'),
(2, 3, 'Najjaci sorc na svetu!'),
(2, 3, 'Pere se samo na 40 stepeni, pazite ljudi!');

-- --------------------------------------------------------

--
-- Table structure for table `korisnik`
--

CREATE TABLE `korisnik` (
  `iDkorisnik` int(11) NOT NULL,
  `korisnicko_ime` varchar(45) NOT NULL,
  `lozinka` varchar(260) NOT NULL,
  `ime_prezime` varchar(45) NOT NULL,
  `datum_registracije` varchar(15) NOT NULL,
  `adresa` varchar(100) NOT NULL,
  `broj_telefona` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `TipKorisnika_idTipKorisnika` int(11) NOT NULL,
  `url_profilna_slika` varchar(255) NOT NULL,
  `stanje` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `korisnik`
--

INSERT INTO `korisnik` (`iDkorisnik`, `korisnicko_ime`, `lozinka`, `ime_prezime`, `datum_registracije`, `adresa`, `broj_telefona`, `email`, `TipKorisnika_idTipKorisnika`, `url_profilna_slika`, `stanje`) VALUES
(2, 'tpopovic', '7a70d0c0e38f4b861b5b3b2853b47b1dc932613d8551b371e127fb16d8ecdf98', 'Teodor Popovic', '2023-01-16', 'Carapanska 24', '0601234567', 'tpopovic@raf.rs', 2, 'images/user_images/blok21.jpg', 139200),
(3, 'ivananana', '37d3dc6b2935a1b1cb87dded5de7fe38f5b2483a406687f35a6820101472beb9', 'Ivana Bojovic', '2023-01-16', 'Marsala Tita 113', '0687654321', 'ibojovic@f.bg.ac.rs', 2, '/', 0),
(4, 'mjelic', '60c73ffbbdf88b9794b1e2822507105be8238c96bd565eda7950c81fae365f9e', 'Milan Jelic', '2023-01-16', 'Gancijeva 43', '0675467987', 'mjelic@raf.rs', 3, 'images/user_images/IMG_20230111_120649.jpg', 21800),
(6, 'test', '37268335dd6931045bdcdf92623ff819a64244b53d0e746d438797349d4da578', 'test test', '2023-01-17', 'test', '0677777777', 'test@test', 3, 'test', -9800),
(7, 'test1', '1b4f0e9851971998e732078544c96b36c3d01cedf7caa332359d6f1d83567014', 'test1', '2023-01-17', 'test1', 'test1', 'test1@test1', 3, 'test1', 0),
(8, 'test3', 'fd61a03af4f77d870fc21e05e7e80678095c92d808cfb3b5c279ee04c74aca13', 'test3', '2023-01-18', 'test3', 'test3', 'test3@test3', 3, 'test3', 93200),
(30, 'abojovic', '1d35ea76dd6ee01719fe9e17906c6e9f628a971a0e1117c2e68f317b6ce99432', 'Aleksandar Bojovic', '2023-01-20', 'Bulevar Arsenija Carnojevica 148', '0605331201', 'abojovic@abojovic', 1, 'images/user_images/abojovic.jpeg', 272180),
(31, 'martakaka', '251820405c0da22bf732e8e2f54d9531aeed861011fbfca0ba93027b65c2274d', 'Marta Kaka', '2023-01-20 17:3', 'Bulevar Arsenija Carnojevica 148/11/krevetic u dnevnoj sobi', '0600000000', 'marta@kaka.kuc', 3, '/images/user_images/martakaka.jpg', 84400),
(33, 'jborovic', '31933723c49abe18b42a6cac0e50318e0289561cb887a0f8fb1e69a7af73c537', 'Janko Borovic', '2023-01-20 19:1', 'Doktora Dragoslava Popovica 15', '0695304211', 'jborovic@raf.rs', 3, 'images/user_images/Screenshot_2023-01-20-19-14-02-544_com.whatsapp.jpg', 0),
(35, 'jnesic', 'da13a23f7e932836fcca684e761545dc926cbb4c065b8a6447079770c3804b03', 'Jovana Nesic', '2023-01-20 19:3', 'Kakanjska 8', '0616050031', 'jnesic55021@jus.ac.rs', 1, 'images/user_images/1674239709468.png', 0),
(36, 'neordinarna', 'a5d05e4ae895ffbf027975fca4fac2029245d67bf42d4ebc19b6ef4de2a627b5', 'Crki', '2023-01-21 16:5', 'Bele vode', '06409222846', 'crki@raf.rs', 3, 'images/user_images/IMG-20221210-WA0022.jpg', 120000),
(37, 'odisa', 'e49b58ff411c5e5f531ee344919ab8c0e6db5083754fd595a6397201a98404ed', 'Odi Nashville', '2023-01-23 19:0', 'Kakanjska 8/crna fotelja', '0699999999', 'odisa@fbi.gov.us', 2, 'images/user_images/DALL·E 2022-12-26 22.13.51 - A portrait of a short haired daschund construction worker.png', 115400),
(38, 'proba', '0e85510f97a75739aa35970c47e08178b868238b269c387e0a7abba49bbd4153', 'proba', '2023-01-24 01:3', 'proba', '060666666', 'proba@redirect.com', 3, 'images/user_images/basic.webp', 0),
(40, 'administrator', '4194d1706ed1f408d5e02d672777019f4d5385c766a8c6ca8acba3167d36a7b9', 'Administrator Administratoric', '2023-01-24 02:1', 'Administrativnih brigada 123', '0644444444', 'administrator@raf.rs', 1, 'images/user_images/basic.webp', 0);

-- --------------------------------------------------------

--
-- Table structure for table `lager`
--

CREATE TABLE `lager` (
  `idVelicina` int(11) NOT NULL,
  `idProizvod` int(11) NOT NULL,
  `kolicina` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `lager`
--

INSERT INTO `lager` (`idVelicina`, `idProizvod`, `kolicina`) VALUES
(3, 10, 62),
(4, 10, 38),
(3, 1, 30),
(1, 1, 79),
(1, 9, 3),
(2, 1, 30),
(4, 1, 26),
(5, 1, 30),
(6, 1, 30),
(1, 3, 30),
(2, 3, 30),
(4, 3, 29),
(5, 3, 28),
(6, 3, 28),
(1, 4, 20),
(3, 3, 30),
(5, 5, 25),
(6, 5, 35),
(1, 10, 60),
(6, 10, 30),
(5, 10, 25),
(2, 10, 30),
(1, 6, 24),
(2, 6, 18),
(3, 6, 20);

-- --------------------------------------------------------

--
-- Table structure for table `porudzbina`
--

CREATE TABLE `porudzbina` (
  `idKorpa` int(11) NOT NULL,
  `Korisnik_iDkorisnik` int(11) NOT NULL,
  `datum_porudzbine` date NOT NULL,
  `stanje_porudzbine` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `porudzbina`
--

INSERT INTO `porudzbina` (`idKorpa`, `Korisnik_iDkorisnik`, `datum_porudzbine`, `stanje_porudzbine`) VALUES
(5, 4, '2023-01-17', 'izvrsena'),
(7, 4, '2023-01-17', 'izvrsena'),
(8, 3, '2023-01-17', 'korpa'),
(12, 2, '2023-01-17', 'izvrsena'),
(13, 6, '2023-01-17', 'izvrsena'),
(14, 7, '2023-01-17', 'korpa'),
(15, 8, '2023-01-18', 'izvrsena'),
(16, 8, '2023-01-18', 'izvrsena'),
(17, 8, '2023-01-18', 'izvrsena'),
(18, 8, '2023-01-18', 'izvrsena'),
(19, 8, '2023-01-18', 'izvrsena'),
(20, 8, '2023-01-18', 'izvrsena'),
(21, 6, '2023-01-19', 'izvrsena'),
(22, 8, '2023-01-19', 'izvrsena'),
(23, 8, '2023-01-19', 'izvrsena'),
(24, 8, '2023-01-19', 'izvrsena'),
(25, 8, '2023-01-19', 'izvrsena'),
(26, 8, '2023-01-19', 'izvrsena'),
(27, 8, '2023-01-19', 'izvrsena'),
(28, 8, '2023-01-19', 'izvrsena'),
(29, 8, '2023-01-19', 'izvrsena'),
(30, 6, '2023-01-20', 'izvrsena'),
(31, 6, '2023-01-20', 'izvrsena'),
(32, 6, '2023-01-20', 'izvrsena'),
(33, 6, '2023-01-20', 'korpa'),
(34, 30, '2023-01-20', 'izvrsena'),
(35, 30, '2023-01-20', 'izvrsena'),
(36, 30, '2023-01-20', 'izvrsena'),
(37, 30, '2023-01-20', 'izvrsena'),
(38, 31, '2023-01-20', 'izvrsena'),
(39, 30, '2023-01-21', 'izvrsena'),
(40, 30, '2023-01-21', 'izvrsena'),
(41, 36, '2023-01-21', 'korpa'),
(42, 30, '2023-01-22', 'izvrsena'),
(43, 2, '2023-01-22', 'izvrsena'),
(44, 4, '2023-01-22', 'izvrsena'),
(45, 4, '2023-01-22', 'izvrsena'),
(46, 4, '2023-01-22', 'izvrsena'),
(47, 4, '2023-01-22', 'izvrsena'),
(48, 2, '2023-01-23', 'izvrsena'),
(49, 37, '2023-01-23', 'izvrsena');

-- --------------------------------------------------------

--
-- Table structure for table `proizvod`
--

CREATE TABLE `proizvod` (
  `idProizvod` int(11) NOT NULL,
  `naziv_proizvoda` varchar(45) NOT NULL,
  `proizvod_cena` float NOT NULL,
  `opis_proizvoda` varchar(45) NOT NULL,
  `url_slike` varchar(255) DEFAULT NULL,
  `u_prodaji` varchar(3) NOT NULL,
  `idProdavac` int(11) NOT NULL,
  `broj_prodatih` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `proizvod`
--

INSERT INTO `proizvod` (`idProizvod`, `naziv_proizvoda`, `proizvod_cena`, `opis_proizvoda`, `url_slike`, `u_prodaji`, `idProdavac`, `broj_prodatih`) VALUES
(1, 'Majica', 2000, 'Majica na kratke rukave', 'images/product_images/hmgoepprod.webp', 'da', 2, 8),
(3, 'Crni sorc', 1200, 'Kratki crni pamucni sorc', 'images/product_images/sorccrni.webp', 'da', 2, 5),
(4, 'Sorc Classic', 1700, 'Kratak sivi sorc', 'images/product_images/sorcsivi.jpg', 'da', 2, 0),
(5, 'Pantalone Casual', 5200, 'Duge bez pantalone', 'images/product_images/bezpantole.webp', 'da', 2, 0),
(6, 'Dzemper Stripes', 2300, 'Crno-beli prugasti dzemper', 'images/product_images/djemper.jfif', 'da', 2, 2),
(9, 'Kuca', 100000000, 'Braon jazavicar', 'images/product_images/DALLE_2022-12-26_22.00.48_-_A_portrait_of_a_daschund_drinking_beer.png', 'ne', 2, 0),
(10, 'Bele pantole', 2400, 'Fensi bele pantole sa kaisem', 'images/product_images/bele-pantole.webp', 'da', 30, 0),
(11, 'Karirana kosulja', 2300, 'Crveno-crna karirana kosulja sa dugim rukavim', 'images/product_images/karirana-crvena-kosulja.webp', 'da', 3, 0);

-- --------------------------------------------------------

--
-- Table structure for table `stavkaporudzbine`
--

CREATE TABLE `stavkaporudzbine` (
  `Korpa_idKorpa` int(11) NOT NULL,
  `Proizvod_idProizvod` int(11) NOT NULL,
  `kolicina` int(11) NOT NULL,
  `idVelicina` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `stavkaporudzbine`
--

INSERT INTO `stavkaporudzbine` (`Korpa_idKorpa`, `Proizvod_idProizvod`, `kolicina`, `idVelicina`) VALUES
(5, 1, 4, 1),
(13, 1, 3, 1),
(14, 5, 3, 1),
(8, 3, 3, 1),
(8, 5, 3, 1),
(12, 3, 3, 1),
(15, 1, 3, 1),
(16, 4, 3, 1),
(17, 4, 3, 1),
(18, 4, 3, 1),
(19, 5, 3, 1),
(20, 3, 3, 1),
(20, 5, 3, 1),
(13, 3, 3, 1),
(21, 3, 3, 1),
(22, 5, 3, 1),
(23, 1, 3, 1),
(24, 1, 3, 1),
(25, 3, 3, 1),
(26, 3, 3, 1),
(27, 1, 3, 1),
(28, 3, 3, 1),
(29, 4, 3, 1),
(29, 5, 3, 1),
(30, 1, 3, 1),
(30, 3, 3, 1),
(31, 3, 5, 1),
(31, 1, 2, 1),
(32, 5, 4, 1),
(33, 3, 1, 1),
(33, 1, 1, 1),
(34, 1, 1, 1),
(35, 6, 2, 1),
(36, 3, 1, 1),
(36, 5, 1, 1),
(37, 1, 1, 1),
(38, 5, 3, 1),
(38, 6, 1, 1),
(39, 3, 1, 1),
(40, 9, 5, 1),
(41, 9, 1, 1),
(7, 3, 2, 1),
(12, 10, 1, 1),
(43, 10, 1, 3),
(44, 1, 1, 4),
(45, 1, 1, 4),
(45, 5, 1, 5),
(46, 3, 1, 5),
(46, 1, 1, 4),
(46, 3, 1, 6),
(47, 1, 1, 1),
(47, 1, 1, 3),
(48, 1, 2, 3),
(49, 6, 2, 2),
(42, 3, 1, 4);

-- --------------------------------------------------------

--
-- Table structure for table `tipkorisnika`
--

CREATE TABLE `tipkorisnika` (
  `idTipKorisnika` int(11) NOT NULL,
  `naziv_tipa` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tipkorisnika`
--

INSERT INTO `tipkorisnika` (`idTipKorisnika`, `naziv_tipa`) VALUES
(1, 'administrator'),
(2, 'prodavac'),
(3, 'kupac');

-- --------------------------------------------------------

--
-- Table structure for table `velicina`
--

CREATE TABLE `velicina` (
  `idVelicina` int(11) NOT NULL,
  `oznaka_velicine` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `velicina`
--

INSERT INTO `velicina` (`idVelicina`, `oznaka_velicine`) VALUES
(1, 'XS'),
(2, 'S'),
(3, 'M'),
(4, 'L'),
(5, 'XL'),
(6, 'XXL');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `komentar`
--
ALTER TABLE `komentar`
  ADD KEY `idKorisnik` (`idKorisnik`),
  ADD KEY `idProizvod` (`idProizvod`);

--
-- Indexes for table `korisnik`
--
ALTER TABLE `korisnik`
  ADD PRIMARY KEY (`iDkorisnik`),
  ADD UNIQUE KEY `KorisnikID_UNIQUE` (`iDkorisnik`),
  ADD KEY `fk_Korisnik_TipKorisnika1_idx` (`TipKorisnika_idTipKorisnika`);

--
-- Indexes for table `lager`
--
ALTER TABLE `lager`
  ADD KEY `idProizvod` (`idProizvod`),
  ADD KEY `idVelicina` (`idVelicina`);

--
-- Indexes for table `porudzbina`
--
ALTER TABLE `porudzbina`
  ADD PRIMARY KEY (`idKorpa`),
  ADD UNIQUE KEY `idKorpa_UNIQUE` (`idKorpa`),
  ADD KEY `fk_Korpa_Korisnik1_idx` (`Korisnik_iDkorisnik`);

--
-- Indexes for table `proizvod`
--
ALTER TABLE `proizvod`
  ADD PRIMARY KEY (`idProizvod`),
  ADD UNIQUE KEY `idProizvod_UNIQUE` (`idProizvod`);

--
-- Indexes for table `stavkaporudzbine`
--
ALTER TABLE `stavkaporudzbine`
  ADD KEY `fk_StavkaKorpe_Korpa1_idx` (`Korpa_idKorpa`),
  ADD KEY `fk_StavkaKorpe_Proizvod1_idx` (`Proizvod_idProizvod`),
  ADD KEY `idVelicina` (`idVelicina`);

--
-- Indexes for table `tipkorisnika`
--
ALTER TABLE `tipkorisnika`
  ADD PRIMARY KEY (`idTipKorisnika`),
  ADD UNIQUE KEY `idTipProizvoda_UNIQUE` (`idTipKorisnika`);

--
-- Indexes for table `velicina`
--
ALTER TABLE `velicina`
  ADD PRIMARY KEY (`idVelicina`),
  ADD UNIQUE KEY `idVelicina_UNIQUE` (`idVelicina`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `korisnik`
--
ALTER TABLE `korisnik`
  MODIFY `iDkorisnik` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `porudzbina`
--
ALTER TABLE `porudzbina`
  MODIFY `idKorpa` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;

--
-- AUTO_INCREMENT for table `proizvod`
--
ALTER TABLE `proizvod`
  MODIFY `idProizvod` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `tipkorisnika`
--
ALTER TABLE `tipkorisnika`
  MODIFY `idTipKorisnika` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `velicina`
--
ALTER TABLE `velicina`
  MODIFY `idVelicina` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `komentar`
--
ALTER TABLE `komentar`
  ADD CONSTRAINT `komentar_ibfk_1` FOREIGN KEY (`idKorisnik`) REFERENCES `korisnik` (`iDkorisnik`),
  ADD CONSTRAINT `komentar_ibfk_2` FOREIGN KEY (`idProizvod`) REFERENCES `proizvod` (`idProizvod`);

--
-- Constraints for table `korisnik`
--
ALTER TABLE `korisnik`
  ADD CONSTRAINT `fk_Korisnik_TipKorisnika1` FOREIGN KEY (`TipKorisnika_idTipKorisnika`) REFERENCES `tipkorisnika` (`idTipKorisnika`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `lager`
--
ALTER TABLE `lager`
  ADD CONSTRAINT `lager_ibfk_1` FOREIGN KEY (`idProizvod`) REFERENCES `proizvod` (`idProizvod`),
  ADD CONSTRAINT `lager_ibfk_2` FOREIGN KEY (`idVelicina`) REFERENCES `velicina` (`idVelicina`);

--
-- Constraints for table `porudzbina`
--
ALTER TABLE `porudzbina`
  ADD CONSTRAINT `fk_Korpa_Korisnik1` FOREIGN KEY (`Korisnik_iDkorisnik`) REFERENCES `korisnik` (`iDkorisnik`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `stavkaporudzbine`
--
ALTER TABLE `stavkaporudzbine`
  ADD CONSTRAINT `fk_StavkaKorpe_Korpa1` FOREIGN KEY (`Korpa_idKorpa`) REFERENCES `porudzbina` (`idKorpa`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_StavkaKorpe_Proizvod1` FOREIGN KEY (`Proizvod_idProizvod`) REFERENCES `proizvod` (`idProizvod`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `stavkaporudzbine_ibfk_1` FOREIGN KEY (`idVelicina`) REFERENCES `velicina` (`idVelicina`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
